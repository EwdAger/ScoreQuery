# -*- coding: utf-8 -*-
import scrapy
from scrapy.conf import settings #从settings文件中导入Cookie，这里也可以室友from scrapy.conf import settings.COOKIE

class DoubanSpider(scrapy.Spider):
    name = "douban"
    #allowed_domains = ["csdn.com"]
    start_urls = ["http://kdjw.hnust.cn/kdjw/Logon.do?method=logon"]
    cookie = 'JSESSIONID=5126B2EFF2F6C3528127B91B67D9E392'  # 带着Cookie向网页发请求\
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], headers=self.headers, cookies=self.cookie)# 这里带着cookie发出请求
    def parse(self, response):
        print response.body