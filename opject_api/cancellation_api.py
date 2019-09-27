#注销接口
# coding=utf-8
import requests
import re

class Cancellation():
    def __init__(self,s):
        self.s=s

    def user_zhuxiao(self):
        self.s.get