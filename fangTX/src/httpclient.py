#coding:utf-8
import requests
from time import sleep
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


#登录
payload = {'uName':'shandy', 'pWord':'61523577'}
r = requests.get('http://api.shjmpt.com:9002/pubApi/uLogin', params=payload)
token=(r.text).split("&")[0]
print token

#获取手机号
payload = {'ItemId':'28', 'token':token}
r = requests.get('http://api.shjmpt.com:9002/pubApi/GetPhone', params=payload)
Phone=(r.text).split(";")[0]
print Phone

sleep(20)

#获取验证码
payload = {'ItemId':'28', 'token':token,'Phone':Phone}
isgetyzm=False
for i in range(10):    
    r = requests.get('http://api.shjmpt.com:9002/pubApi/GMessage', params=payload)
    messg=(r.text)
    if len(messg)>30:
        me=messg.split("&")[3]        
        yzm=(str(me).split('验证码')[1])[0:6]        
        isgetyzm=True
    else:
        yzm='not get yzm'
    if isgetyzm:
        break
    sleep(5)
print yzm

#加黑    
tel=""
payload = {'phoneList':tel, 'token':token}
r = requests.get('http://api.shjmpt.com:9002/pubApi/AddBlack', params=payload)

#退出
payload = {'token':token}
r = requests.get('http://api.shjmpt.com:9002/pubApi/uExit', params=payload)

