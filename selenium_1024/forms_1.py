# 1、导入模块
from time import  sleep
from  selenium import  webdriver
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/news/help/id/4")

# 1、在商品搜索框输入“123”并打印当前窗体信息
driver.find_element_by_class_name("but1").send_keys("123")
sleep(2)
print(driver.window_handles)        #打印当前页面信息
driver.maximize_window()            #最大化窗口
sleep(2)
driver.find_element_by_link_text("秒杀").click()             #点击“秒杀”超链接
sleep(2)
print(driver.window_handles)                                 #打印当前页面窗体信息
driver.switch_to.window(driver.window_handles[1])            #切换句柄到新页面
driver.find_element_by_link_text("即将开始").click()         #点击"即将开始"超链接
sleep(2)
driver.close()                                               #关闭当前窗体
sleep(2)
print(driver.window_handles)                                 #再次打印句柄所在窗体信息
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()