import scrapy
from selenium import webdriver
from time import sleep

class CookieGithubSpider(scrapy.Spider):
    name = 'cookie_github'
    #allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self,response):
        driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        driver.get('https://github.com/login')
        sleep(3)
        driver.find_element_by_id('login_field').send_keys('*****')
        sleep(1)
        driver.find_element_by_id('password').send_keys('*****')
        sleep(1)
        driver.find_element_by_xpath('//input[@class="btn btn-primary btn-block"]').click()
        cookie = driver.get_cookies()
        #print(cookie)
        cookie_dic=dict()
        for cookies in cookie:
            cookie_dic[cookies['name']]=cookies['value']
        #print(cookie_dic)
        yield scrapy.Request(url='https://github.com/warren620/warren-s-python-note',cookies=cookie_dic,callback=self.login)

    def login(self,response):
        print(response.url)
        print(response.text)

