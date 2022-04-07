#1、导入模块
from time  import  sleep
from selenium import  webdriver
#2、实例化浏览器对象:类名()
driver = webdriver.Chrome()
#3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/member/register")
#需求
#1、进入云商系统前台注册界面
#2、定位手机号输入框，输入：17628231114。定位密码输入框，输入：123456。定位确认密码输入框，输入：123456
# 定位验证码输入框，输入admi、定位短信验证码输入框，输入123456
driver.find_element_by_name("username").send_keys("17628231114")        #手机号
driver.find_element_by_name("password").send_keys(123456)               #密码
driver.find_element_by_name("repasswd").send_keys(123456)               #确认密码
driver.find_element_by_id("vcode").send_keys("admi")                    #图形验证码
driver.find_element_by_id("smscode").send_keys(123456)                  #手机验证码
#4、浏览网页
sleep(8)
#5、关闭网页
driver.quit()

