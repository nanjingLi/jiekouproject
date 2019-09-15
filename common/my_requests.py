from requests import  session
import requests
class HttpSession():
    s = session()
    def __init__(self,method,url,data):
        self.method=method
        self.url=url
        self.data=data
    def httpSession(self):
        if self.method == 'get':
            return self.s.get(url=self.url, params=self.data)
        elif self.method == 'post':
            return self.s.post(url=self.url, data=self.data)
class HttpRequest():
    def __init__(self,method,url,data):
        self.method=method
        self.url=url
        self.data=data
    def httpRequest(self):
        if self.method=='get':
            return requests.get(url=self.url,params=self.data)
        elif self.method =='post':
            return requests.post(url=self.url, data=self.data)

