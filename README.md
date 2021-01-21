[TOC]
#### 环境搭建
##### 安装虚拟环境的命令
* sudo pip install virtualenv #安装虚拟环境
* sudo pip install virtualenvwrapper #安装虚拟环境扩展包
* vi ~/.bashrc 或 vi ~/.bash_profile 文件添加两行
          export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3 #如果电脑之前存在python2， 就再加这句
          export WORKON_HOME=$HOME/.virtualenvs
          source /usr/local/bin/virtualenvwrapper.sh
* source .bashrc 或 # source .bash_profile 使修改生效

##### Flask 虚拟环境搭建 及 常用命令
* 虚拟环境：
    * [安装可能遇到的问题](https://app.yinxiang.com/shard/s41/nl/9936432/7085c175-f2ef-4ae2-ae0d-0583cb54cbb3/)
    
* 创建虚拟环境命令
    * mkvirtualenv 虚拟环境名 #默认python2环境, 可以在 $HOME/.virtualenvs 这里查看
    * mkvirtualenv -p python3 虚拟环境名 #创建python3 虚拟环境
  
* 进入虚拟环境工作
    * workon 虚拟环境名

* 查看机器上有多少个虚拟环境
    * workon 空格 + 两个tab键
    * lsvirtualenv -b #Mac端

* 退出虚拟环境
    * deactivate

* 删除虚拟环境
    * rmvirtualenv 虚拟环境名

* 查看虚拟环境下安装的包信息
    * pip list
    * pip freeze #发布时使用

* 虚拟环境下安装包命令
    * pip install 包名 #不能在前面使用sudo， 这样就会安装到系统目录下
    * pip install flask==0.10.1 #0.10.1是版本号

* 导出工程依赖包并安装
    * pip freeze > requirements.txt （导出依赖包）
    * pip install -r requirements.txt （依次安装依赖包）

* 安装flask
    * pip install -U Flask

#### vscode配置
##### tutorial (scrapy工程例子)
##### bbs_fob （bbs.fobshanghai.com 论坛信息抓取例子）
