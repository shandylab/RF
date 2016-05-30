
import wx

class Frame(wx.Frame):
    pass

class App(wx.App):
    
    def OnInit(self):
        self.frame=Frame(parent=None,title='Spare')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
#if _name_=='_main_':
app=App()
app.MainLoop()


