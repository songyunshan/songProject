class Discuz:

    client = None

    def __init__(self,client):
        self.client = client
    #打开首页
    def index(self):
        with self.client.get("/bbs/forum.php", name="打开首页") as response:
            return response
    def login(self,username = None,password = None):
        #url = "/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
        url="/bbs/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
        headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"}
        data = {"fastloginfield": "username", "handlekey": "ls", "password": username, "username": password,
                "quickforward": "yes"}
        #登录
        with self.client.post(url, headers =headers, data=data, name="登录") as response:
            pass
        #刷新首页
        with self.client.get("/bbs/forum.php",name="刷新首页") as response:
           return  response
    #退出登录
    def logout(self,formhash = None):
        self.client.get("/bbs/member.php?mod=logging&action=logout&formhash=" + formhash ,name="退出登录")