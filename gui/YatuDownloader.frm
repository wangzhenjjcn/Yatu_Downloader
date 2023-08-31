VERSION 5.00
Begin VB.Form YatuDownloader 
   Caption         =   "Yatu视频下载"
   ClientHeight    =   10335
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   17355
   LinkTopic       =   "Form1"
   ScaleHeight     =   10335
   ScaleWidth      =   17355
   StartUpPosition =   3  '窗口缺省
   Begin VB.Frame ChromeFrame 
      Caption         =   "浏览器下载"
      Height          =   4935
      Left            =   120
      TabIndex        =   1
      Top             =   5280
      Width           =   17055
      Begin VB.CommandButton CloseChromeBtn 
         Caption         =   "关闭浏览器"
         Height          =   735
         Left            =   480
         TabIndex        =   8
         Top             =   2640
         Width           =   1815
      End
      Begin VB.ListBox LogList 
         Height          =   4200
         ItemData        =   "YatuDownloader.frx":0000
         Left            =   2760
         List            =   "YatuDownloader.frx":0002
         TabIndex        =   7
         Top             =   480
         Width           =   13695
      End
      Begin VB.CommandButton AlyseBtn 
         Caption         =   "分析当前页面"
         Height          =   735
         Left            =   480
         TabIndex        =   6
         Top             =   1560
         Width           =   1815
      End
      Begin VB.CommandButton OpenChromeBtn 
         Caption         =   "打开浏览器"
         Height          =   735
         Left            =   480
         TabIndex        =   5
         Top             =   480
         Width           =   1815
      End
   End
   Begin VB.Frame VideoDownloaderFrame 
      Caption         =   "视频下载"
      Height          =   5055
      Left            =   120
      TabIndex        =   0
      Top             =   120
      Width           =   17055
      Begin VB.CommandButton StopDownloadBtn 
         Caption         =   "停止下载"
         Height          =   615
         Left            =   15240
         TabIndex        =   16
         Top             =   3360
         Width           =   1575
      End
      Begin VB.CommandButton DownloadListBtn 
         Caption         =   "下载队列"
         Height          =   615
         Left            =   15240
         TabIndex        =   14
         Top             =   2640
         Width           =   1575
      End
      Begin VB.CommandButton AddListBtn 
         Caption         =   "添加到队列"
         Height          =   615
         Left            =   15240
         TabIndex        =   13
         Top             =   1920
         Width           =   1575
      End
      Begin VB.ListBox DownloadList 
         Height          =   2760
         ItemData        =   "YatuDownloader.frx":0004
         Left            =   1560
         List            =   "YatuDownloader.frx":0006
         TabIndex        =   12
         Top             =   1920
         Width           =   13455
      End
      Begin VB.CommandButton ChoseFolderBtn 
         Caption         =   "选择下载目录"
         Height          =   615
         Left            =   15240
         TabIndex        =   11
         Top             =   960
         Width           =   1575
      End
      Begin VB.CommandButton DownloadBtn 
         Caption         =   "下载视频"
         Height          =   615
         Left            =   15240
         TabIndex        =   4
         Top             =   240
         Width           =   1575
      End
      Begin VB.TextBox M3U8AdressText 
         Height          =   495
         Left            =   1560
         TabIndex        =   3
         Top             =   360
         Width           =   13455
      End
      Begin VB.Label Label3 
         Caption         =   "下载队列："
         Height          =   375
         Left            =   240
         TabIndex        =   15
         Top             =   1920
         Width           =   975
      End
      Begin VB.Label DownloadFolderLabel 
         Caption         =   "尚未初始化"
         Height          =   375
         Left            =   1560
         TabIndex        =   10
         Top             =   1200
         Width           =   13335
      End
      Begin VB.Label Label2 
         Caption         =   "下载目录："
         Height          =   375
         Left            =   240
         TabIndex        =   9
         Top             =   1200
         Width           =   975
      End
      Begin VB.Label Label1 
         Caption         =   "M3U8地址："
         Height          =   255
         Left            =   240
         TabIndex        =   2
         Top             =   480
         Width           =   975
      End
   End
End
Attribute VB_Name = "YatuDownloader"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Label4_Click()

End Sub
