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
        html1 = req.get('http://kdjw.hnust.cn/kdjw/xszqcjglAction.do?method=queryxscj')
        html2 = req.get('http://kdjw.hnust.cn/kdjw/xszqcjglAction.do?method=toXfjdList')
        wd.quit()
        return [html1.text, html2.text]

    def class_select(self, num):
        major = ''
        if num == "1":
            major = "计算机科学与工程"
        elif num == "2":
            major = "网络工程"
        elif num == "3":
            major = "信息安全"
        elif num == "4":
            major = "物联网工程"
        elif num == "5" or num == "6":
            major = "软件工程"
        return major

    def query_spider(self):
        html = self.login()
        selector = etree.HTML(html[0])
        selector2 = etree.HTML(html[1])
        i, j = 1, 1
        data_list = []
        new_data_list = []

        #成绩爬虫
        while True:
            block1 = selector.xpath('//tr[@id="' + str(i) + '"]')
            if len(block1) != 0:
                id = selector.xpath('//tr[@id="' + str(i) + '"]/td[3]/text()')
                stu_id = id[0]
                name = selector.xpath('//tr[@id="' + str(i) + '"]/td[4]/text()')
                term = selector.xpath('//tr[@id="' + str(i) + '"]/td[5]/text()')
                c_name = selector.xpath('//tr[@id="' + str(i) + '"]/td[6]/text()')
                score = selector.xpath('//tr[@id="' + str(i) + '"]/td[7]/text()')
                c_type = selector.xpath('//tr[@id="' + str(i) + '"]/td[9]/text()')
                credit = selector.xpath('//tr[@id="' + str(i) + '"]/td[12]/text()')
                properties = selector.xpath('//tr[@id="' + str(i) + '"]/td[13]/text()')
                grade = stu_id[0:2] + "级"
                major = self.class_select(stu_id[5])
                class_num = stu_id[7] + "班"

                data = {'stu_id': stu_id, 'name': name[0], 'term': term[0],
                           'c_name': c_name[0], 'score': score[0], 'c_type': c_type[0],
                           'credit': credit[0], 'properties': properties[0], 'grade': grade,
                           'major': major, 'class_num': class_num}

                data_list.append(data)
                i += 1
            else:
                break

        #学分绩点爬虫
        while True:
            block2 = selector2.xpath('//tr[@id="' + str(j) + '"]')
            if len(block2) != 0:
                c_name = selector2.xpath('//tr[@id="' + str(j) + '"]/td[3]/text()')
                point = selector2.xpath('//tr[@id="' + str(j) + '"]/td[6]/text()')
                grade_point = selector2.xpath('//tr[@id="' + str(j) + '"]/td[7]/text()')
                for data in data_list:
                    if data['c_name'] == c_name[0] and data['properties'] == u'重修':
                        data['point'] = ""
                        data['grade_point'] = ""
                        new_data_list.append(data)
                    elif data['c_name'] == c_name[0]:
                        data['point'] = point[0]
                        data['grade_point'] = grade_point[0]
                        new_data_list.append(data)
                j += 1
            else:
                break
        return new_data_list


"""
a = spider()
b = a.query_spider()
c = b[0]
print c['c_name'], c['grade_point']
print len(b)
"""