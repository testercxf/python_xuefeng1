#1、导入模块
from time import  sleep
from selenium import  webdriver
#2、实例化浏览器对象
driver = webdriver.Chrome()
#3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/buy/index")
# 需求
# 通过class_name方式定位到元素模拟用户点击，修改
driver.find_element_by_id("text").send_keys("17628231234")                #用户名
driver.find_element_by_id("password").send_keys(123456)                   #密码
driver.find_element_by_name("submit").click()
sleep(1)                                                                  #防止页面跳转响应时间过长，程序报错
driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/div[2]/p/a[1]").click()  #会员中心
sleep(0.5)
driver.find_element_by_link_text("我的购物车").click()                    #点击我的购物车
driver.find_element_by_class_name("ckbox_cartid").click()                 #取消商品的选择
driver.find_element_by_class_name("cart_minus").click()                   #数量减一
driver.find_element_by_class_name("num").send_keys(1)                     #数量输入框
driver.find_element_by_class_name("cart_plus").click()                    #数量加一
driver.find_element_by_class_name("gopay").click()                        #结算按钮
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()