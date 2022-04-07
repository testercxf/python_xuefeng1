# # 1、导入模块
# from time import  sleep
# from  selenium import  webdriver
# # 2、实例化浏览器对象
# driver = webdriver.Chrome()
# # 3、打开网页
# driver.get("http://101.133.169.100/yuns/index.php/")
# # 4、浏览网页
# sleep(8)
# # 5、关闭网页
# driver.quit()



from selenium import  webdriver
from selenium.webdriver.support.select import Select
from time import sleep
driver = webdriver.Chrome()
driver.get('http://182.92.197.48:8082/index.html#/workbench/index')
driver.maximize_window()
sleep(2)
driver.find_element_by_xpath('//input[@name="username"]').send_keys('13201596609')#输入crm账号
driver.find_element_by_xpath('//input[@name="password"]').send_keys('199606')#输入密码
driver.find_element_by_xpath('//div[@class="el-form-item__content"]/button').click()#点击登录
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/section/header/div/div/div/a[2]/div').click()#点击客户管理
sleep(5)
driver.find_element_by_xpath('//*[@id="app"]/section/section/aside/div/ul/a[8]/li').click()#点击合同
sleep(5)
driver.find_element_by_xpath('//*[@id="crm-main-container"]/div/div/div[1]/div[3]/button/span').click()

sleep(5)
driver.find_element_by_xpath('//div[@class="el-form-item crm-create-item is-required"]/div/span/div[2]/div/div').click()
sleep(5)
driver.find_element_by_xpath("//span[text()='admin']").click()