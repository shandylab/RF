#coding:utf-8

import win32com.client

#从excel取值,需要import win32com.client模块
def get_value_from_excel(file,sheetname,row,column):   
    xlApp=win32com.client.Dispatch('Excel.Application')
    xlBook = xlApp.Workbooks.Open(file)
    xlSht = xlBook.Worksheets(sheetname) 
    value = xlSht.Cells(row,column).Value
    xlBook.Close(SaveChanges=0)     
    del xlApp
    return value

#写值进excel需要import win32com.client模块
def set_value_to_excel(file,sheetname,row,column,value):
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
        

x=get_value_from_excel('D:\\test.xlsx','Sheet1',1,1)
print str(x) 
y=set_value_to_excel(u'D:\\test.xlsx',u'Sheet1',2,9,u'test')
print y 


