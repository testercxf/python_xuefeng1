# 1、导入模块
from time import  sleep
from  selenium import  webdriver
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/member/login?returnUrl=http%3A%2F%2F101.133.169.100%2Fyuns%2Findex.php%2F")
# 需求
# 1、模拟用户点击控件
driver.find_element_by_class_name("submit_login").click()
# 2、模拟用户再输入框输入数据
driver.find_element_by_id("text").send_keys("yonghu")
# 3、模拟用户清空输入框数据
driver.find_element_by_id("text").clear()
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()