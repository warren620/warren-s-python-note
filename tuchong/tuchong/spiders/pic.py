#第一个基于scrapy框架开发的selenium模拟登录爬取图片的项目
import scrapy
from selenium import webdriver
from lxml import etree
from tuchong.items import TuchongItem

class PicSpider(scrapy.Spider):
    name = 'pic'
    #allowed_domains = ['stock.tuchong.com']
    start_urls = ['https://stock.tuchong.com/accounts/login']


    def __init__(self):
        #实例化一个浏览器对象(实例化一次)
        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

    #必须在整个爬虫结束后，关闭浏览器
    def closed(self,spider):
        print('爬虫结束')
        self.driver.quit()


    def parse(self, response):
        tree=etree.HTML(response.text)
        a_list=tree.xpath('//div[@class="images-gallery"]/a')
        for a in a_list:
            img_url='https:'+a.xpath('./img/@data-src')[0]
            print(img_url)
            item = TuchongItem()
            item['url']=img_url
            yield item


