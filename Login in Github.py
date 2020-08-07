#基于scrapy开发的模拟登录Github项目
import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github'
    #allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        token=response.xpath('//input[@name="authenticity_token"]/@value')[0].extract()
        timestamp=response.xpath('//input[@name="timestamp"]/@value')[0].extract()
        timestamp_secret=response.xpath('//input[@name="timestamp_secret"]/@value')[0].extract()
        data={
            'commit': 'Sign in',
            'authenticity_token': token,
            'ga_id': '766730325.1575016852',
            'login': '*****',
            'password': '*****',
            'webauthn - support': 'supported',
            'webauthn - iuvpaa - support': 'supported',
            'return_to':'',
            'required_field_2dc0':'',
            'timestamp': timestamp,
            'timestamp_secret': timestamp_secret
        }
        yield  scrapy.FormRequest(url='https://github.com/session',formdata=data,callback=self.github)

    #查验一下是否有名字就可以知道是否登录成功了
    def github(self,response):
        name=response.xpath('//strong[@class="css-truncate-target"]/text()')[0].extract()
        print(name)
