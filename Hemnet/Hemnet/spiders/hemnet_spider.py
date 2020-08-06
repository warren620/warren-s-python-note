import scrapy
from Hemnet.items import HemnetItem

class HemnetSpiderSpider(scrapy.Spider):
    name = 'Hemnet_spider' #爬虫名称
    allowed_domains = ['hemnet.se'] #允许爬取的域名
    start_urls = ['https://www.hemnet.se/bostader?page=1']
    #起始的页码
    num = 1
    # 每页的url
    url = "https://www.hemnet.se/bostader?page=%d"

    # 回调函数接受item
    def parse_house(self, response):
        item = HemnetItem()
        sale_names=response.xpath('//div[@class="broker-contact-card__inner-content broker-contact-card__inner-content--sidebar"]//strong/text()')[0].extract()
        #print(sale_names)
        sale_names = ''.join(sale_names)
        #sale_names = sale_names.strip('\n')
        item['sale_names'] = sale_names
        yield item

    #self为可自定义名称并非内置函数
    def parse(self, response):
        #xpath解析数据
        li_list=response.xpath('//div[@id="result"]/ul/li[@class="normal-results__hit js-normal-list-item"]')
        for li in li_list:
            url_house=li.xpath('./a/@href')[0].extract()
            yield scrapy.Request(url_house, callback=self.parse_house)

        #用while比if快10倍...鬼知道为什么
        while self.num <= 2:  # num最大为50
            self.num += 1
            url = format(self.url % self.num)
            print(url)

            # 递归爬取数据：callback参数的值为回调函数（将url请求后，得到的相应数据继续进行parse解析），递归调用parse函数
            yield scrapy.Request(url=url, callback=self.parse)


