# 1、导入模块
from time import  sleep
from  selenium import  webdriver
from selenium.webdriver.common.action_chains import  ActionChains
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("https://passport.ctrip.com/user/login?BackUrl=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155952%26allianceid%3D4897%26ouid%3Dindex#ctm_ref=c_ph_login_buttom")
# 需求
# 1、鼠标悬浮
sleep(3)
ele = driver.find_element_by_xpath("//*[@id='logintitle']/a")
ActionChains(driver).move_to_element(ele).perform()
# 2、模拟用户右击页面
ele = driver.find_element_by_id("lg_loginbox")
ActionChains(driver).context_click(ele).perform()
# 3、模拟用户双击控件
ele = driver.find_element_by_id("npwd")
ActionChains(driver).double_click(ele).perform()
# 4、拖动控件
# 通过定位开始位置和结束位置进行拖拽
# a = driver.find_element_by_xpath("//*[@id='slideCode']/div[1]/div[2]")                           #定位控件开始位置
# b = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/input[1]")            #定位控件结束位置
# ActionChains(driver).drag_and_drop(a,b).perform()
# 定义开始位置的控件，调整像素点，拖拽到指定位置
sleep(3)
a = driver.find_element_by_xpath("//*[@id='sliderddnormal']/div[1]/div[3]")
ActionChains(driver).drag_and_drop_by_offset(a,260,0).perform()
# 5、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()