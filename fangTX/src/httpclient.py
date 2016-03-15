
import requests
from time import sleep


#login
payload = {'uName':'shandy', 'pWord':'61523577'}
r = requests.get('http://api.shjmpt.com:9002/pubApi/uLogin', params=payload)
token=(r.text).split("&")[0]
print token

#getPhone
payload = {'ItemId':'28', 'token':token}
r = requests.get('http://api.shjmpt.com:9002/pubApi/GetPhone', params=payload)
Phone=(r.text).split(";")[0]
print Phone

sleep(40)

payload = {'ItemId':'28', 'token':token,'Phone':Phone}
r = requests.get('http://api.shjmpt.com:9002/pubApi/GMessage', params=payload)
messg=(r.text).split("&")[3]
yzm=messg.split(r"验证码")[1][0:6]
print yzm

#http://api.shjmpt.com:9002/pubApi/GMessage?token=WPLEFC1PE8c36WVMqYV54z7XyAmGXM15&ItemId=28&Phone=13252782564
#MSG&28&13252782564&验证码847569，当日内有效。如果您未自定义密码，则注册时的验证码即为原始密码，请及时修改。如非本人操作，回复TD退阅。【搜房网】





