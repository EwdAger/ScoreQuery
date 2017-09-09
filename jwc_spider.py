# -*- coding: utf-8 -*-
from selenium import webdriver
import requests
from PIL import Image
from lxml import etree

class spider(object):

    def split_captcha(self):
        im = Image.open('captcha.png')
        im = im.crop((215, 321, 295, 360))
        im.save('captcha.png')
        im.show()

    def login(self):
        Path = r'D:\project\ScoreQuery\ScoreQuery\phantomjs-2.1.1-windows\bin\phantomjs.exe'
        wd = webdriver.PhantomJS(executable_path=Path)
        loginUrl = 'http://kdjw.hnust.cn/kdjw/'
        wd.get(loginUrl)
        wd.save_screenshot('captcha.png')
        self.split_captcha()
        wd.find_element_by_xpath('//*[@id="userAccount"]').send_keys('1505020114')
        wd.find_element_by_xpath('//*[@id="userPassword"]').send_keys('140216')
        wd.find_element_by_xpath('//*[@id="RANDOMCODE"]').send_keys(raw_input("输入验证码： "))
        wd.find_element_by_xpath('//*[@id="imgbtn"]').click() #点击登陆

        req = requests.Session()
        cookies = wd.get_cookies()
        for cookie in cookies:
            req.cookies.set(cookie['name'], cookie['value'])
        html = req.get('http://kdjw.hnust.cn/kdjw/xszqcjglAction.do?method=queryxscj')
        wd.quit()
        return html.text

    def query_spider(self):
        html = self.login()
        print type(html)
        selector = etree.HTML(html)
        stu_id = selector.xpath('//tr[@id="1"]/td[3]/text()')
        print stu_id

a = spider()
a.query_spider()

