# 1、导入模块
from time import  sleep
from  selenium import  webdriver
# 2、实例化浏览器对象
driver = webdriver.Chrome()
# 3、打开网页
driver.get("file:/C:/Users/28918/Desktop/testAlert.html")
# 1、执行js方法
driver.execute_script("prom()")
sleep(1)
# 1、在输入框内输入反馈信息
driver.switch_to.alert.send_keys("每天晚上12点整会报错")
# 点击所有正向按钮
driver.switch_to.alert.accept()
# 打印输入框的内容
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
# 点击所有反向按钮
# driver.switch_to.alert.dismiss()
# 4、浏览网页
sleep(8)
# 5、关闭网页
driver.quit()