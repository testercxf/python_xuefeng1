# 1、导入模块
from time import  sleep
from  selenium import  webdriver
from selenium.webdriver.support.select import  Select
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index")
sleep(6)                            #网页加载相应时间
driver.maximize_window()
#获取标签中的文本信息
select_1 = driver.find_element_by_id("J_roomCountList")
Select(select_1).select_by_visible_text("3间")
#获取value值
sleep(3)
Select(select_1).select_by_value("2")
#按索引方式取下标
sleep(3)
Select(select_1).select_by_index(3)
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()