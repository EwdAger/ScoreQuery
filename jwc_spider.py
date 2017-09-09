# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
import urllib
from PIL import Image

Path = r'D:\project\ScoreQuery\ScoreQuery\phantomjs-2.1.1-windows\bin\phantomjs.exe'
wd = webdriver.PhantomJS(executable_path=Path)
loginUrl = 'http://kdjw.hnust.cn/kdjw/'
wd.get(loginUrl)

wd.save_screenshot('screenshot.png')

im = Image.open('screenshot.png')
im = im.crop((215, 321, 295, 360))
im.save('screenshot.png')
im.show()

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

wd.quit()
