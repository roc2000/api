#添加学生
#coding=utf-8
import requests
import re
from jiekou10.opject_api.login_api import Login
class Add_student():
    def __init__(self,s):
        self.s=s

    def add_stu(self):
        url = "http://47.104.190.48:8000/xadmin/hello/student/add/"
        r=self.s.get(url)
        token=re.findall('name="csrfmiddlewaretoken" value="(.+?)"',r.text)
        body={
            "csrfmiddlewaretoken":token[0],
            "csrfmiddlewaretoken":token[0],
            "student_id":"009",
            "name":"张无极",
            "gender":"M",
            "age":"16",
            "_save":"",
        }
        r1=self.s.post(url,data=body)

        return r1.text

    def get_student_text(self,t):
        if "学号" in t:
            print("添加成功")
            return True
        else:
            print("添加失败")
            return False
if __name__=="__main__":
    s=requests.session()
    l=Login(s)
    l.user_login()
    a=Add_student(s)
    a1=a.add_stu()
    a.get_student_text(a1)