#coding:utf-8
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import sys
import xlrd
import win32com.client
from time import sleep
import requests
from httpclient import yzm

reload(sys)
sys.setdefaultencoding('utf-8')

#登录
payload = {'uName':'shandy', 'pWord':'61523577'}
r = requests.get('http://api.shjmpt.com:9002/pubApi/uLogin', params=payload)
token=(r.text).split("&")[0]
print token



for i in range(2,6):
    xlApp=win32com.client.Dispatch('Excel.Application')
    xlBook = xlApp.Workbooks.Open(u'D:\\汽车之家.xlsx')
    xlSht = xlBook.Worksheets(u'绑定手机') 
    try:
        name = xlSht.Cells(i,1).Value
        pwd = xlSht.Cells(i,2).Value
        
        d=webdriver.Firefox()
        try:
            d.set_page_load_timeout(20)
            d.get(u'http://account.autohome.com.cn/login?backUrl=http%3a%2f%2fi.autohome.com.cn%2fsetting%2fmobile')
        except Exception:      
            try:
                d.send_keys(Keys.CONTROL +'Escape')
            except Exception: 
                print 'time out'
        
        e=d.find_element_by_id('UserName')
        e.clear()  
        e.send_keys(name)
        e=d.find_element_by_id('PassWord')
        e.clear()        
        e.send_keys(pwd)
        d.find_element_by_id('SubmitLogin').click()
        sleep(5)    
        if d.page_source.find(str('账号或密码错误'))>0:
            print '密码错误'
            xlSht.Cells(i,4).Value=u'账号或密码错误'            
        elif d.page_source.find(str('您的账号存在异常'))>0:
            print '您的账号存在异常'
            xlSht.Cells(i,4).Value=u'您的账号存在异常'
        elif d.page_source.find(str(u'请绑定手机'))>0:
            
            payload = {'ItemId':'28', 'token':token}
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
                    yzm='not get yzm'
                if isgetyzm:
                    break
                sleep(5)
            print yzm
            if cmp(yzm,'not get yzm')==0:
                payload = {'phoneList':Phone, 'token':token}
                r = requests.get('http://api.shjmpt.com:9002/pubApi/AddBlack', params=payload)
                break
                
            d.find_element_by_id('tchecknumber').send_keys(yzm)
            sleep(1)
            d.find_element_by_id('save').click()
            
            
            
            xlSht.Cells(i,4).Value=u'正常'  
        else:
            print '错误'         
        d.quit()
        xlBook.Close(SaveChanges=1) 
    except:
        xlBook.Close() 
        del xlApp
        print str(i)+' 错误'
print '完成'

