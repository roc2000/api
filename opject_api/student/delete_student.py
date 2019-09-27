#删除学生
#coding=utf-8
import requests
import re
class Delete_student():
    def __init__(self,s):
        self.s=s

    def user_delete(self):
        url="http://47.104.190.48:8000/xadmin/hello/student/362/delete/"
        r=self.s.get(url)
        token=re.findall('name="csrfmiddlewaretoken" value="(.+?)"',r.text)
        body={
            "csrfmiddlewaretoken":token[0],
            "post":"yes",
        }
        r1=self.s.post(url,data=body)
        return r1.text

    def get_student_text(self,t):
        if "" in t:
            print("删除成功")
            return True
        else:
            print("删除失败")
            return False

if __name__=="__main__":
