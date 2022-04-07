#1、导入模块
from time  import  sleep
from selenium import  webdriver
#2、实例化浏览器对象:类名()
driver = webdriver.Chrome()
#3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/member/login?returnUrl=http%3A%2F%2F101.133.169.100%2Fyuns%2Findex.php")
driver.maximize_window()
sleep(2)
#需求
#1、进入云商系统前台登录界面
#2、通过id定位到用户名，输入：admin。定位到密码输入框，输入admin。定位到登录按钮并点击
driver.find_element_by_id("text").send_keys("17628231234")           #用户名
driver.find_element_by_id("password").send_keys("123456")            #密码
driver.find_element_by_name("submit").click()                        #登录按钮
#4、浏览网页
sleep(8)
#5、关闭网页
driver.quit()

