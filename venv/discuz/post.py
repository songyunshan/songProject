from locust import HttpLocust, TaskSet, task
import huicetools
from random import choice
from discuz import *
class Discuz_Post(TaskSet):

    @task
    def post(self):
        discuz = Discuz(self.client)
        response = discuz.index()
        fids = huicetools.fetchStringArrayByBoundary(response.text, LB="fid=", RB="\"><img")
        fid = choice(fids)
        print("fid：" + fid)

        #随机选择一个账号
        userinfo = choice(self.locust.userdata)
        userinfo = userinfo.split(",")
        print("登录用户：" + userinfo[0])

        #登录
        response = discuz.login(username = userinfo[0],password = userinfo[1])
        uid = huicetools.fetchStringByBoundary(response.text, LB="uid=", RB="\"")
        print("用户id：" + uid)
        formhash = huicetools.fetchStringByBoundary(response.text, LB="formhash\" value=\"", RB="\"")
        print(formhash)

        headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"}
        self.client.get("/bbs/forum.php?mod=forumdisplay&fid=" + fid,name = "随机选择模块")

        #点击发帖
        with self.client.get("/bbs/forum.php?mod=post&action=newthread&fid=" +
                             fid + "&referer=http%3A//10.17.9.180:8083%3A8888/forum.php%3Fmod%3Dforumdisplay%26fid%3D41",
                             name = "点击发帖") as response:
            hash = huicetools.fetchStringByBoundary(response.text, LB="\"hash\" value=\"", RB="\"")
            print(hash)
            posttime = huicetools.fetchStringByBoundary(response.text, LB="posttime\" value=\"", RB="\"")
            print(posttime)

        #------------------------------上传附件 start--------------------------------------
        url = "/misc.php?mod=swfupload&action=swfupload&operation=upload&fid=" + fid

        data = {"Filename": "20190105154352.jpg", "hash": hash, "filetype": ".jpg", "uid": uid,
                "Upload":"Submit Query"}

        files = {'Filedata': open('20190105154352.jpg', 'rb')}
        #上传附件
        with self.client.post(url, headers=headers, files = files, data=data,name="上传附件") as response:
            fileid = response.text
            print("上传附件：" + response.text)
        # ------------------------------上传附件 end--------------------------------------

        # ------------------------------提交帖子 start--------------------------------------
        url = "/bbs/forum.php?mod=post&action=newthread&fid=" + fid + "&extra=&topicsubmit=yes"
        data = {"formhash": formhash, "posttime": posttime, "wysiwyg": "1", "subject": "dddddddd88888",
                "message": "hhhhhhhhhhxxxxxxxxx", "save": "","attachnew[" + fileid + "][description]": "",
                "uploadalbum": "-2", "newalbum": "请输入相册名称","usesig": "1", "allownoticeauthor":"1"}

        #提交帖子
        with self.client.post(url, headers=headers, data=data, name="提交帖子") as response:
            pass
           # print("提交帖子：" + response.text)
        # ------------------------------提交帖子 end--------------------------------------

        #退出登录
        discuz.logout(formhash)

class DiscizPost_User(HttpLocust):
    task_set = Discuz_Post
    host = "http://10.17.9.180:8083"
    min_wait = 1000
    max_wait = 3000

    userdata = [] #列表，数据可以重复使用
    with open("data/userdata.csv", "r") as file:
        for line in file.readlines():
            userdata.append(line.strip())