from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)

        MainWindow.setStyleSheet("QMainWindow{\n"
                                "border-radius:15px\n"
                                "}\n"
                                "QWidget{\n"
                                "border-radius:15px;\n"
                                "}\n"
                                "#frame{\n"
                                "background: #e1e9ed;}\n"
                                "QToolButton{\n"
                                "background:#EAF7FF;\n"
                                "border-radius:15px;\n"
                                "}\n"
                                "QToolButton:hover{\n"
                                "background:#EAF7FF;\n"
                                "border-radius:15px;\n"
                                "background:#49ebff;\n"
                                "}\n"
                                "#label{\n"
                                "text-align:center;\n"
                                "}\n"
                                "#welcome{\n"
                                "text-align:center;\n"
                                "}\n"
                                "#toolButton_7\n"
                                "{\n"
                                "background:#e1e9ed;\n"
                                "}")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        #历史创作
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clientbutton = QtWidgets.QToolButton(self.centralwidget)
        self.clientbutton.setGeometry(QtCore.QRect(540, 220, 200, 120))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.clientbutton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./pictures/client.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clientbutton.setIcon(icon)
        self.clientbutton.setIconSize(QtCore.QSize(80, 80))
        self.clientbutton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.clientbutton.setObjectName("clientbutton")
        #开始创作
        self.roombutton = QtWidgets.QToolButton(self.centralwidget)
        self.roombutton.setGeometry(QtCore.QRect(60, 220, 200, 120))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.roombutton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./pictures/coffee.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.roombutton.setIcon(icon4)
        self.roombutton.setIconSize(QtCore.QSize(80, 80))
        self.roombutton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.roombutton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.roombutton.setObjectName("roombutton")
        #用户管理
        self.staffbutton = QtWidgets.QToolButton(self.centralwidget)
        self.staffbutton.setGeometry(QtCore.QRect(300, 220, 200, 120))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.staffbutton.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./pictures/staff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.staffbutton.setIcon(icon5)
        self.staffbutton.setIconSize(QtCore.QSize(80, 80))
        self.staffbutton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.staffbutton.setObjectName("staffbutton")

        self.chartbutton = QtWidgets.QToolButton(self.centralwidget)
        self.chartbutton.setGeometry(QtCore.QRect(300, 380, 200, 120))
        self.chartbutton.setMinimumSize(QtCore.QSize(200, 120))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.chartbutton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./pictures/chart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chartbutton.setIcon(icon1)
        self.chartbutton.setIconSize(QtCore.QSize(70, 70))
        self.chartbutton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.chartbutton.setObjectName("chartbutton")
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(540, 380, 200, 120))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_6.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./pictures/tobecontinued.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon2)
        self.toolButton_6.setIconSize(QtCore.QSize(70, 80))
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_6.setObjectName("toolButton_6")
        self.orderbutton = QtWidgets.QToolButton(self.centralwidget)
        self.orderbutton.setGeometry(QtCore.QRect(60, 380, 200, 120))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.orderbutton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./pictures/order.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.orderbutton.setIcon(icon3)
        self.orderbutton.setIconSize(QtCore.QSize(80, 80))
        self.orderbutton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.orderbutton.setObjectName("orderbutton")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 180))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.welcome = QtWidgets.QLabel(self.frame)
        self.welcome.setGeometry(QtCore.QRect(40, 10, 751, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.welcome.setFont(font)
        self.welcome.setText("")
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.setObjectName("welcome")

        self.toolButton_7 = QtWidgets.QToolButton(self.frame)
        self.toolButton_7.setGeometry(QtCore.QRect(370, 70, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButton_7.setFont(font)
        self.toolButton_7.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./pictures/hotel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon6)
        self.toolButton_7.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_7.setObjectName("toolButton_7")

        self.modifyPwd = QtWidgets.QToolButton(self.frame)
        self.modifyPwd.setGeometry(QtCore.QRect(710, 150, 81, 21))
        self.modifyPwd.setStyleSheet("background:#e1e9ed")
        self.modifyPwd.setObjectName("modifyPwd")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 540, 241, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 560, 241, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clientbutton.setText(_translate("MainWindow", "历史创作"))
        self.chartbutton.setText(_translate("MainWindow", "敬请期待"))
        self.toolButton_6.setText(_translate("MainWindow", "敬请期待"))
        self.orderbutton.setText(_translate("MainWindow", "敬请期待"))
        self.roombutton.setText(_translate("MainWindow", "开始创作"))
        self.staffbutton.setText(_translate("MainWindow", "用户管理"))
        self.modifyPwd.setText(_translate("MainWindow", "修改密码"))

        self.label.setText(_translate("MainWindow", "基于深度学习的油画创作系统-lcj"))
        self.label_2.setText(_translate("MainWindow", "version 1.0"))