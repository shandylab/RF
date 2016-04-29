#coding:utf-8
import win32com.client

class shandylib():    
    # 从excel取值,需要import win32com.client模块
    def get_value_from_excel(self,file, sheetname, row, column):
        #file=
        xlApp = win32com.client.Dispatch('Excel.Application')
        xlBook = xlApp.Workbooks.Open(file)
        xlSht = xlBook.Worksheets(sheetname) 
        value = xlSht.Cells(int(row), int(column)).Value
        xlBook.Close(SaveChanges=0) 
        del xlApp
        return value

    # 写值进excel需要import win32com.client模块
    def set_value_to_excel(self,file, sheetname, row, column, value):
        try:
            xlApp = win32com.client.Dispatch('Excel.Application')
            xlBook = xlApp.Workbooks.Open(file)
            xlSht = xlBook.Worksheets(sheetname) 
            xlSht.Cells(int(row), int(column)).Value = value
            xlBook.Close(SaveChanges=1) 
            del xlApp
            return True
        except Exception:
            return False
    
    def readtxt(self,file):
        try:
            f = open(file, "r")  
            while True:  
                line = f.readline()  
                if line:  
                    pass    # do something here 
                    line=unicode(line.strip(),"gbk")        
                    return line
                else:  
                    break
            f.close()
        except Exception:
            return False


  
    
    
