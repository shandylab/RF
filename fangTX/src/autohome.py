#coding:utf-8
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import  xdrlib ,sys
import xlrd
from time import sleep

reload(sys)
sys.setdefaultencoding('utf-8')

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
        

for i in range(0,4):
    try:
        d=webdriver.Firefox()
        try:
            d.set_page_load_timeout(10)
            d.get('http://account.autohome.com.cn/login?backUrl=http%3a%2f%2fi.autohome.com.cn%2fsetting%2fmobile')
        except Exception:      
            try:
                d.send_keys(Keys.CONTROL +'Escape')
            except Exception: 
                print 'time out'
        
        e=d.find_element_by_id('UserName')
        e.clear()
        data=open_excel('d:/test.xls')    
        sheet1=data.sheet_by_name('Sheet1')
    #    unicode('你有病我也没药' , errors='ignore')
        name=sheet1.cell(i,0).value
        e.send_keys(name)
        e=d.find_element_by_id('PassWord')
        e.clear()
        pwd=str(sheet1.cell(i,1).value)
        e.send_keys(pwd)
        d.find_element_by_id('SubmitLogin').click()
        sleep(5)    
        if d.page_source.find(str('您的账号存在异常'))==-1:
            print '正常'
        else:
            print '您的账号存在异常'       
        d.quit()
    except:
        print str(i)+' 错误'
