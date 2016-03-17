#coding:utf-8
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import sys
from time import sleep 

for i in range(5):
    sleep(10)
    d=webdriver.Firefox()
    d.get('http://1212.ip138.com/ic.asp')
    print d.page_source
    d.quit()
    print i
    

