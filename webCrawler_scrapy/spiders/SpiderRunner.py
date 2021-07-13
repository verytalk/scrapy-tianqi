#coding=utf-8
import scrapy
import re
import os
import urllib
import MySQLdb
import sys
import datetime
import time
import calendar

from scrapy.selector import Selector
from scrapy.http import HtmlResponse,Request

from webCrawler_scrapy.date import getBetweenMonth
from webCrawler_scrapy.items import WebcrawlerScrapyItem

class SpiderRunner(scrapy.spiders.Spider):
    name="webCrawler_scrapy"    #定义爬虫名，要和settings中的BOT_NAME属性对应的值一致

    allowed_domains=["lishi.tianqi.com"] #搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页
    start_urls=["https://lishi.tianqi.com/"]   #开始爬取的地址
    #该函数名不能改变，因为Scrapy源码中默认callback函数的函数名就是parse
    def parse(self, response):
        print "-------------- start spider --------------"
        se = Selector(response) #创建查询对象，HtmlXPathSelector已过时
        #print se.xpath("//html").extract()
       # print response.url
        #print "======----=-=-=-=-=-=-="

        print "response url: ",response.url

        #print re.match("http://lishi.tianqi.com/[\w]+/[\d]+.html", response.url)
        matchURL = re.match(r"http://lishi.tianqi.com/(.*)/(.*).html", response.url)
        print matchURL
        if(matchURL):#如果url能够匹配到需要爬取的url，就爬取
            address_code = matchURL.group(1)
            print "address code is : " , address_code
            print "--------------start analysis--------------"
            src = se.xpath("//div[@class='tian_three']/ul") #匹配到ul下的所有小li
            address = se.xpath("//div[@class='flex']/h3//text()").extract()

            print "address is: ",address
            print "src is: ",src

            print "weather list size : ",range(len(src))

            # print src[1].xpath('li//text()').extract()
            # print src[2].xpath('li//text()').extract()
            srcCount = range(len(src))

            data = src.xpath("li")  # 依次抽取所需要的信息

            dataCount = range(len(data))
            print "--------------start dataCount--------------",dataCount,data

            #print data[0].xpath('div//text()').extract()

            for j in dataCount:
                dateWeater = data[j].xpath('div//text()').extract()
                print dateWeater
                print "=======-------"
                if j >= 0:
                    item=WebcrawlerScrapyItem()  #实例item（具体定义的item类）,将要保存的值放到事先声明的item属性中
                    item['date']=dateWeater[0]
                    item['max_tempe'] = dateWeater[1]
                    item['min_tempe'] = dateWeater[2]
                    item['weather'] = dateWeater[3]
                    item['wind'] = dateWeater[4]
                    item['wind_power']=0
                    item['address']=address
                    item['address_code']=address_code
                    print item
                    yield item  #返回item,这时会自定解析item

                    #urllib.urlretrieve(realUrl,path)  #接收文件路径和需要保存的路径，会自动去文件路径下载并保存到我们指定的本地路径


        all_urls = se.xpath("//a/@href").extract()  # 提取界面所有的url
        for url in all_urls:
            print url
            tianqiURL = re.match(r"(.*)/index.html", url)
            if (tianqiURL):
                tianqiAddress = tianqiURL.group(1)
                #if (tianqiAddress != ""):
                if (tianqiAddress == "beijing"):

                    print tianqiAddress

                    # date = "201911"
                    # print date
                    # print "====-----=-=-=-=-=-=-=-=-=-=-========== ", tianqiAddress, date
                    # yield Request("http://lishi.tianqi.com/" + tianqiAddress + "/" + date + ".html",callback=self.parse)
                    # print "====-----=-=-=-=-=-=-=-=-=-=-========== END ", "http://lishi.tianqi.com/" + tianqiAddress + "/" + date + ".html"
                    date_list = getBetweenMonth("2021-05-01", "2021-05-02")
                    for date in date_list:
                        print date
                        print "====-----=-=-=-=-=-=-=-=-=-=-========== ",tianqiAddress,date
                        yield Request("http://lishi.tianqi.com/"+tianqiAddress+"/"+date+".html",callback = self.parse)
                        print "====-----=-=-=-=-=-=-=-=-=-=-========== END ","http://lishi.tianqi.com/"+tianqiAddress+"/"+date+".html"


        # date_list = getBetweenMonth("2011-01-01", "2019-11-01")
        # tianqiAddress = "aershan"
        # print(date_list);
        # for date in date_list:
        #     print date
        #     print "====-----=-=-=-=-=-=-=-=-=-=-=========="
        #     print "====-----=-=-=-=-=-=-=-=-=-=-=========="
        #     yield Request("http://lishi.tianqi.com/" + tianqiAddress + "/" + date + ".html", callback=self.parse)
