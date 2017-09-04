# -*- coding: utf-8 -*-
import scrapy
import urllib
from scrapy.http import Request, FormRequest
from urlparse import urljoin

class scoreQuerySpider(scrapy.Spider):
    name = "scoreQuery"
    #allowed_domains = ["http://kdjw.hnust.cn/"]
    header = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.8",
                "Connection": "keep-alive",
                "Host": "kdjw.hnust.cn",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
    }
    def start_requests(self):
        return [Request("http://kdjw.hnust.cn/kdjw/Logon.do?method=logon", meta={"cookiejar": 1}, callback=self.parse)]

    def parse(self, response):
        captcha = response.xpath('//span[@id="SafeCodeImg"]/img/@src').extract()[0]
        #captcha = "http://kdjw.hnust.cn/kdjw/verifycode.servlet"
        print "此时有验证码 "
        localpath = "D:/project/ScoreQuery/yzm/1.png"
        urllib.urlretrieve(urljoin(response.url, captcha), filename=localpath)
        print "请输入验证码： "
        captcha_value = raw_input()
        data = {
                "useDogCode": "",
                "dlfl": "0",
                "USERNAME": "1505020114",
                "PASSWORD": "140216",
                "RANDOMCODE": captcha_value,
                "x": "0",
                "y": "0"
        }
        print "登录中..."
        return [FormRequest.from_response(response, meta={"cookiejar": response.meta["cookiejar"]},
                                          headers=self.header, formdata=data, callback=self.Next)]

    def Next(self, response):
        print "正在爬取成绩信息"
        #errorInfo = response.xpath('//span[@id="errorinfo"]/text()').extract()
        #print errorInfo

        return [Request("http://kdjw.hnust.cn/kdjw/xszqcjglAction.do?method=queryxscj", meta={"cookiejar": response.meta["cookiejar"]}, callback=self.fun)]

    def fun(self, response):
        print response.body
        """infos = response.xpath('//div[@id="mxhDiv"]/table/tbody/tr/td').extract()
        fullInfo = ''
        for info in infos:
            print info"""