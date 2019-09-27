#修改用户密码
#coding=utf-8

import re
import requests
from jiekou10.opject_api.login_api import Login

class Password():
    def __init__(self,s):
        self.s=s

    #修改密码
    def modify_pas(self):
        url="http://47.104.190.48:8000/xadmin/account/password/"
        r=self.s.get(url)
        # print(r.text)
        token=re.findall('name="csrfmiddlewaretoken" value="(.+?)"',r.text)
        for i in token:
            print(i)
        body={
            "csrfmiddlewaretoken":token[0],
            "csrfmiddlewaretoken":token[0],
            "old_password":"youyou123456",
            "new_password1":"you2626777",
            "new_password2":"you2626777",
        }
        r1=self.s.post(url,data=body)
        # print(r1.text)
        return r1.text

    def get_password_text(self,t):
        if "请登录" in t:
            print("修改成功")
            return True
        else:
            print("修改失败")
            return False

if __name__=="__main__":
    s=requests.session()
    f=Login(s)
    t1=f.user_login()
    f.get_login_text(t1)
    p=Password(s)
    t=p.modify_pas()
    p.get_password_text(t)