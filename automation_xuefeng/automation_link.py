#1、导入模块
from time import  sleep
from selenium import  webdriver
#2、实例化浏览器对象
driver = webdriver.Chrome()
#3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/admin/index/index")
#需求
# 通过link_text和partial_link_text方式进行元素定位
driver.find_element_by_id("username").send_keys("admin")            #用户名
driver.find_element_by_id("password").send_keys("admin")            #密码
driver.find_element_by_name("submit").click()                       #登录按钮
sleep(1)                                                            #防止页面跳转响应时间过长，程序报错
driver.find_element_by_link_text("订单").click()
driver.find_element_by_link_text("商品").click()
driver.find_element_by_link_text("营销").click()
driver.find_element_by_partial_link_text("员").click()
driver.find_element_by_partial_link_text("站").click()
driver.find_element_by_partial_link_text("置").click()
#4、浏览网页
sleep(5)
#5、关闭网页
driver.quit()