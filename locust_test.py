from locust import HttpUser, TaskSet, task
import json

# 定义用户行为
class UserBehavior(TaskSet):
    def on_start(self):
        print("start")

    @task(1)
    def task_push(self):
        head = {"Content-Type":"application/json", "Cookie":"userId=101010013817072; token=953e2ba49084a990c964bf57a3aa9096; timeStamp=1586835808658108; mobile=15958032925; sessionId=6815407899486085346; _NOWUID=101010013817072; isLogined=1; index_router=/marketCenter"}
        body = {"forwardConfig":"[{\"msgType\":1,\"msgContent\":\"http://filesystem.api.jituancaiyun.net/sfs/file?digest=fida68ba8bdcc15313681dbe70a0f5d788d\"}，{\"msgType\":2,\"msgContent\":\"http://filesystem.api.jituancaiyun.net/sfs/file?digest=fid5b194d7590a569e6d6298596828af515\"},{\"msgType\":4,\"msgContent\":\"http://filesystem.api.jituancaiyun.net/sfs/file?digest=fid291c9f3bf00ee8f30a6b554bfc148e72\"}]","materialId":1980,"materialType":2,"attachContent":"117","publishMode":2,"publishRange":3,"authorName":"张童","supportCode":1,"policyType":1}
        body = json.dumps(body)
        res = self.client.post("/yxzx-opr/publish/submit.json", data=body, headers=head)

        # 打印接口response详情
        # print(res.content.decode("utf-8"))



class WebsiteUser(HttpUser):
    host = "http://cmmc.jituancaiyun.net"
    task_set = UserBehavior()
    min_wait = 150
    max_wait = 500