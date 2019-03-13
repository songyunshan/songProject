from locust import HttpLocust,TaskSet,task
#随机选取元素 选的是一行
from random import choice
from discuz import huicetools
#在这个类定义期望的业务 继承于TaskSet 才能自动执行LOCUST
class Discuz_Task(TaskSet):
    #权重
    @task(1)
    #打开首页
    def index(self):
        #定义头信息 告诉服务器 浏览器是ie
        headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"}
        #python with 语句 有异常的时候可以正常访问
        with self.client.get("/bbs/forum.php",headers=headers,name ="打开首页") as response:
            print(response.text)
class Discuz_Login(TaskSet):
    @task(2)
    #登录
    def login(self):
        userinfo = choice(self.locust.user_data)
        print(userinfo)
        userinfoNew = userinfo.split(",")

        #定义头信息
        headers ={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0"}
        #请求体
        data = {"fastloginfield":"username","handlekey":"ls","password":userinfoNew[1],"quickforward":"yes","username":userinfoNew[0]}
        # 登录用POST请求 text的值 是从服务器
        with self.client.post("/bbs/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1",headers = headers,
                         data =data,name ="登录") as login:
            print(login.text)

        #登录成功后，刷新首页之后，获取formhash 写 关联函数
        with self.client.get("/bbs/forum.php",name='登录成功刷新首页') as response:
            formhash = huicetools.fetchStringByBoundary(response.text,LB="formhash\" value=\"",RB="\"" )
            formhash =formhash[0]
            print(formhash)
        # 退出
        self.client.get("/bbs/member.php?mod=logging&action=logout&formhash=" + formhash,name='退出')

#用户
class Discuz_Locust(HttpLocust):
    #task_set可以指向哪个业务类
    # 指向打开首页
    #task_set = Discuz_Task
    #指向登录
    task_set = Discuz_Login
    #可以放到用户类里 也可以放到业务类
    host = "http://192.168.4.52:8083"
    min_wait = 1000
    max_wait = 2000
    #定义一个列表 数据可以重复使用
    user_data = []
    #参数化 随机从文件里 取出数据
    with open("./data/data.csv" ,"r") as file:
        #把数据都读出来 去除两端的空格
        for line in file.readlines():
            user_data.append(line.strip())
