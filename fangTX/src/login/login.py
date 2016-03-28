from selenium import webdriver
from time import sleep

d=webdriver.Firefox()
d.get('https://passport.fang.com/register.aspx')
d.find_element_by_id('tel').clear()
d.find_element_by_id('tel').send_keys('13246968702')
sleep(5)
d.find_element_by_id('sendIdentifyingCodeChange').click()

#d.quit()

