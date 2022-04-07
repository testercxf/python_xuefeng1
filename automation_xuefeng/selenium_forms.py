# 1、导入模块
from time import  sleep
from  selenium import  webdriver
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/")
# 需求
# 1、最大化窗口
driver.maximize_window()
# 2、指定浏览器窗口大小
sleep(1)
driver.set_window_size(900,800)    #900:宽   800:高
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()