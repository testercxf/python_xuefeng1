import pytest
import requests

class  TestSend():
    def  test_send_get(self):
        url = "https://selectcar.yiche.com/selectcarforapp"
        data = {
            "mid":7,
            "s":4,
            "page":1,
            "pagesize":20,
            "cityId":201
        }
        res = requests.request("get",url,params=data)
        #以json格式打印
        print(res.json())
        #断言message参数值为"ok"
        assert  res.json()['message'] == "ok"
        # raise  Exception("错啦")          #抛出一个异常

        # print(res.json()['data']['resList'][1]['name'])        #返回节点参数值为“卡罗拉”信息
        # print(res.url)              #返回url
        # print(res.text)             #返回文本格式的数据
        # print(res.content)          #返回字节格式的数据
        # print(res.encoding)         #返回编码格式
        # print(res.headers)          #返回响应头信息
        # print(res.status_code)      #返回响应状态码

    # @pytest.mark.smoke     #标记这是一个冒烟的用例，只执行这条用例    需要在执行命令里加上  -m "分组的用例"
    def  test_send_post(self):
        url = "http://182.92.178.83:8081/login"
        data = {
            "username":"sang",
            "password":123
        }
        res = requests.request("post",url,data=data)
        print(res.json())
        #断言是否登录 成功
        assert  res.json()["msg"]  == "登录成功"  and  res.json()["status"] == "success"

if __name__ == '__main__':
    pytest.main(['-vs'])