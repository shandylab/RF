#coding:utf-8
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import sys
import xlrd
import win32com.client
from time import sleep

reload(sys)
sys.setdefaultencoding('utf-8')

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
        

for i in range(5,20):
    xlApp=win32com.client.Dispatch('Excel.Application')
    xlBook = xlApp.Workbooks.Open(u'D:\\汽车之家.xlsx')
    xlSht = xlBook.Worksheets(u'已完成') 
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
        if d.page_source.find(str('密码错误'))>0:
            print '密码错误'
            xlSht.Cells(i,4).Value=u'密码错误'
            
        elif d.page_source.find(str('您的账号存在异常'))>0:
            print '您的账号存在异常'
            xlSht.Cells(i,4).Value=u'您的账号存在异常'
        elif d.page_source.find(str(u'*****'))>0:
            print '正常'
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
        
        
        
        
        
        
        
        
        
