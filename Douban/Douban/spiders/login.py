#模拟登录豆瓣.这个项目主要难点是iframe
#吐槽：同样的办法Github和豆瓣都能成功携带cookie进行请求.淘宝就不行.这也是个练手项目，为了对比跟淘宝模拟登录的区别在哪
import scrapy
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from time import sleep

class LoginSpider(scrapy.Spider):
    name = 'login'
    #allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def parse(self, response):
        #创建driver对象并修改window.navigator.webdriver值
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option('useAutomationExtension', False)
        driver = Chrome(options=option,executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })
        driver.get('https://www.douban.com/')
        sleep(3)
        driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@frameborder="0"]'))
        sleep(3)
        driver.find_element_by_xpath('//li[@class="account-tab-account"]').click()
        sleep(1)
        driver.find_element_by_id('username').send_keys('*****')
        sleep(1)
        driver.find_element_by_id('password').send_keys('*****')
        sleep(1)
        driver.find_element_by_xpath('//div[@class="account-form-field-submit "]/a').click()
        sleep(10)

        # 获得cookie
        cookie = driver.get_cookies()
        # print(cookie)
        # 取出指定cookie值
        cookie_dic = dict()
        for cookies in cookie:
            cookie_dic[cookies['name']] = cookies['value']
        print(cookie_dic)
        yield scrapy.Request(url='https://movie.douban.com/',cookies=cookie_dic,callback=self.cookie)


    def cookie(self,response):
        print(response.text)
