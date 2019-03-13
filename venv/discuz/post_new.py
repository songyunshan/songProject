from locust import HttpLocust,TaskSet,task
from discuz import huicetools
from random import choice
from discuz import *
class  Discuz_Post_New:
    def post_new(self):
        pass
class DiscizPostNew_User(HttpLocust):
    task_set = Discuz_Post
    host = "http://192.168.1.201:8888"
    min_wait = 1000
    max_wait = 3000