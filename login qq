#首次尝试用基于selenium模块开发的模拟登录QQ空间并获取所有说说点赞的url再进行访问

from selenium import webdriver
import time
# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# 用get打开百度页面
driver.get("https://qzone.qq.com/")

#将当前定位的主体切换了frame 里
driver.switch_to.frame('login_frame')
driver.find_element_by_id('switcher_plogin').click()

driver.find_element_by_id('u').send_keys('**********')#uesr_name
driver.find_element_by_id('p').send_keys('*****')#password
driver.find_element_by_id('login_button').click()

#等待2s进入空间后执行下拉到底操作获得动态加载数据
time.sleep(3)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

'''
page_text=driver.page_source
tree=etree.HTML(page_text)
li_list=tree.xpath('//ul[@id="feed_friend_list"]/li//div[@class="user-list"]/a')
for li in li_list:
    url=li.xpath('.//@href')[0]
    name=li.xpath('.//text()')[0]
    #print(url+'\t'+name)
'''

elements=driver.find_elements_by_xpath('//a[@class="item q_namecard"]')
print(elements)
for t in elements:
    print(t)
    #driver.execute_script("arguments[0].click();",t)
