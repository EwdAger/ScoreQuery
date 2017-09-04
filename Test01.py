# -*- coding: utf-8 -*-
from selenium import webdriver
import requests
chromePath = r'D:\project\ScoreQuery\ScoreQuery\chromedriver.exe'
wd = webdriver.Chrome(executable_path=chromePath)
loginUrl = 'http://kdjw.hnust.cn/kdjw/'
wd.get(loginUrl)
wd.find_element_by_xpath('//*[@id="userAccount"]').send_keys('1505020114')
wd.find_element_by_xpath('//*[@id="userPassword"]').send_keys('140216')
wd.find_element_by_xpath('//*[@id="RANDOMCODE"]').send_keys(raw_input("输入验证码： "))
wd.find_element_by_xpath('//*[@id="imgbtn"]').click() #点击登陆
req = requests.Session()

cookies = wd.get_cookies()
for cookie in cookies:
    req.cookies.set(cookie['name'], cookie['value'])
test = req.get('http://kdjw.hnust.cn/kdjw/xszqcjglAction.do?method=queryxscj')
print test.text
