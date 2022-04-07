# 1、导入模块
from time import  sleep
from  selenium import  webdriver
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/")
driver.maximize_window()                                             #最大化窗体
sleep(2)
driver.implicitly_wait(5)
#xpath相对路径
driver.find_element_by_xpath("//*[contains(@placeholder,'请输入')]").send_keys("123")  #属性包含了请输入的属性值定位方式，输入123
driver.find_element_by_xpath("//*[@class='schhot']/a[1]").click()    #点击“女装”
driver.find_element_by_xpath("//*[@class='schhot']/a[2]").click()    #点击“荔枝”
driver.find_element_by_xpath("//*[@class='schhot']/a[3]").click()    #点击“家装节”
driver.find_element_by_xpath("//*[text()='男装']").click()           #通过标签中的文本信息定位，点击“男装”
driver.find_element_by_xpath("//*[@class='schhot']/a[5]").click()    #点击“全场一员”
driver.find_element_by_xpath("//*[@class='schhot']/a[6]").click()    #点击“T恤男2016”
driver.find_element_by_xpath("//*[@class='schhot']/a[7]").click()    #点击“运动男鞋”
driver.find_element_by_xpath("//*[@class='schhot']/a[8]").click()    #点击“9.9抢大牌”
driver.implicitly_wait(6)                                            #后面的元素定位在6秒内加载后继续执行后面的代码
driver.find_element_by_xpath("//*[@class='pp']/dd/a[1]").click()     #点击“全部”
driver.find_element_by_xpath("//*[@class='pp']/dd/a[2]").click()     #点击“GXG”
driver.find_element_by_xpath("//*[@class='pp']/dd/a[3]").click()     #点击“森马”
driver.find_element_by_xpath("//*[@class='pp']/dd/a[4]").click()     #点击“优衣库”
driver.find_element_by_xpath("//*[@class='pp']/dd/a[5]").click()     #点击“花花公子”
driver.find_element_by_xpath("//*[@class='header' and @title='秒杀']").click()     #点击“秒杀”
driver.close()                                                       #关闭当前窗体
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()