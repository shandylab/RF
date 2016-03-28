#coding:utf-8
import win32com.client

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


  
    
    