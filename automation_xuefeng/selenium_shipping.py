#1、导入模块
from time import  sleep
from  selenium import  webdriver
from selenium.webdriver import ActionChains
#2、实例化浏览器对象
driver = webdriver.Chrome()
#3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/address")
driver.find_element_by_id("text").send_keys("17628231234")                #用户名
driver.find_element_by_id("password").send_keys(123456)                   #密码
# driver.find_element_by_id("password").clear()                           #清空密码
driver.find_element_by_name("submit").click()                             #登录按钮
sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/div[2]/p/a[1]").click()   #会员中心
driver.find_element_by_link_text("收货地址").click()                                        #收货地址
driver.find_element_by_id("add_address").click()                                            #新增收货地址
sleep(1)
driver.find_element_by_id("recive_name").send_keys("张三")                    #姓名
driver.find_element_by_id("recive_mobile").send_keys("17823212221")           #手机号
m_drop_down = driver.find_element_by_class_name("area_name")                  #定位下拉选择框
ActionChains(driver).move_to_element(m_drop_down).perform()                   #鼠标悬浮
# sleep(1)
#选择省
driver.find_element_by_xpath("/html/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/div/div/div/div[1]/a[23]").click()
#选择该省下的市
driver.find_element_by_xpath("/html/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/div/div/div/div[2]/a[1]").click()
#选择该市下的区
driver.find_element_by_xpath("/html/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/div/div/div/div[3]/a[2]").click()
driver.find_element_by_id("recive_address").send_keys("四川省成都市")         #收货地址
driver.find_element_by_id("recive_zip").send_keys(638422)                     #邮编
driver.find_element_by_id("recive_is_default").click()                        #默认单选
sleep(2)
driver.find_element_by_xpath("/html/div[2]/div/div[1]/em").click()            #关闭地址输入框页面
sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul/a[2]").click()  #退出登录
#4、浏览网页
sleep(8)
#5、关闭网页
driver.quit()

