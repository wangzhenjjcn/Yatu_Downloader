#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Yatu视频下载')
        self.master.geometry('1157x689')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('ChromeFrame.TLabelframe',font=('宋体',9))
        self.ChromeFrame = LabelFrame(self.top, text='浏览器下载', style='ChromeFrame.TLabelframe')
        self.ChromeFrame.place(relx=0.007, rely=0.511, relwidth=0.983, relheight=0.478)

        self.style.configure('VideoDownloaderFrame.TLabelframe',font=('宋体',9))
        self.VideoDownloaderFrame = LabelFrame(self.top, text='视频下载', style='VideoDownloaderFrame.TLabelframe')
        self.VideoDownloaderFrame.place(relx=0.007, rely=0.012, relwidth=0.983, relheight=0.489)

        self.style.configure('CloseChromeBtn.TButton',font=('宋体',9))
        self.CloseChromeBtn = Button(self.ChromeFrame, text='关闭浏览器', command=self.CloseChromeBtn_Cmd, style='CloseChromeBtn.TButton')
        self.CloseChromeBtn.place(relx=0.028, rely=0.535, relwidth=0.106, relheight=0.149)

        self.LogListVar = StringVar(value='')
        self.LogListFont = Font(font=('宋体',9))
        self.LogList = Listbox(self.ChromeFrame, listvariable=self.LogListVar, font=self.LogListFont)
        self.LogList.place(relx=0.162, rely=0.097, relwidth=0.803, relheight=0.851)

        self.style.configure('AlyseBtn.TButton',font=('宋体',9))
        self.AlyseBtn = Button(self.ChromeFrame, text='分析当前页面', command=self.AlyseBtn_Cmd, style='AlyseBtn.TButton')
        self.AlyseBtn.place(relx=0.028, rely=0.316, relwidth=0.106, relheight=0.149)

        self.style.configure('OpenChromeBtn.TButton',font=('宋体',9))
        self.OpenChromeBtn = Button(self.ChromeFrame, text='打开浏览器', command=self.OpenChromeBtn_Cmd, style='OpenChromeBtn.TButton')
        self.OpenChromeBtn.place(relx=0.028, rely=0.097, relwidth=0.106, relheight=0.149)

        self.style.configure('ChoseFolderBtn.TButton',font=('宋体',9))
        self.ChoseFolderBtn = Button(self.VideoDownloaderFrame, text='选择下载目录', command=self.ChoseFolderBtn_Cmd, style='ChoseFolderBtn.TButton')
        self.ChoseFolderBtn.place(relx=0.894, rely=0.19, relwidth=0.092, relheight=0.122)

        self.style.configure('DownloadBtn.TButton',font=('宋体',9))
        self.DownloadBtn = Button(self.VideoDownloaderFrame, text='下载视频', command=self.DownloadBtn_Cmd, style='DownloadBtn.TButton')
        self.DownloadBtn.place(relx=0.894, rely=0.047, relwidth=0.092, relheight=0.122)

        self.M3U8AdressTextVar = StringVar(value='')
        self.M3U8AdressText = Entry(self.VideoDownloaderFrame, textvariable=self.M3U8AdressTextVar, font=('宋体',9))
        self.M3U8AdressText.place(relx=0.091, rely=0.071, relwidth=0.789, relheight=0.098)

        self.style.configure('DownloadFolderLabel.TLabel',anchor='w', font=('宋体',9))
        self.DownloadFolderLabel = Label(self.VideoDownloaderFrame, text='尚未初始化', style='DownloadFolderLabel.TLabel')
        self.DownloadFolderLabel.place(relx=0.091, rely=0.237, relwidth=0.782, relheight=0.074)

        self.style.configure('Label2.TLabel',anchor='w', font=('宋体',9))
        self.Label2 = Label(self.VideoDownloaderFrame, text='下载目录：', style='Label2.TLabel')
        self.Label2.place(relx=0.014, rely=0.237, relwidth=0.057, relheight=0.074)

        self.style.configure('Label1.TLabel',anchor='w', font=('宋体',9))
        self.Label1 = Label(self.VideoDownloaderFrame, text='M3U8地址：', style='Label1.TLabel')
        self.Label1.place(relx=0.014, rely=0.095, relwidth=0.057, relheight=0.05)

        self.DownloadListVar = StringVar(value='')
        self.DownloadListFont = Font(font=('宋体',9))
        self.DownloadList = Listbox(self.VideoDownloaderFrame, listvariable=self.DownloadListVar, font=self.DownloadListFont)
        self.DownloadList.place(relx=0.091, rely=0.38, relwidth=0.789, relheight=0.546)

        self.style.configure('AddListBtn.TButton',font=('宋体',9))
        self.AddListBtn = Button(self.VideoDownloaderFrame, text='添加到队列', command=self.AddListBtn_Cmd, style='AddListBtn.TButton')
        self.AddListBtn.place(relx=0.894, rely=0.38, relwidth=0.092, relheight=0.122)

        self.style.configure('DownloadListBtn.TButton',font=('宋体',9))
        self.DownloadListBtn = Button(self.VideoDownloaderFrame, text='下载队列', command=self.DownloadListBtn_Cmd, style='DownloadListBtn.TButton')
        self.DownloadListBtn.place(relx=0.894, rely=0.522, relwidth=0.092, relheight=0.122)

        self.style.configure('Label3.TLabel',anchor='w', font=('宋体',9))
        self.Label3 = Label(self.VideoDownloaderFrame, text='下载队列：', style='Label3.TLabel')
        self.Label3.place(relx=0.014, rely=0.38, relwidth=0.057, relheight=0.074)

        self.style.configure('StopDownloadBtn.TButton',font=('宋体',9))
        self.StopDownloadBtn = Button(self.VideoDownloaderFrame, text='停止下载', command=self.StopDownloadBtn_Cmd, style='StopDownloadBtn.TButton')
        self.StopDownloadBtn.place(relx=0.894, rely=0.665, relwidth=0.092, relheight=0.122)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def CloseChromeBtn_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def AlyseBtn_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def OpenChromeBtn_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def ChoseFolderBtn_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def DownloadBtn_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def AddListBtn_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def DownloadListBtn_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def StopDownloadBtn_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
