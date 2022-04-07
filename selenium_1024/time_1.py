# 1、导入模块
from time import  sleep
from  selenium import  webdriver
from selenium.webdriver.common.keys import Keys
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("https://hotel.meituan.com/xian/")
sleep(3)
driver.maximize_window()
# 普通时间控件处理方式
time = driver.find_element_by_xpath("//*[@id='HD_CheckIn']")
time.clear()
time.send_keys("2021-10-25")
#模拟用户利用键盘操作定位后全选数据，删除，输入指定格式日期
driver.find_element_by_xpath("//*[@id='HD_CheckIn']").send_keys(Keys.CONTROL,"a")
driver.find_element_by_xpath("//*[@id='HD_CheckIn']").send_keys(Keys.BACKSPACE)
driver.find_element_by_xpath("//*[@id='HD_CheckIn']").send_keys("2021-10-25")
# 特殊时间控件处理方式
js = "document.getElementByXpath("").removeAttribute('readonly')"          #调用js方法
driver.execute_script(js)                                    #执行通过id定位输入框，并移除掉readonly属性
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()