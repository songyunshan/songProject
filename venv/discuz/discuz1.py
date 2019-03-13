from locust import HttpLocust,TaskSet,task
class Discuz_Post(TaskSet):
    # 打开首页
    def index(self):
        # 定义头信息 告诉服务器 浏览器是ie
        headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"}
        # python with 语句 有异常的时候可以正常访问
        with self.client.get("/bbs/forum.php", headers=headers, name="打开首页") as response:
            print(response.text)
    def login(self,username = username,password = password):
        # 定义头信息
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0"}
        # 请求体
        data = {"fastloginfield": "username", "handlekey": "ls", "password": userinfoNew[1], "quickforward": "yes",
                "username": userinfoNew[0]}
        # 登录用POST请求 text的值 是从服务器
        with self.client.post(
                "/bbs/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1",
                headers=headers,
                data=data, name="登录") as login:
            print(login.text)
        # 登录成功后，刷新首页之后，获取formhash 写 关联函数
        with self.client.get("/bbs/forum.php", name='登录成功刷新首页') as response:
            formhash = huicetools.fetchStringByBoundary(response.text, LB="formhash\" value=\"", RB="\"")
            formhash = formhash[0]
            print(formhash)