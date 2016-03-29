#coding:utf-8
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import sys
import win32com.client
from time import sleep

#===============================================================================
reload(sys)
sys.setdefaultencoding('utf-8')
#===============================================================================

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

for i in range(518,519):
    
    try:
        name = get_value_from_excel(u'D:\\汽车之家.xlsx',u'Sheet2',i,1)
        pwd = get_value_from_excel(u'D:\\汽车之家.xlsx',u'Sheet2',i,2)
        print name
        
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
        sleep(8)    
        page_source=d.page_source
        if page_source.find(str(u'密码错误'))>0:
            print '密码错误'                
            set_value_to_excel(u'D:\\汽车之家.xlsx',u'Sheet2',i,6,u'密码错误')       
        elif page_source.find(str(u'您的账号存在异常'))>0:
            print '您的账号存在异常'
            set_value_to_excel(u'D:\\汽车之家.xlsx',u'Sheet2',i,6,u'您的账号存在异常') 
        elif page_source.find(str(u'*****'))<0:
            print '未绑手机'
            set_value_to_excel(u'D:\\汽车之家.xlsx',u'Sheet2',i,6,u'未绑手机')          
        else:
            d.find_element_by_class_name(u'ico_lt01').click()
            sleep(5)
            d.get(d.find_element_by_id('app').get_attribute('src'))
            sleep(2)
            if d.page_source.find(u'关禁闭')>0:
                print '关禁闭'
                set_value_to_excel(u'D:\\汽车之家.xlsx',u'Sheet2',i,6,u'关禁闭')          
            else:
                print '正常'
                set_value_to_excel(u'D:\\汽车之家.xlsx',u'Sheet2',i,6,u'正常')  
        d.quit()
        
    except Exception,e:  
        print Exception,":",e
print '完成'
        
