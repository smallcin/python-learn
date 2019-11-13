# coding=utf-8
import urllib
import re


def getHtmlContent(url):
    page = urllib.urlopen(url)
    return page.read()


# 从html中解析出所有jpg图片的url
# 百度贴吧html中jpg图片的url格式为：<img ... src="XXX.jpg" width=...>
def getJPGs(html):

    # 解析jpg图片url的正则
    jpgreg = re.compile(r'<img.+?src="(.+?\.jpg)" width')  # 注：这里最后加一个'width'是为了提高匹配精确度
    # 解析出jpg的url列表
    jpgs = re.findall(jpgreg, html)

    return jpgs


# 用图片url下载图片并保存成制定文件名
def downloadJPG(imgUrl, fileName):
    urllib.urlretrieve(imgUrl,fileName)


# 批量下载图片，默认保存到当前目录下
def batchDownloadJPGs(imgUrls, path='./'):
    # 用于给图片命名
    count = 1
    for url in imgUrls:
        downloadJPG(url, ''.join([path, '{0}.jpg'.format(count)]))
        count = count + 1


# 封装：从百度贴吧网页下载图片
def download(url):
    html = getHtmlContent(url)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)


def main():
    # url = "http://www.baidu.com"
    # response1 = urllib2.urlopen(url)
    # print u"第一种方法"
    # #获取状态码，200表示成功
    # print response1.getcode()
    # 获取网页内容的长度
    # print len(response1.read())
    # print response1.read()
    # url = 'http://tieba.baidu.com/p/2256306796'
    # download(url)

    str = "abc123edf"
    patt = r"[0-9]+"
    print re.match(patt, str)



if __name__ == "__main__":
    main()