
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
yzm=messg.split(r"��֤��")[1][0:6]
print yzm

#http://api.shjmpt.com:9002/pubApi/GMessage?token=WPLEFC1PE8c36WVMqYV54z7XyAmGXM15&ItemId=28&Phone=13252782564
#MSG&28&13252782564&��֤��847569����������Ч�������δ�Զ������룬��ע��ʱ����֤�뼴Ϊԭʼ���룬�뼰ʱ�޸ġ���Ǳ��˲������ظ�TD���ġ����ѷ�����





