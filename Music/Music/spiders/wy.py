import scrapy
import requests
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from time import sleep

class WySpider(scrapy.Spider):
    name = 'wymusic'
    #allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
        }
        # 创建driver对象并修改window.navigator.webdriver值
        option = ChromeOptions()
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
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
        driver.get('https://music.163.com/')
        sleep(3)
        #将窗口放到最大
        driver.maximize_window()
        sleep(2)
        #进行登录操作
        driver.find_element_by_xpath('//a[@data-action="login"]').click()
        sleep(1)
        driver.find_element_by_xpath('//a[@class="u-btn2 other"]').click()
        sleep(1)
        driver.find_element_by_id('j-official-terms').click()
        sleep(1)
        driver.find_element_by_xpath('//a[@class="u-btn2 u-btn2-2"]').click()
        sleep(1)
        user_name=input("请输入网易云登陆账户的手机号")
        driver.find_element_by_xpath('//input[@class="j-phone txt u-txt"]').send_keys(user_name)
        sleep(1)
        password=input('请输入网易云登录账户的密码')
        driver.find_element_by_xpath('//input[@class="j-pwd u-txt"]').send_keys(password)
        sleep(1)
        driver.find_element_by_xpath('//a[@class="j-primary u-btn2 u-btn2-2"]').click()
        sleep(3)
        driver.find_element_by_xpath('//a[@data-module="my"]').click()
        sleep(1)
        #切换到iframe窗口
        driver.switch_to.frame('g_iframe')
        sleep(1)
        #找到所有存放id的标签
        id_list=driver.find_elements_by_xpath('//div[@class="hd "]/span[1]')#[0].get_attribute('data-res-id')
        lens=(len(id_list))
        #从指定长度的list里提取指定位置的标签进行get_attribute提取所需的内容
        for i in range(0,lens+1):
            id=driver.find_elements_by_xpath('//div[@class="hd "]/span[1]')[i].get_attribute('data-res-id')
            title=driver.find_elements_by_xpath('//span[@class="txt"]/a/b')[i].get_attribute('title')
            #进程
            print(title+'\t'+'正在下载'+'\n')
            #路径
            path=title+'.mp3'
            #封装
            url='http://music.163.com/song/media/outer/url?id='+id+'.mp3'
            #二进制
            content=requests.get(url=url,headers=headers).content
            with open(path,'wb')as fp:
                fp.write(content)