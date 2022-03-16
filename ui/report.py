# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QScrollBar, QScrollArea, QWidget, QGridLayout, QVBoxLayout


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 599)
        MainWindow.setStyleSheet("QListWidget, QListView, QTreeWidget, QTreeView,QFrame {\n"
                                "    outline: 0px;\n"
                                "}\n"
                                "/*设置左侧选项的最小最大宽度,文字颜色和背景颜色*/\n"
                                "#listWidget {\n"
                                "    min-width: 200px;\n"
                                "    max-width: 200px;\n"
                                "    color: white;\n"
                                "    background-color:#2f4050\n"
                                "}\n"
                                "#head\n"
                                "{\n"
                                "background:white;\n"
                                "border-radius:30px;\n"
                                "}\n"
                                "#head_2\n"
                                "{\n"
                                "background:#CCFFCC;\n"
                                "border:1px solid;\n"
                                "border-color:#CCFFCC;\n"
                                "border-radius:60px;\n"
                                "}\n"
                                "#Search\n"
                                "{\n"
                                "border-radius:5px;\n"
                                "background:#293846;\n"
                                "border:0.5px solid;\n"
                                "border-color:white;\n"
                                "\n"
                                "}\n"
                                "#listWidget::item\n"
                                "{\n"
                                "height:60;\n"
                                "background-color:#293846;\n"
                                "}\n"
                                "#frame\n"
                                "{\n"
                                "background-color:#2f4050\n"
                                "\n"
                                "}\n"
                                "/*被选中时的背景颜色和左边框颜色*/\n"
                                "#listWidget::item:selected {\n"
                                "    background: rgb(52, 52, 52);\n"
                                "    border-left: 2px solid rgb(9, 187, 7);\n"
                                "}\n"
                                "/*鼠标悬停颜色*/\n"
                                "HistoryPanel::item:hover {\n"
                                "    background: rgb(52, 52, 52);\n"
                                "}\n"
                                "/*右侧的层叠窗口的背景颜色*/\n"
                                "QStackedWidget {\n"
                                "    background: white;\n"
                                "}\n"
                                "/*模拟的页面*/\n"
                                "#frame > QLabel\n"
                                "{\n"
                                "color:white;\n"
                                "}\n"
                                "#frame_2\n"
                                "{\n"
                                "background-color:#CCFFCC;\n"
                                "}\n"
                                "#page_2 > QLineEdit\n"
                                "{\n"
                                "border-radius:5px;\n"
                                "background:#FFFFFF;\n"
                                "border:1px solid;\n"
                                "border-color:#6699CC;\n"
                                "}\n"
                                "QLineEdit\n"
                                "{\n"
                                "border-radius:5px;\n"
                                "background:#FFFFFF;\n"
                                "border:1px solid;\n"
                                "border-color:#6699CC;\n"
                                "}\n"
                                "QComboBox,QDateEdit\n"
                                "{\n"
                                "border-radius:5px;\n"
                                "background:#FFFFFF;\n"
                                "border:1px solid;\n"
                                "border-color:#6699CC;\n"
                                "}\n"
                                "#listWidget_2,#listWidget_3,#listWidget_4\n"
                                "{\n"
                                "background-color:#CCFFFF;\n"
                                "border:1px solid black\n"
                                "}\n"
                                "\n"
                                "\n"
                                "\n"
                                "")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 200, 204, 400))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./pictures/customer2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.listWidget.addItem(item)

        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./pictures/customer1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 204, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.head = QtWidgets.QToolButton(self.frame)
        self.head.setGeometry(QtCore.QRect(60, 20, 60, 60))
        self.head.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./pictures/staff3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.head.setIcon(icon2)
        self.head.setIconSize(QtCore.QSize(60, 60))
        self.head.setObjectName("head")
        self.welcome = QtWidgets.QLabel(self.frame)
        self.welcome.setGeometry(QtCore.QRect(30, 90, 110, 20))
        self.welcome.setText("")
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.setObjectName("welcome")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Search = QtWidgets.QLineEdit(self.frame)
        self.Search.setGeometry(QtCore.QRect(20, 170, 145, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(7)
        self.Search.setFont(font)
        self.Search.setStyleSheet("")
        self.Search.setObjectName("Search")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(170, 170, 21, 20))
        self.toolButton.setStyleSheet("background-color:#2f4050;\n"
                                        "border:0px;\n"
                                        "\n"
                                        "border-radius:5px")
        self.toolButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./pictures/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon3)
        self.toolButton.setIconSize(QtCore.QSize(15, 15))
        self.toolButton.setObjectName("toolButton")

        self.role = QtWidgets.QLabel(self.frame)
        self.role.setGeometry(QtCore.QRect(30, 120, 110, 15))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.role.setFont(font)
        self.role.setText("")
        self.role.setAlignment(QtCore.Qt.AlignCenter)
        self.role.setObjectName("role")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 560, 241, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 540, 241, 41))

        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(210, 0, 591, 591))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.toolButton_2 = QtWidgets.QToolButton(self.page)
        self.toolButton_2.setGeometry(QtCore.QRect(10, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet("border:none")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./pictures/search1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon4)
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.page)
        self.formLayoutWidget.setGeometry(QtCore.QRect(330, 86, 201, 431))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.tosql1 = QtWidgets.QToolButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.tosql1.setFont(font)
        self.tosql1.setStyleSheet("background-color:#CCFFFF")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./pictures/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tosql1.setIcon(icon5)
        self.tosql1.setIconSize(QtCore.QSize(80, 80))
        self.tosql1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tosql1.setObjectName("tosql1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tosql1)
        self.tosql2 = QtWidgets.QToolButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.tosql2.setFont(font)
        self.tosql2.setStyleSheet("background-color:#CCFFFF")
        self.tosql2.setIcon(icon5)
        self.tosql2.setIconSize(QtCore.QSize(70, 80))
        self.tosql2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tosql2.setObjectName("tosql2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tosql2)
        self.toexcel = QtWidgets.QToolButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.toexcel.setFont(font)
        self.toexcel.setStyleSheet("background-color:#CCFFFF")
        self.toexcel.setIcon(icon5)
        self.toexcel.setIconSize(QtCore.QSize(80, 80))
        self.toexcel.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toexcel.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toexcel.setObjectName("toexcel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.toexcel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.line_2 = QtWidgets.QFrame(self.page)
        self.line_2.setGeometry(QtCore.QRect(-10, 356, 601, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.page)
        self.line_3.setGeometry(QtCore.QRect(-10, 20, 591, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.page)
        self.line_4.setGeometry(QtCore.QRect(-10, 506, 601, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line = QtWidgets.QFrame(self.page)
        self.line.setGeometry(QtCore.QRect(0, 206, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(270, 560, 241, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(200, 540, 241, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.path1 = QtWidgets.QLineEdit(self.page)
        self.path1.setGeometry(QtCore.QRect(110, 136, 181, 31))
        self.path1.setStyleSheet("border-radius:10px;\n"
                                "background:#FFFFFF;\n"
                                "border:1px solid;\n"
                                "border-color:#CCCCFF;\n"
                                "")
        self.path1.setObjectName("path1")
        self.label_30 = QtWidgets.QLabel(self.page)
        self.label_30.setGeometry(QtCore.QRect(20, 130, 81, 40))
        self.label_30.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_30.setObjectName("label_30")
        self.scan = QtWidgets.QPushButton(self.page)
        self.scan.setGeometry(QtCore.QRect(130, 180, 93, 28))
        self.scan.setStyleSheet("#scan{background:white\n"
                                ";\n"
                                "border:1px solid black;\n"
                                "border-radius:8px}\n"
                                "#scan:hover\n"
                                "{\n"
                                "background:#CCFF99\n"
                                "}")
        self.scan.setObjectName("scan")
        self.label_31 = QtWidgets.QLabel(self.page)
        self.label_31.setGeometry(QtCore.QRect(20, 270, 81, 40))
        self.label_31.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_31.setObjectName("label_31")
        self.scan_2 = QtWidgets.QPushButton(self.page)
        self.scan_2.setGeometry(QtCore.QRect(130, 316, 93, 28))
        self.scan_2.setStyleSheet("#scan_2{background:white\n"
                                ";\n"
                                "border:1px solid black;\n"
                                "border-radius:8px}\n"
                                "#scan_2:hover\n"
                                "{\n"
                                "background:#CCFF99\n"
                                "}")
        self.scan_2.setObjectName("scan_2")
        self.path2 = QtWidgets.QLineEdit(self.page)
        self.path2.setGeometry(QtCore.QRect(110, 276, 181, 31))
        self.path2.setStyleSheet("border-radius:10px;\n"
                                "background:#FFFFFF;\n"
                                "border:1px solid;\n"
                                "border-color:#CCCCFF;\n"
                                "")
        self.path2.setObjectName("path2")
        self.label_32 = QtWidgets.QLabel(self.page)
        self.label_32.setGeometry(QtCore.QRect(20, 420, 81, 40))
        self.label_32.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_32.setObjectName("label_32")
        self.scan_3 = QtWidgets.QPushButton(self.page)
        self.scan_3.setGeometry(QtCore.QRect(130, 466, 93, 28))
        self.scan_3.setStyleSheet("#scan_3{background:white\n"
                                ";\n"
                                "border:1px solid black;\n"
                                "border-radius:8px}\n"
                                "#scan_3:hover\n"
                                "{\n"
                                "background:#CCFF99\n"
                                "}")
        self.scan_3.setObjectName("scan_3")
        self.path3 = QtWidgets.QLineEdit(self.page)
        self.path3.setGeometry(QtCore.QRect(110, 426, 181, 31))
        self.path3.setStyleSheet("border-radius:10px;\n"
                                "background:#FFFFFF;\n"
                                "border:1px solid;\n"
                                "border-color:#CCCCFF;\n"
                                "")
        self.path3.setObjectName("path3")
        self.label_33 = QtWidgets.QLabel(self.page)
        self.label_33.setGeometry(QtCore.QRect(20, 231, 81, 40))
        self.label_33.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.page)
        self.label_34.setGeometry(QtCore.QRect(20, 386, 81, 40))
        self.label_34.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_34.setObjectName("label_34")
        self.ask = QtWidgets.QToolButton(self.page)
        self.ask.setGeometry(QtCore.QRect(0, 40, 101, 21))
        self.ask.setStyleSheet("border:none")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./pictures/ask.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ask.setIcon(icon6)
        self.ask.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.ask.setObjectName("ask")
        self.name1 = QtWidgets.QComboBox(self.page)
        self.name1.setGeometry(QtCore.QRect(110, 240, 181, 22))
        self.name1.setStyleSheet("border-radius:10px;\n"
                                "background:#FFFFFF;\n"
                                "border:1px solid;\n"
                                "border-color:#CCCCFF;")
        self.name1.setObjectName("name1")
        self.name1.addItem("")
        self.name1.addItem("")
        self.name1.addItem("")
        self.name1.addItem("")
        self.name1.addItem("")
        self.name1.addItem("")
        self.name1.addItem("")
        self.name1.addItem("")
        self.name1.addItem("")
        self.name1.addItem("")
        self.name2 = QtWidgets.QComboBox(self.page)
        self.name2.setGeometry(QtCore.QRect(110, 395, 181, 22))
        self.name2.setStyleSheet("border-radius:10px;\n"
                                "background:#FFFFFF;\n"
                                "border:1px solid;\n"
                                "border-color:#CCCCFF;")
        self.name2.setObjectName("name2")
        self.name2.addItem("")
        self.name2.addItem("")
        self.name2.addItem("")
        self.name2.addItem("")
        self.name2.addItem("")
        self.name2.addItem("")
        self.name2.addItem("")
        self.name2.addItem("")
        self.name2.addItem("")
        self.name2.addItem("")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.line_5 = QtWidgets.QFrame(self.page_2)
        self.line_5.setGeometry(QtCore.QRect(0, 20, 591, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.toolButton_3 = QtWidgets.QToolButton(self.page_2)
        self.toolButton_3.setGeometry(QtCore.QRect(10, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setStyleSheet("border:none")
        self.toolButton_3.setIcon(icon4)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_3.setObjectName("toolButton_3")

        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_2)
        self.stackedWidget_2.setGeometry(QtCore.QRect(0, 0,600,800))
        self.stackedWidget_2.setObjectName("stackedWidget_2")


        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        #查看按钮
        self.showfigure1 = QtWidgets.QPushButton(self.page_3)
        self.showfigure1.setGeometry(QtCore.QRect(460, 10, 93, 28))
        self.showfigure1.setStyleSheet("#showfigure1{background:white\n"
                                        ";\n"
                                        "border:1px solid black;\n"
                                        "border-radius:8px}\n"
                                        "#showfigure1:hover\n"
                                        "{\n"
                                        "background:#CCFF99\n"
                                        "}")
        self.showfigure1.setObjectName("showfigure1")
        #作品显示部分
        self.groupBox = QtWidgets.QGroupBox(self.page_3)
        self.groupBox.setGeometry(QtCore.QRect(-10,40,800,800))
        self.groupBox.setObjectName("groupBox")

        #设置滚轮
        self.scroll_ares_images = QScrollArea(self.groupBox)
        self.scroll_ares_images.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget(self.page_3)
        self.scrollAreaWidgetContents.setObjectName('scrollAreaWidgetContends')

        # 进行网络布局
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scroll_ares_images.setWidget(self.scrollAreaWidgetContents)
        self.scroll_ares_images.setGeometry(20,20,600,500)
        self.vertocal1 = QVBoxLayout()
        self.vertocal1.addWidget(self.scroll_ares_images)

        #设置图片的预览尺寸；
        self.displayed_image_size = 200
        self.col =0
        self.row =0
        self.initial_path =None

        self.stackedWidget_2.addWidget(self.page_3)
        self.stackedWidget.addWidget(self.page_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "  数据库备份"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "  历史创作"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "*表示需要最高权限"))
        self.Search.setPlaceholderText(_translate("MainWindow", "搜索"))
        self.label_3.setText(_translate("MainWindow", "version 1.0"))
        self.label.setText(_translate("MainWindow", "基于深度学习的油画创作系统-lcj"))
        self.toolButton_2.setText(_translate("MainWindow", "数据库备份"))
        self.tosql1.setText(_translate("MainWindow", "导出数据库（.sql）"))
        self.tosql2.setText(_translate("MainWindow", "导出数据表（.sql）"))
        self.toexcel.setText(_translate("MainWindow", "导入数据表（.csv）"))
        self.label_4.setText(_translate("MainWindow", "version 1.0"))
        self.label_5.setText(_translate("MainWindow", "基于深度学习的油画创作系统-lcj"))
        self.path1.setPlaceholderText(_translate("MainWindow", "导出路径"))
        self.label_30.setText(_translate("MainWindow", "导出路径："))
        self.scan.setText(_translate("MainWindow", "浏览"))
        self.label_31.setText(_translate("MainWindow", "导出路径："))
        self.scan_2.setText(_translate("MainWindow", "浏览"))
        self.path2.setPlaceholderText(_translate("MainWindow", "导出路径"))
        self.label_32.setText(_translate("MainWindow", "导出路径："))
        self.scan_3.setText(_translate("MainWindow", "浏览"))
        self.path3.setPlaceholderText(_translate("MainWindow", "导出路径"))
        self.label_33.setText(_translate("MainWindow", "表名："))
        self.label_34.setText(_translate("MainWindow", "表名："))
        self.ask.setText(_translate("MainWindow", "关于表名"))
        #
        self.name1.setItemText(0, _translate("MainWindow", "请选择..."))
        self.name1.setItemText(4, _translate("MainWindow", "staff"))

        self.name2.setItemText(0, _translate("MainWindow", "请选择..."))
        self.name2.setItemText(4, _translate("MainWindow", "staff"))
        self.toolButton_3.setText(_translate("MainWindow", "历史信息"))

        self.showfigure1.setText(_translate("MainWindow", "查看作品"))
        self.groupBox.setTitle(_translate("MainWindow", "作品"))

