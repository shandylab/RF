#coding:utf-8
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import sys
import win32com.client
from time import sleep
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

def yzkyd(username,d):
    d.get(u'http://account.autohome.com.cn/register')
    e=d.find_element_by_id('UserName')
    e.clear()
    e.send_keys(username)
    #d.acti
    d.find_element_by_id('Password').click()
    sleep(4)
    x=d.find_element_by_id('autohomeregister').text   
    if x.find(u'一旦注册成功不能修改')>0:
        return True
    else:
        return False



def yzky(username):
    d=webdriver.Firefox()
    d.get(u'http://account.autohome.com.cn/register')
    e=d.find_element_by_id('UserName')
    e.clear()
    e.send_keys(username)
    d.find_element_by_id('Password').click()
    sleep(4)
    x=d.find_element_by_id('autohomeregister').text
    d.quit()   
    if x.find(u'一旦注册成功不能修改')>0:
        return True
    else:
        return False   
#从excel取值,需要import win32com.client模块
def get_value_from_excel(file= 'file.xls',sheetname='sheetname',row='row',column='column'):
    xlApp=win32com.client.Dispatch('Excel.Application')
    xlBook = xlApp.Workbooks.Open(file)
    xlSht = xlBook.Worksheets(sheetname) 
    value = xlSht.Cells(row,column).Value
    xlBook.Close(SaveChanges=0) 
    del xlApp
    return value

#写值进excel需要import win32com.client模块
def set_value_to_excel(file= 'file.xls',sheetname='sheetname',row='row',column='column',value='value'):
    try:
        xlApp=win32com.client.Dispatch('Excel.Application')
        xlBook = xlApp.Workbooks.Open(file)
        xlSht = xlBook.Worksheets(sheetname) 
        xlSht.Cells(row,column).Value=value
        xlBook.Close(SaveChanges=1) 
        del xlApp
        return True
    except Exception:
        return False    
#登录
payload = {'uName':'shandy', 'pWord':'61523577'}
r = requests.get('http://api.shjmpt.com:9002/pubApi/uLogin', params=payload)
token=(r.text).split("&")[0]
print token    
    
if __name__=="__main__":
    d=webdriver.Firefox()
    for i in range(7,8):
        set_value_to_excel(u'D:\\test.xlsx',u'Sheet1',i,4,u'正在注册')
        username=get_value_from_excel(u'D:\\test.xlsx',u'Sheet1',i,1)
        pwd=get_value_from_excel(u'D:\\test.xlsx',u'Sheet1',i,2)
        if yzkyd(username=username,d=d):
            d.get(u'http://account.autohome.com.cn/register')
            e=d.find_element_by_id('UserName')
            e.clear()
            e.send_keys(username)
            e=d.find_element_by_id('Password')
            e.clear()
            e.send_keys(pwd)
            sleep(15)
            d.find_element_by_id('SubmitBtn').click()
            sleep(4)
           
            if d.current_url.find(u'AddCar')>0:
                d.get('http://i.autohome.com.cn/setting/mobile')
                #获取手机号
                payload = {'ItemId':'11187', 'token':token}
                r = requests.get('http://api.shjmpt.com:9002/pubApi/GetPhone', params=payload)
                Phone=(r.text).split(";")[0]
                print Phone
                
                d.find_element_by_id('tphonenumber').clear()
                d.find_element_by_id('tphonenumber').send_keys(Phone)
                sleep(1)
                d.find_element_by_id('tchecknumber').click()
                sleep(1)
                d.find_element_by_id('btngetchecknumber').click()
                
                sleep(20)
                
                payload = {'ItemId':'11187', 'token':token,'Phone':Phone}
                isgetyzm=False
                for i in range(10):    
                    r = requests.get('http://api.shjmpt.com:9002/pubApi/GMessage', params=payload)
                    messg=(r.text)
                    if len(messg)>30:
                        me=messg.split("&")[3]        
                        yzm=(str(me).split('验证码')[1])[0:6]        
                        isgetyzm=True
                    else:
                        pass                        
                    if isgetyzm:
                        break
                    sleep(5)
                print yzm
                if not isgetyzm:
                    payload = {'phoneList':Phone, 'token':token}
                    r = requests.get('http://api.shjmpt.com:9002/pubApi/AddBlack', params=payload)
                    break    
                
                d.find_element_by_id('tchecknumber').send_keys(yzm)
                sleep(1)
                d.find_element_by_id('save').click()
            
                
        else:
            set_value_to_excel(u'D:\\test.xlsx',u'Sheet1',i,4,u'不可用')
                
    
            
            
    
