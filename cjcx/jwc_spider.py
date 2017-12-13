# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from captcha_verify import verify

class spider(object):

    def login(self, username, password):
        login_url = 'http://kdjw.hnust.cn/kdjw/Logon.do?method=logon'
        check = "<script language=\"javascript\">window.location.href='http://kdjw.hnust.cn/kdjw/framework/main.jsp';</script>"
        i = 0
        msg = ''
        while (True):
            if i == 10:
                msg = "学号密码错误或连接教务网失败"
                break
            cookies = requests.get('http://kdjw.hnust.cn/kdjw/verifycode.servlet').cookies
            img = requests.get('http://kdjw.hnust.cn/kdjw/verifycode.servlet', cookies=cookies).content
            with open('cjcx/yzm/captcha.bmp', 'wb') as f:
                f.write(img)
            code = verify("cjcx/yzm/captcha.bmp")
            data = {
                'USERNAME': username,
                'PASSWORD': password,
                'RANDOMCODE': code
            }
            login = requests.post(login_url, cookies=cookies, data=data)
            soup = BeautifulSoup(login.content, "lxml")
            if str(soup.script) == check:
                break
            i += 1

        return cookies, msg

    def score_spider(self, username, password):
        cookies, msg = self.login(username, password)
        if msg == '':
            html = requests.get('http://kdjw.hnust.cn/kdjw/xszqcjglAction.do?method=queryxscj', cookies=cookies)
            with open('cjcx/page/data.html', 'w') as f:
                f.write(html.content)
        return msg


    def score_data(self):
        soup = BeautifulSoup(open("cjcx/page/data.html"), "lxml")
        keys = []
        data = []
        year = []

        cj_soup = soup.find("tr", class_="smartTr")
        while(True):
            if cj_soup == None:
                break
            for i in range(4, 7):
                key = cj_soup.contents[i].text.strip()
                if i == 6 and key == '':
                    key = '无成绩'
                keys.append(key)
            keys.append(cj_soup.contents[11].text.strip())
            if not keys[0] in year:
                y = keys[0]
                year.append(y)
            data.append(keys)
            keys = []
            cj_soup = cj_soup.next_sibling

        return data, year


"""
a = spider()
data = a.score_bs()

for i in data:
    for j in range(4):
        print(i[j])
"""