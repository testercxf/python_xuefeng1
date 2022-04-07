# 1、导入模块
from time import  sleep
from  selenium import  webdriver
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/")
# 需求
# 1、获取网页的标题
title_1 = driver.title
print(title_1)
# 2、获取网页的网址
url = driver.current_url
print(url)
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()