from selenium import webdriver

d=webdriver.Firefox()
d.get('http://www.hao123.com')
d.find_element_by_name('word').send_keys('xxxxxx')