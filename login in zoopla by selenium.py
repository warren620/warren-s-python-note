#selenium练手项目第二章.模拟登录英国房产网站并搜索伦敦所有房产.未做持久化存储
#吐槽：以前辛辛苦苦拿cookie做模拟登录...选择用selenium轻轻松松就进去了...这么好的东西为啥我选择才学

from selenium import webdriver
# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get('https://www.zoopla.co.uk/signin/?page_after_login=%2F')

driver.find_element_by_xpath('//button[@class="ui-button-primary ui-cookie-accept-all-medium-large"]').click()
driver.find_element_by_id('signin_email').send_keys('*******')#username
driver.find_element_by_id('signin_password').send_keys('*****')#password
driver.find_element_by_id('signin_submit').click()

driver.find_element_by_xpath('//input[@class="search-input geo_autocomplete"]').send_keys('London')#搜索某地的房产.未指定价格等参数
driver.find_element_by_id('search-submit').click()
