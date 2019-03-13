from locust import HttpLocust, TaskSet, task
from common.huicetools import *
import urllib

class Alfresco_Login(TaskSet):
    #打开登录界面
    @task(1)
    def Login(self):
        url = "/share/page/dologin"
        data={"username":"admin","success":"/share/page/","failure":"/share/page/type/login?error=true","password":"admin"}
        with self.client.post(url,data=data,name="登录") as response:
            #检查点，如果登录失败，后续业务不执行
            print(response.text)

        #点击创建html文件 获取token
        with self.client.get("/share/page/context/mine/create-content?destination=workspace://SpacesStore/328115ae-1ea7-418a-9089-15a723081ca2&itemId=cm:content&mimeType=text/html",name="点击创建html") as response:
            token = fetchStringByBoundary(response.headers["Set-Cookie"],LB="Alfresco-CSRFToken=",RB=";")
        # 做编码转换 python实现 url 编码转换
            token = urllib.parse.unquote(token)
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0","Alfresco-CSRFToken":token,"Content-Type":"application/json; charset=UTF-8"}
        data = "{\"alf_destination\":\"workspace://SpacesStore/328115ae-1ea7-418a-9089-15a723081ca2\",\"prop_cm_name\":\"ttt-名称1\",\"prop_cm_title\":\"ttt-标题1\",\"prop_cm_description\":\"ttt-说明1\",\"prop_cm_content\":\"<p>ttt-内容1</p>\",\"prop_mimetype\":\"text/html\",\"prop_app_editInline\":\"true\"}"
        with self.client.post("/share/proxy/alfresco/api/type/cm%3acontent/formprocessor",headers=headers,data=data,name="提交html内容") as response:
            print(response.text)


class Alfresco_Login_User(HttpLocust):
    task_set = Alfresco_Login
    host = "http://huicewang.nat123.net"
    min_wait = 1000
    max_wait = 3000