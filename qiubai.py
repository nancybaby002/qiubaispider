#!/usr/bin/env python
# encoding: UTF-8
import urllib2
import sys
import time
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
reload(sys)
sys.setdefaultencoding("utf-8")
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
headers = {'User-Agent': user_agent}


def get_qiubai(page, file):
    logging.info("开始糗百内容,page="+str(page))
    url = 'http://www.qiushibaike.com/text/page/' + str(page) + '/'
    request = urllib2.Request(url=url, headers=headers)
    try:
        response = urllib2.urlopen(request)
        html = response.read()
    except Exception, e:
        logging.warn(e)
        logging.warn('retry 2 ...')
        time.sleep(3)
        try:
            response = urllib2.urlopen(request)
            html = response.read()
        except Exception, e:
            logging.warn(e)
            logging.warn('retry 3 ...')
            time.sleep(3)
            try:
                response = urllib2.urlopen(request)
                html = response.read()
            except Exception, e:
                logging.warn(e)
                return
    soup = BeautifulSoup(html)
    content = soup.find(id="content-left")
    articles = content.find_all(class_="article")
    for article in articles:
        text = article.find(class_="content").getText()
        file.write(str(text) + "\n")


def getqiubai_txt(page):
    page = page + 1
    File = open("qiubai.txt", "w")
    for a in range(1, page):
        get_qiubai(a, File)
    File.close()


if __name__ == '__main__':
    getqiubai_txt(35)
