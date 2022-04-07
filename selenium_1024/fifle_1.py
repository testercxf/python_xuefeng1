# 1、导入模块
from time import  sleep
from  selenium import  webdriver
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("http://www.baidu.com")
driver.maximize_window()
sleep(1)
#定位是input标签，type的属性值file，定位后直接跟文件路径
driver.find_element_by_xpath("//*[@class='soutu-btn']").click()
sleep(1)
driver.find_element_by_class_name("upload-pic").send_keys("D:/test1.png")
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()