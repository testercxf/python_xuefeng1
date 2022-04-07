# 1、导入模块
from time import sleep
from selenium  import  webdriver
from selenium.webdriver.support.ui  import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions  as  ec
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/")
driver.maximize_window()                                         #最大化窗口
# 1、强制等待时间
sleep(2)                                                         #等待5秒后才会继续往下执行
# 2、隐式等待时间
driver.implicitly_wait(2)                                        #后面的控件定位全部等待5秒
driver.find_element_by_css_selector(".con  p a:nth-child(1)")
sleep(2)                                                         #打破隐式等待的规则
driver.find_element_by_xpath("//*[@class='but1']").send_keys("123")
# 3、显示等待时间
#点击“我的购物车”
driver.find_element_by_xpath("//*[@class='small_cart_name']/span").click()
# 在五秒内每隔0.5秒去检测跳转的界面是否有“现在就去购物”特点的控件,如果有该控件程序就往下执行
WebDriverWait(driver,5,0.5).until(ec.presence_of_element_located((By.LINK_TEXT,"现在就去购物 >>")))
#在五秒内每隔0.5秒去检测跳转的界面是否有“现在就去购物”特点的控件，如果有该控件程序就会报错
WebDriverWait(driver,5,0.5).until_not(ec.presence_of_element_located((By.LINK_TEXT,"现在就去购物 >>")))
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()