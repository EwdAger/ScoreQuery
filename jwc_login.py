# -*- coding: utf-8 -*-
import requests
import urllib2
import urllib
import cookielib

cj = cookielib.CookieJar()
opener = urllib2.build_opener((urllib2.HTTPCookieProcessor(cj)))
opener.add_handler = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')]

def login():
    username = '1505020114'
    pw = '*'


    cap_url = r'http://kdjw.hnust.cn/kdjw/verifycode.servlet'
    cap_content = urllib2.urlopen(cap_url).read()
    cap_file = open('./yzm/cap.gif', 'wb')
    cap_file.write(cap_content)
    cap_file.close()
    captcha = raw_input('capture: ')


    url = r'http://kdjw.hnust.cn/kdjw/xscjcx_check.jsp'
    datas = {
        'useDogCode': '',
        'dlfl': '0',
        'USERNAME': username,
        'PASSWORD': pw,
        'RANDOMCODE': captcha,
    }
    data = urllib.urlencode(datas)
    urllib2.urlopen(url, data).read()

    search_url = 'http://kdjw.hnust.cn/kdjw/xszqcjglAction.do?method=queryxscj'
    print urllib2.urlopen(search_url).read()
if __name__=="__main__":
    login()


