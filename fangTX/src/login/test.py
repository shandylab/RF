#coding:utf-8
from selenium import webdriver

d=webdriver.Firefox()
d.get('https://www.hao123.com/')
d.find_element_by_name('word').send_keys(u'黄连')
d.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[3]/form/div[2]/input').click()
