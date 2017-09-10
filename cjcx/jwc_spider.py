# -*- coding: utf-8 -*-
from selenium import webdriver
import requests
from PIL import Image
from lxml import etree

class spider(object):

    def split_captcha(self):
        im = Image.open('cjcx/yzm/captcha.png')
        im = im.crop((215, 321, 295, 360))
        im.save('cjcx/yzm/captcha.png')
        im.show()

    def login(self):
        Path = r'D:\project\ScoreQuery\ScoreQuery\phantomjs-2.1.1-windows\bin\phantomjs.exe'
        wd = webdriver.PhantomJS(executable_path=Path)
        loginUrl = 'http://kdjw.hnust.cn/kdjw/'
        wd.get(loginUrl)
        wd.save_screenshot('cjcx/yzm/captcha.png')
        self.split_captcha()
        wd.find_element_by_xpath('//*[@id="userAccount"]').send_keys('1505020114')
        wd.find_element_by_xpath('//*[@id="userPassword"]').send_keys('140216')
        wd.find_element_by_xpath('//*[@id="RANDOMCODE"]').send_keys(raw_input("输入验证码："))
        wd.find_element_by_xpath('//*[@id="imgbtn"]').click() #点击登陆

        req = requests.Session()
        cookies = wd.get_cookies()
        for cookie in cookies:
            req.cookies.set(cookie['name'], cookie['value'])
        html = req.get('http://kdjw.hnust.cn/kdjw/xszqcjglAction.do?method=queryxscj')
        wd.quit()
        return html.text

    def class_select(self, stu_id):
        major = ''
        if stu_id == "1":
            major = "计算机科学与工程"
        elif stu_id == "2":
            major = "网络工程"
        elif stu_id == "3":
            major = "信息安全"
        elif stu_id == "4":
            major = "物联网工程"
        elif stu_id == "5" or stu_id == "6":
            major = "软件工程"
        return major

    def query_spider(self):
        html = self.login()
        selector = etree.HTML(html)
        i = 1
        data_list = []
        while True:
            block = selector.xpath('//tr[@id="' + str(i) + '"]')
            if len(block) != 0:
                stu_id = str(selector.xpath('//tr[@id="' + str(i) + '"]/td[3]/text()'))
                name = selector.xpath('//tr[@id="' + str(i) + '"]/td[4]/text()')
                term = selector.xpath('//tr[@id="' + str(i) + '"]/td[5]/text()')
                c_name = selector.xpath('//tr[@id="' + str(i) + '"]/td[6]/text()')
                score = selector.xpath('//tr[@id="' + str(i) + '"]/td[7]/text()')
                c_type = selector.xpath('//tr[@id="' + str(i) + '"]/td[9]/text()')
                credit = selector.xpath('//tr[@id="' + str(i) + '"]/td[12]/text()')
                properties = selector.xpath('//tr[@id="' + str(i) + '"]/td[13]/text()')
                grade = stu_id[0:2] + "级"
                major = self.class_select(stu_id[5:6])
                class_num = stu_id[7:8] + "班"
                data = {'stu_id': stu_id, 'name': name, 'term': term,
                           'c_name': c_name, 'score': score, 'c_type': c_type,
                           'credit': credit, 'properties': properties, 'grade': grade,
                           'major': major, 'class_num': class_num}

                data_list.append(data)
                i += 1
            else:
                return data_list

a = spider()
b = a.query_spider()
c = b[0]
print c['major']
print len(c)
