# 1、导入模块
from time import  sleep
from  selenium import  webdriver
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/")
driver.maximize_window()
# 需求
# 1、点击网页前进按钮
driver.refresh()
# 2、点击网页刷新按钮
driver.forward()
# 3、点击网页返回按钮
driver.back()
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()