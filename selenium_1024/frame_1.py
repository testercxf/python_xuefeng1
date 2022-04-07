# 1、导入模块
from time import  sleep
from  selenium import  webdriver
from selenium.webdriver.common.action_chains import  ActionChains
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/admin/index/index")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("admin")            #用户名
driver.find_element_by_id("password").send_keys("admin")            #密码
driver.find_element_by_name("submit").click()
# 1、点击“商品”菜单
sleep(2)
driver.find_element_by_link_text("会员").click()
# 2、切入第一层iframe框架
sleep(1)
aa = driver.find_element_by_xpath("//*[@class='login_main']/iframe")
driver.switch_to.frame(aa)
sleep(2)
driver.find_element_by_name('username').send_keys("123")      #定位到用户搜素框，并输入123
#鼠标悬浮到用户列表中的“更多”
a = driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[1]/td[1]/div/span/a")
ActionChains(driver).move_to_element(a).perform()
sleep(2)
driver.switch_to.default_content()                            #切回到根目录
# driver.switch_to.parent_frame()                             #切回到父级frame
#返回到“首页”菜单
sleep(1)
driver.find_element_by_link_text("首页").click()
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()