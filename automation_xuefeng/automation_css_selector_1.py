# 1、导入模块
from time import  sleep
from  selenium import  webdriver
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/")
driver.maximize_window()                                                           #窗口最大化
#检测后面的每一条定位能否在7秒内加载出来，如果提前加载出来就继续执行
driver.implicitly_wait(7)
driver.find_element_by_css_selector("html>body>div>div>div>div>form>input.but1").send_keys("123")    #css的绝对路径。定位输入框
driver.find_element_by_css_selector(".but2").click()                                                 #class属性专有，定位搜索按钮并点击
driver.find_element_by_css_selector("#cart_num").click()
driver.back()                                                                      #点击浏览器的返回
driver.find_element_by_css_selector("[title='女装']").click()
driver.find_element_by_css_selector(".schhot>a:nth-child(2)").click()
driver.find_element_by_css_selector(".schhot>a:nth-child(3)").click()
driver.find_element_by_css_selector(".schhot>a:nth-child(4)").click()
driver.find_element_by_css_selector("[title='全场一员'][class='ch']").click()
driver.find_element_by_css_selector(".schhot>a:nth-child(6)").click()
driver.find_element_by_css_selector(".schhot>a:nth-child(7)").click()
driver.find_element_by_css_selector(".schhot>a:nth-child(8)").click()
driver.find_element_by_css_selector(".pp>dd>a:first-child").click()               #第一个
driver.find_element_by_css_selector(".pp>dd>a:nth-child(3)").click()
driver.find_element_by_css_selector(".pp>dd>a:nth-child(4)").click()
driver.find_element_by_css_selector(".pp>dd>a:last-child").click()                #倒数第一个
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()