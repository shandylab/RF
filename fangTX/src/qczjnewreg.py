#coding:utf-8
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import sys
import win32com.client
from time import sleep

reload(sys)
sys.setdefaultencoding('utf-8')

def yzkyd(username,d):
    d.get(u'http://account.autohome.com.cn/register')
    e=d.find_element_by_id('UserName')
    e.clear()
    e.send_keys(username)
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
    
    
    
if __name__=="__main__":
    b=webdriver.Firefox()    
    print yzkyd(username=u'sdfalloojjh',d=b)
    
