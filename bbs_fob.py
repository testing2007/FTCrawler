import requests
from lxml import etree
from lxml import html

def getHTML(url):
    # 发送HTTP请求时的HEAD信息，用于伪装为浏览器
    heads = {  
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    # print('{}'.format(url) )
    # 不压缩html，最大链接时间为10妙
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url, headers=heads, verify=False, timeout=10)
    # 为防止出错，编码utf-8
    res.encoding = 'utf-8'
    return res.content

def parseHTMLContent(content, lzUID, pageSize):    
    # 将html构建为Xpath模式
    root = etree.HTML(content)
    
    html = ''
    for i in range(1, pageSize):
        subNodeId = '/html/body/center/div[5]/form/div[' +str(i)+']'
        subUsrNodeId = subNodeId + '/table/tr/td[1]/div'
        subContentNodeId = subNodeId + '/table/tr/td[2]/table/tr[2]/td'
        subUsrNodeInfo = root.xpath(subUsrNodeId + '/text()')
        bFound = False
        # subUsrNodeInfo = ['\n', '\n', '\n', '\n', '\n', ' \xa0\n', '\nUID 2040879', '\n精华 ', '\n积分 10893', '\n帖子 1277', '\n福步币 10 块', '\n阅读权限 120', '\n注册 2012-10-12', '\n状态 离线\n']
        if isinstance(subUsrNodeInfo, list):
            for userInfoItem in subUsrNodeInfo:
                subLen = len(userInfoItem)
                if('\nUID ' in userInfoItem and  subLen > 5 and userInfoItem[5:subLen] == lzUID):
                    print('i get it {}'.format(userInfoItem))
                    break;

        subContentNode = root.xpath(subContentNodeId)
        if subContentNode:
            html += '<tr>'
            html += etree.tostring(subContentNode[0], pretty_print=True, encoding="unicode")
            html += '</tr>'

    print(html)
    return html

if __name__ == '__main__':
    
    # 参数
    domain = 'https://bbs.fobshanghai.com'
    uri = 'viewthread.php'
    paramTid = '5391454' #'4403848'
    paramBtwaf = '11556039' # '42299993' #变化
    lzUID = '2753' #'2040879'
    pageSize = 15 # 每页大小
    pageCount = 5 # 总页数

    # 获取需要的内容
    interestContent = ''
    for i in range(1, pageCount):
        url = domain + '/' + uri + '?' + 'tid='+paramTid + '&page='+str(i)+'&btwaf='+str(paramTid)
        content = getHTML(url)
        if len(content) > 0:
            interestContent += parseHTMLContent(content, lzUID, pageSize)

    # 将获取到的内容拼接到 <table></table> 标签里面，最后写入文件
    mainContent = '<html>\
    <head>\
        <!-- <meta http-equiv="Content-Type" content="text/html; charset=gbk"> -->\
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">\
        <link rel="dns-prefetch" href="//www.google-analytics.com">\
        <title>bbs.fob爬虫</title>\
        <body>\
            <table class="content">\
            </table>\
        </body>\
    </html>'
    htmlRoot = html.fromstring(mainContent)
    if len(interestContent) > 0:
        tableEle = htmlRoot.find('.//body//table')
        if tableEle != None:
            newEle = html.fromstring(interestContent)
            tableEle.insert(0, newEle)

            htmlContent = html.tostring(htmlRoot)
            print(htmlContent)
            
            fileName = 'fobshagnhai-'+lzUID + '.html'
            with open(fileName, 'wb') as f:
                f.write(htmlContent)

