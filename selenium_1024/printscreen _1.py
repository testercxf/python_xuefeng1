# 1、导入模块
from time import  sleep
from  selenium import  webdriver
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/")
# 1、对当前窗体的主体界面进行截图操作，并以*.png格式保存到电脑完整路径下
driver.get_screenshot_as_file("d:/test1.png")
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()