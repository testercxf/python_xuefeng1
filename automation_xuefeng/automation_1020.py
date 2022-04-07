#1、导入模块
from  time  import  sleep
from selenium import  webdriver
#2、实例化浏览器对象：类名()
driver = webdriver.Chrome()
#3、打开网页：必须包含协议头
driver.get("http://www.baidu.com")
#4、观察效果
sleep(8)
#5、关闭页面
driver.quit()