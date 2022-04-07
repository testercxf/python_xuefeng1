# 1、导入模块
from time import  sleep
from  selenium import  webdriver
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("http://101.133.169.100/yuns/index.php/")

# 注入js
js = " a=document.documentElement.scrollTop=10000"          # 从顶部拉到页面最底部
driver.execute_script(js)
sleep(2)
js = " a =document.documentElement.scrollTop=0"              # 从底部拉到页面最顶部
driver.execute_script(js)
sleep(3)
# 在y轴向下滑动页面的30%
driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.3)")
#移动到指定坐标
sleep(1)
driver.execute_script("window.scrollTo(0,1000)")
# # 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()