#1、导入模块
from  time import  sleep
from selenium import  webdriver
#2、实例化浏览器对象
driver = webdriver.Chrome()
#3、打开网页
#需求
# 通过xpath的绝对路径定位元素，进行三次页面跳转
driver.get("http://101.133.169.100/yuns/index.php/")
driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/a/div/span").click()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div/div/div/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/input[2]").click()
#4、浏览网页
sleep(8)
#5、关闭网页
driver.quit()