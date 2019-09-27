#coding=utf-8
#登陆接口
import requests
import re
class Login():
    def __init__(self,s:requests.session()):
        self.s=s

    def user_login(self,username="roc123",password="you2626777"):
        url="http://47.104.190.48:8000/login/"
        r=self.s.get(url)
        token=re.findall('name="csrfmiddlewaretoken" value="(.+?)"',r.text)
        body={
            "Cancellation":token[0],
            "username":username,
            "password":password,
            "this_is_the_login_form":"1",
            "next":"/xadmin/"
        }
        r1=self.s.post(url,data=body)
        return r1.text

    def get_login_text(self,t):
        if "登录成功" in t:
            print("登陆成功啦")
            return True
        else:
            print("登录失败")
            return False



if __name__=='__main__':
    s=requests.session()
    f=Login(s)
    t=f.user_login()

    t1=f.get_login_text(t)
    print(t1)
