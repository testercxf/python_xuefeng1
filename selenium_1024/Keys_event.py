# 1、导入模块
from time import  sleep
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/goods/theme?id=6")
driver.maximize_window()
# 需求
# 1、商品搜索框输入商品
driver.find_element_by_xpath("//*[@class='but1']").send_keys("女装")
# 2、光标向左移动一位
driver.find_element_by_xpath("//*[@class='but1']").send_keys(Keys.LEFT)
# 3、在光标后面输入一个空格
driver.find_element_by_xpath("//*[@class='but1']").send_keys(Keys.SPACE)
# 4、全选输入框内容
driver.find_element_by_xpath("//*[@class='but1']").send_keys(Keys.CONTROL,"a")
# 5、复制输入框的数据
driver.find_element_by_xpath("//*[@class='but1']").send_keys(Keys.CONTROL,"c")
# 6、光标向右移动一位后粘贴复制的数据
sleep(1)
driver.find_element_by_xpath("//*[@class='but1']").send_keys(Keys.RIGHT)
driver.find_element_by_xpath("//*[@class='but1']").send_keys(Keys.CONTROL,"v")
# 点击键盘上的enter键进行搜索
sleep(2)
driver.find_element_by_xpath("//*[@class='but1']").send_keys(Keys.ENTER)
# 4、浏览网页
sleep(5)
# 5、关闭网页
driver.quit()


