# 1、导入模块
from time import  sleep
from  selenium import  webdriver
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/")
# 需求
# 1、获取商品搜索框控件的尺寸
size = driver.find_element_by_xpath("//*[@class='but1']").size
print(size)
# 2、获取女装超链接控件的文本信息
text = driver.find_element_by_link_text("女装").text
print(text)
# 3、获取标签里的属性值
get_attribute = driver.find_element_by_xpath("//*[@class='but1']").get_attribute("placeholder")
print(get_attribute)
# 4、获取在商品输入框里已输入的数据
driver.find_element_by_xpath("//*[@class='but1']").send_keys("nihao")
get_attribute = driver.find_element_by_xpath("//*[@class='but1']").get_attribute('value')
print(get_attribute)
# 5、判断搜索按钮是否已加载成功
is_displayed = driver.find_element_by_link_text("女装").is_displayed()
print(is_displayed)
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()