import scrapy
from Tese.items import TeseItem

class PicNetbianComSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/4kmeinv/index.html']

    url="http://pic.netbian.com/4kmeinv/index_%d.html"
    num=1 #起始页码

    def parse(self, response):
        li_list=response.xpath('//div[@class="wrap clearfix"]/div/div[@class="slist"]/ul/li')
        for li in li_list:
            img_url="http://pic.netbian.com"+li.xpath('./a/img/@src')[0].extract()
            item=TeseItem()
            item['img_url']=img_url
            yield item

        if self.num<=161:
            self.num+=1
            url = format(self.url % self.num)
            print(url)

            yield scrapy.Request(url=url, callback=self.parse)

