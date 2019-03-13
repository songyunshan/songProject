from locust import HttpLocust,TaskSet,task
from discuz import huicetools
#队列 保证数据的唯一性
import queue
class Discuz_Register(TaskSet):
    #可以执行
    @task(1)
    def register(self):
        #打开首页 获取服务器端返回的formhash
        with self.client.get("/bbs/forum.php",name="打开首页") as response:
            formhash = huicetools.fetchStringByBoundary(response.text, LB="formhash\" value=\"", RB="\"")
            formhash = formhash[0]
            print(formhash)
        #点击立即注册
        self.client.get("/bbs/member.php?mod=register",name='点击立即注册')
        # 从队列中 取数据
        try:
            userinfo = self.locust.user_data.get()  # 获取唯一的用户信息
        except queue.Empty:
            print("数据已经取完")
            exit(0)
        userinfo = userinfo.split(",")
        #验证用户名
        self.client.get("/bbs/forum.php?mod=ajax&inajax=yes&infloat=register&handlekey=register&ajaxmenu=1&action=checkusername&username=huice003",
                        name='验证用户名')
        #验证邮箱
        self.client.get("/bbs/forum.php?mod=ajax&inajax=yes&infloat=register&handlekey=register&ajaxmenu=1&action=checkemail&email=huice003@163.com",
                        name='验证邮箱')

        #提交
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0"}
        data ={"activationauth":"","formhash":formhash,"gxbCcR":userinfo[1],"iZZ344":userinfo[0],"lFChnP":userinfo[1],"referer":"forum.php","regsubmit":"yes","t7ot7K":userinfo[2]}
        with self.client.post("/bbs/member.php?mod=register&inajax=1",headers = headers,data=data,name="提交注册") as regist:
            print(userinfo)
            print(regist.text)



class Discuz_Register_User(HttpLocust):
    # 指向登录
    task_set = Discuz_Register
    # 可以放到用户类里 也可以放到业务类
    host = "http://192.168.4.52:8083"
    min_wait = 1000
    max_wait = 2000
    #初始化一个空队列 先进先出
    user_data = queue.Queue()

    with open("./data/newdata.csv","r") as file:
        for line in file.readlines():
            user_data.put_nowait(line.strip())




