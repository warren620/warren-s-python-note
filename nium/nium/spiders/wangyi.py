# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from lxml import etree

class WangyiSpider(scrapy.Spider):
    name = 'pic'
    #allowed_domains = ['www.xxxx.com']
    start_urls = ['https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%93%88%E5%88%A9%E6%B3%A2%E7%89%B9']

    def __init__(self):
        #实例化一个浏览器对象(实例化一次)
        self.drive = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

    #必须在整个爬虫结束后，关闭浏览器
    def closed(self,spider):
        print('爬虫结束')
        self.drive.quit()

    def parse(self, response):
        tree=etree.HTML(response.text)
        li_list=tree.xpath('//div[@id="imgid"]/div/ul/li')
        print(li_list)
        for li in li_list:
            img_url=li.xpath('./div/a/img/@data-imgurl')[0]
            print(img_url)



