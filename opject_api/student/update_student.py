#添加学生
#coding=utf-8
import re
import requests
from jiekou10.opject_api.login_api import Login
class Update_student():
    def __init__(self,s):
        self.s=s

    def user_update(self):
        url="http://47.104.190.48:8000/xadmin/hello/student/361/update/"
        r=self.s.get(url)
        token=re.findall('name="csrfmiddlewaretoken" value="(.+?)"',r.text,timeout=0.1)  #timeout超时时间，响应超过这个时间报错
        body={
            "csrfmiddlewaretoken":token[0],
            "csrfmiddlewaretoken":token[0],
            "student_id":"009",
            "name":"张学友",
            "gender":"M",
            "age":"19",
            "_save":"",
        }
        r1=self.s.post(url,data=body)
        return  r1.text

    def get_student_text(self,t):
        if "学生" in t:
            print("修改成功")
            return True
        else:
            print("修改失败")
            return False

if __name__=="__main__":
    s=requests.session()
    l=Login(s)
    r=l.user_login()
    l.get_login_text(r)
    u=Update_student(s)
    r2=u.user_update()
    # print(r2)
    u.get_student_text(r2)


