import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        # "https://world.huanqiu.com/",
        "https://www.xuexila.com/"
    ]
# /html/head/title
    def parse(self, response):
        a =response.xpath('/html/head/title/text()')[0].root
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)