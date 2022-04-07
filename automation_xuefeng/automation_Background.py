#1、导入模块
from time import  sleep
from selenium import  webdriver
#2、实例化浏览器对象
driver = webdriver.Chrome()
#3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/admin/index/index")
#需求
#1、点击用户名输入框，输入：admin。再点击密码输入框，输入：admin
#点击登录
driver.find_element_by_id("username").send_keys("admin")            #用户名
driver.find_element_by_id("password").send_keys("admin")            #密码
driver.find_element_by_name("submit").click()                       #登录按钮
#4、浏览网页
sleep(8)
#5、关闭网页
driver.quit()