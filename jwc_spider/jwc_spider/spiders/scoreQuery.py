# -*- coding: utf-8 -*-
import scrapy
import urllib
from scrapy.http import Request, FormRequest

class scoreQuerySpider(scrapy.Spider):
    name = "scoreQuery"
    #allowed_domains = ["http://kdjw.hnust.cn/"]
    header = {"user-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5"}
    def start_requests(self):
        return [Request("http://kdjw.hnust.cn/kdjw/", meta={"cookiejar": 1}, callback=self.parse)]

    def parse(self, response):
        #captcha = response.xpath('//span[@id="SafeCodeImg"]/img/@src').extract()
        captcha = "http://kdjw.hnust.cn/kdjw/verifycode.servlet"
        if len(captcha) > 0:
            print "此时有验证码 "
            localpath = "D:/project/ScoreQuery/yzm/1.png"
            urllib.urlretrieve(captcha, filename=localpath)
            print "请输入验证码： "
            captcha_value = raw_input()
            data={
                "useDogCode": "",
                "dlfl": "0",
                "USERNAME": "1505020114",
                "PASSWORD": "140216",
                "RANDOMCODE": captcha_value,
                "redir": "http://kdjw.hnust.cn/kdjw/xszqcjglAction.do?method=queryxscj"
            }
        else:
            print "此时没有验证码"
            data = {
                "useDogCode": "",
                "dlfl": "0",
                "USERNAME": "1505020114",
                "PASSWORD": "140216",
                "redir": "http://kdjw.hnust.cn/kdjw/xszqcjglAction.do?method=queryxscj"
            }
        print "登录中..."
        return [FormRequest.from_response(response, meta={"cookiejar": response.meta["cookiejar"]},
                                          headers=self.header, formdata=data, callback=self.next)]

    def next(self, response):
        print "正在爬取成绩信息"
        infos = response.xpath('//div[@id="mxhDiv"]/table/tbody/tr/td').extract()
        fullInfo = ''
        for info in infos:
            print info