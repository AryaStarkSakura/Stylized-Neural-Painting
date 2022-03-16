from PyQt5.QtWidgets import QMainWindow
from ui.MainUI import Ui_MainWindow
from service import globalValue
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import time

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.staff = globalValue.get_staff()
        print(self.staff.sname[0])
        self.welcome.setText(self.staff.sname + ',你好。欢迎使用本系统'+'。今天是' + time.strftime("%Y-%m-%d", time.localtime()))
        self.staffbutton.clicked.connect(self.gotoStaff)
        self.roombutton.clicked.connect(self.creation)
        self.clientbutton.clicked.connect(self.history)
        self.orderbutton.clicked.connect(self.gotoOrder)
        self.chartbutton.clicked.connect(self.gotoChart)
        self.modifyPwd.clicked.connect(self.modifyPasswd)
    #修改密码
    def modifyPasswd(self):
        print("123")
        from service.modifyPwd import mpWindow
        self.mpWindow = mpWindow()
        self.close()
        self.mpWindow.show()
    #开始创作
    def creation(self):
        from service.MainMenu import Ui_MainWindow
        self.Ui_MainWindow = Ui_MainWindow()
        #self.close()
        self.Ui_MainWindow.show()
    #用户管理
    def gotoStaff(self):
        from service.staffOp import StaffOP
        self.StaffOP = StaffOP()
        self.StaffOP.show()
    #历史创作
    def history(self):
        #from service.clientOp import ClientOp
        #self.ClientOp = ClientOp()
        #self.ClientOp.show()
        from service.chartOp import ChartOp
        self.ChartOp = ChartOp()
        self.ChartOp.show()
    #敬请期待中
    def gotoChart(self):
        print("123")

    #敬请期待左
    def gotoOrder(self):
        print("123")
        #from service.orderOp import OrderOp
        #self.OrderOp = OrderOp()
        #self.OrderOp.show()




