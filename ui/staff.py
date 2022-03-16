# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staff.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QListWidget, QListView, QTreeWidget, QTreeView,QFrame {\n"
                                "    outline: 0px;\n"
                                "}\n"
                                "/*设置左侧选项的最小最大宽度,文字颜色和背景颜色*/\n"
                                "QListWidget {\n"
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
                                "QListWidget::item\n"
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
                                "QListWidget::item:selected {\n"
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
                                "#page_2 > QLineEdit,QDateEdit\n"
                                "{\n"
                                "border-radius:5px;\n"
                                "background:#FFFFFF;\n"
                                "border:1px solid;\n"
                                "border-color:#6699CC;\n"
                                "}\n"
                                "#page_4 > QLineEdit\n"
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
                                "\n"
                                "\n"
                                "")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(190, 0, 611, 601))
        self.stackedWidget.setStyleSheet("background-color:#FFFFFF\n"
                                        "")
        self.stackedWidget.setObjectName("stackedWidget")

        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.split = QtWidgets.QFrame(self.page)
        self.split.setGeometry(QtCore.QRect(10, 210, 600, 2))
        self.split.setStyleSheet("color:#CCFFCC;\n"
                                "border-color:#CCFFCC;\n"
                                "background-color:#CCFFCC")
        self.split.setFrameShape(QtWidgets.QFrame.HLine)
        self.split.setFrameShadow(QtWidgets.QFrame.Raised)
        self.split.setObjectName("split")

        self.head_2 = QtWidgets.QToolButton(self.page)
        self.head_2.setGeometry(QtCore.QRect(260, 30, 121, 121))
        self.head_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./pictures/staff3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.head_2.setIcon(icon)
        self.head_2.setIconSize(QtCore.QSize(100, 100))
        self.head_2.setObjectName("head_2")
        self.name = QtWidgets.QLabel(self.page)
        self.name.setGeometry(QtCore.QRect(260, 160, 131, 31))

        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(190, 240, 61, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(190, 290, 51, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(190, 340, 71, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(190, 390, 61, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(190, 440, 71, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(190, 490, 81, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.sname = QtWidgets.QLabel(self.page)
        self.sname.setGeometry(QtCore.QRect(300, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.sname.setFont(font)
        self.sname.setObjectName("sname")

        self.ssex = QtWidgets.QLabel(self.page)
        self.ssex.setGeometry(QtCore.QRect(300, 300, 81, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.ssex.setFont(font)
        self.ssex.setObjectName("ssex")

        self.stime = QtWidgets.QLabel(self.page)
        self.stime.setGeometry(QtCore.QRect(300, 350, 91, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.stime.setFont(font)
        self.stime.setObjectName("stime")

        self.srole = QtWidgets.QLabel(self.page)
        self.srole.setGeometry(QtCore.QRect(300, 400, 81, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.srole.setFont(font)
        self.srole.setObjectName("srole")

        self.sphone = QtWidgets.QLabel(self.page)
        self.sphone.setGeometry(QtCore.QRect(300, 450, 141, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.sphone.setFont(font)
        self.sphone.setObjectName("sphone")

        self.sidcard = QtWidgets.QLabel(self.page)
        self.sidcard.setGeometry(QtCore.QRect(300, 500, 181, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.sidcard.setFont(font)
        self.sidcard.setObjectName("sidcard")

        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(190, 540, 81, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.sidcard_2 = QtWidgets.QLabel(self.page)
        self.sidcard_2.setGeometry(QtCore.QRect(300, 550, 181, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.sidcard_2.setFont(font)
        self.sidcard_2.setObjectName("sidcard_2")

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")

        self.searchTable = QtWidgets.QTableWidget(self.page_3)
        self.searchTable.setGeometry(QtCore.QRect(0, 240, 611, 361))
        self.searchTable.setStyleSheet("")
        self.searchTable.setObjectName("searchTable")
        self.searchTable.setColumnCount(9)
        self.searchTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(8, item)

        self.frame_2 = QtWidgets.QFrame(self.page_3)
        self.frame_2.setGeometry(QtCore.QRect(10, 30, 611, 211))
        self.frame_2.setStyleSheet("background-color:rgb(255, 249, 246)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.searchName = QtWidgets.QLineEdit(self.frame_2)
        self.searchName.setGeometry(QtCore.QRect(170, 40, 181, 41))
        self.searchName.setStyleSheet("border-radius:10px;\n"
                                        "background:#FFFFFF;\n"
                                        "border:1px solid;\n"
                                        "border-color:#CCCCFF;\n"
                                        "")
        self.searchName.setObjectName("searchName")

        self.searchNB = QtWidgets.QToolButton(self.frame_2)
        self.searchNB.setGeometry(QtCore.QRect(370, 40, 101, 41))
        self.searchNB.setStyleSheet("background-color:rgb(255, 249, 246);\n"
                                "border:0px;\n"
                                "\n"
                                "border-radius:5px")
        self.searchNB.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./pictures/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchNB.setIcon(icon1)
        self.searchNB.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.searchNB.setObjectName("searchNB")

        self.label_74 = QtWidgets.QLabel(self.frame_2)
        self.label_74.setGeometry(QtCore.QRect(310, 149, 151, 40))
        self.label_74.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_74.setObjectName("label_74")

        self.modifyvalue = QtWidgets.QLineEdit(self.frame_2)
        self.modifyvalue.setGeometry(QtCore.QRect(430, 160, 111, 21))
        self.modifyvalue.setStyleSheet("border-radius:5px")
        self.modifyvalue.setText("")
        self.modifyvalue.setObjectName("modifyvalue")

        self.commitTableModify = QtWidgets.QPushButton(self.frame_2)
        self.commitTableModify.setGeometry(QtCore.QRect(170, 155, 121, 31))
        self.commitTableModify.setStyleSheet("#commitTableModify{background:#CCFFCC;\n"
                                        "border-radius:8px}\n"
                                        "#commitTableModify:hover\n"
                                        "{\n"
                                        "background:#CCFF99\n"
                                        "}")
        self.commitTableModify.setObjectName("commitTableModify")

        self.label_78 = QtWidgets.QLabel(self.frame_2)
        self.label_78.setGeometry(QtCore.QRect(360, 10, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")

        self.commitTableDel = QtWidgets.QPushButton(self.frame_2)
        self.commitTableDel.setGeometry(QtCore.QRect(170, 110, 121, 31))
        self.commitTableDel.setStyleSheet("#commitTableDel{background:#CCFFCC;\n"
                                        "border-radius:8px}\n"
                                        "#commitTableDel:hover\n"
                                        "{\n"
                                        "background:#CCFF99\n"
                                        "}")
        self.commitTableDel.setObjectName("commitTableDel")

        self.split_3 = QtWidgets.QFrame(self.page_3)
        self.split_3.setGeometry(QtCore.QRect(10, 30, 600, 2))
        self.split_3.setStyleSheet("color:#CCFFCC;\n"
                                "border-color:#CCFFCC;\n"
                                "background-color:#CCFFCC")
        self.split_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.split_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.split_3.setObjectName("split_3")

        self.toolButton_2 = QtWidgets.QToolButton(self.page_3)
        self.toolButton_2.setGeometry(QtCore.QRect(20, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet("border:none")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./pictures/search1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_2.setObjectName("toolButton_2")

        self.line = QtWidgets.QFrame(self.page_3)
        self.line.setGeometry(QtCore.QRect(10, 230, 601, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.stackedWidget.addWidget(self.page_3)

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")

        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(100, 60, 101, 40))
        self.label_9.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_9.setObjectName("label_9")

        self.split_2 = QtWidgets.QFrame(self.page_2)
        self.split_2.setGeometry(QtCore.QRect(10, 30, 600, 2))
        self.split_2.setStyleSheet("color:#CCFFCC;\n"
                                "border-color:#CCFFCC;\n"
                                "background-color:#CCFFCC")
        self.split_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.split_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.split_2.setObjectName("split_2")

        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(100, 260, 101, 41))
        self.label_10.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(100, 110, 101, 41))
        self.label_11.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setGeometry(QtCore.QRect(100, 310, 101, 41))
        self.label_12.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.page_2)
        self.label_13.setGeometry(QtCore.QRect(100, 160, 101, 41))
        self.label_13.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_13.setObjectName("label_13")

        self.label_14 = QtWidgets.QLabel(self.page_2)
        self.label_14.setGeometry(QtCore.QRect(100, 360, 101, 41))
        self.label_14.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_14.setObjectName("label_14")

        self.label_15 = QtWidgets.QLabel(self.page_2)
        self.label_15.setGeometry(QtCore.QRect(100, 210, 101, 41))
        self.label_15.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_15.setObjectName("label_15")

        self.label_16 = QtWidgets.QLabel(self.page_2)
        self.label_16.setGeometry(QtCore.QRect(100, 410, 101, 41))
        self.label_16.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_16.setObjectName("label_16")

        self.label_17 = QtWidgets.QLabel(self.page_2)
        self.label_17.setGeometry(QtCore.QRect(100, 460, 101, 41))
        self.label_17.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_17.setObjectName("label_17")

        self.inputsid = QtWidgets.QLineEdit(self.page_2)
        self.inputsid.setGeometry(QtCore.QRect(220, 70, 221, 21))
        self.inputsid.setObjectName("inputsid")

        self.inputname = QtWidgets.QLineEdit(self.page_2)
        self.inputname.setGeometry(QtCore.QRect(220, 120, 221, 21))
        self.inputname.setObjectName("inputname")

        self.inputuser = QtWidgets.QLineEdit(self.page_2)
        self.inputuser.setGeometry(QtCore.QRect(220, 270, 221, 21))
        self.inputuser.setObjectName("inputuser")

        self.inputpwd = QtWidgets.QLineEdit(self.page_2)
        self.inputpwd.setGeometry(QtCore.QRect(220, 320, 221, 21))
        self.inputpwd.setObjectName("inputpwd")

        self.inputrole = QtWidgets.QLineEdit(self.page_2)
        self.inputrole.setGeometry(QtCore.QRect(220, 370, 221, 21))
        self.inputrole.setObjectName("inputrole")

        self.inputidcard = QtWidgets.QLineEdit(self.page_2)
        self.inputidcard.setGeometry(QtCore.QRect(220, 420, 221, 21))
        self.inputidcard.setObjectName("inputidcard")

        self.inputphone = QtWidgets.QLineEdit(self.page_2)
        self.inputphone.setGeometry(QtCore.QRect(220, 470, 221, 21))
        self.inputphone.setObjectName("inputphone")

        self.toolButton_3 = QtWidgets.QToolButton(self.page_2)
        self.toolButton_3.setGeometry(QtCore.QRect(20, 0, 111, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setStyleSheet("border:none\n"
                                        "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./pictures/insert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon3)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_3.setObjectName("toolButton_3")

        self.commitAdd = QtWidgets.QPushButton(self.page_2)
        self.commitAdd.setGeometry(QtCore.QRect(200, 530, 211, 31))
        self.commitAdd.setStyleSheet("#commitAdd{background:#CCFFCC;\n"
                                "border-radius:8px}\n"
                                "#commitAdd:hover\n"
                                "{\n"
                                "background:#CCFF99\n"
                                "}")
        self.commitAdd.setObjectName("commitAdd")

        self.inputdate = QtWidgets.QDateEdit(self.page_2)
        self.inputdate.setGeometry(QtCore.QRect(220, 220, 221, 22))
        self.inputdate.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.inputdate.setObjectName("inputdate")

        self.inputfemale = QtWidgets.QRadioButton(self.page_2)
        self.inputfemale.setGeometry(QtCore.QRect(320, 170, 115, 19))
        self.inputfemale.setObjectName("inputfemale")

        self.inputmale = QtWidgets.QRadioButton(self.page_2)
        self.inputmale.setGeometry(QtCore.QRect(220, 170, 81, 19))
        self.inputmale.setObjectName("inputmale")

        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.split_4 = QtWidgets.QFrame(self.page_4)
        self.split_4.setGeometry(QtCore.QRect(10, 30, 600, 2))
        self.split_4.setStyleSheet("color:#CCFFCC;\n"
                                "border-color:#CCFFCC;\n"
                                "background-color:#CCFFCC")
        self.split_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.split_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.split_4.setObjectName("split_4")

        self.toolButton_4 = QtWidgets.QToolButton(self.page_4)
        self.toolButton_4.setGeometry(QtCore.QRect(20, 0, 111, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setStyleSheet("border:none\n"
                                        "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./pictures/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon4)
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_4.setObjectName("toolButton_4")

        self.deleteTable = QtWidgets.QTableWidget(self.page_4)
        self.deleteTable.setGeometry(QtCore.QRect(10, 260, 601, 341))
        self.deleteTable.setStyleSheet("")
        self.deleteTable.setObjectName("deleteTable")
        self.deleteTable.setColumnCount(9)
        self.deleteTable.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.deleteTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.deleteTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.deleteTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.deleteTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.deleteTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.deleteTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.deleteTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.deleteTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.deleteTable.setHorizontalHeaderItem(8, item)
        self.desid = QtWidgets.QLineEdit(self.page_4)
        self.desid.setGeometry(QtCore.QRect(250, 90, 221, 21))
        self.desid.setObjectName("desid")

        self.label_18 = QtWidgets.QLabel(self.page_4)
        self.label_18.setGeometry(QtCore.QRect(150, 80, 91, 40))
        self.label_18.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_18.setObjectName("label_18")

        self.dename = QtWidgets.QLineEdit(self.page_4)
        self.dename.setGeometry(QtCore.QRect(250, 130, 221, 21))
        self.dename.setObjectName("dename")
        self.label_19 = QtWidgets.QLabel(self.page_4)
        self.label_19.setGeometry(QtCore.QRect(150, 120, 91, 41))
        self.label_19.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_19.setObjectName("label_19")

        self.deidcard = QtWidgets.QLineEdit(self.page_4)
        self.deidcard.setGeometry(QtCore.QRect(250, 170, 221, 21))
        self.deidcard.setObjectName("deidcard")

        self.label_20 = QtWidgets.QLabel(self.page_4)
        self.label_20.setGeometry(QtCore.QRect(150, 160, 81, 41))
        self.label_20.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_20.setObjectName("label_20")

        self.commitDe = QtWidgets.QPushButton(self.page_4)
        self.commitDe.setGeometry(QtCore.QRect(240, 210, 93, 28))
        self.commitDe.setStyleSheet("#commitDe{background:#CCFFCC;\n"
                                "border-radius:8px}\n"
                                "#commitDe:hover\n"
                                "{\n"
                                "background:#CCFF99\n"
                                "}")
        self.commitDe.setObjectName("commitDe")

        self.label_21 = QtWidgets.QLabel(self.page_4)
        self.label_21.setGeometry(QtCore.QRect(210, 35, 211, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")

        self.stackedWidget.addWidget(self.page_4)

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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./pictures/staff5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./pictures/staff2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./pictures/staff4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon7)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setIcon(icon5)
        self.listWidget.addItem(item)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 204, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.head = QtWidgets.QToolButton(self.frame)
        self.head.setGeometry(QtCore.QRect(60, 20, 60, 60))
        self.head.setText("")
        self.head.setIcon(icon)
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
        self.toolButton.setIcon(icon1)
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "csa "))
        self.label.setText(_translate("MainWindow", "姓名："))
        self.label_3.setText(_translate("MainWindow", "性别："))
        self.label_4.setText(_translate("MainWindow", "申请时间："))
        self.label_5.setText(_translate("MainWindow", "权限："))
        self.label_6.setText(_translate("MainWindow", "手机号："))
        self.label_7.setText(_translate("MainWindow", "身份证号："))
        self.sname.setText(_translate("MainWindow", "邵嘉毅"))
        self.ssex.setText(_translate("MainWindow", "男"))
        self.stime.setText(_translate("MainWindow", "2019-12-12"))
        self.srole.setText(_translate("MainWindow", "1"))
        self.sphone.setText(_translate("MainWindow", "2332121323"))
        self.sidcard.setText(_translate("MainWindow", "1111111111111111111"))
        self.label_8.setText(_translate("MainWindow", "用户号："))
        self.sidcard_2.setText(_translate("MainWindow", "1"))
        item = self.searchTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "用户编号"))
        item = self.searchTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.searchTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "性别"))
        item = self.searchTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "登记申请时间"))
        item = self.searchTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "账户名"))
        item = self.searchTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "密码"))
        item = self.searchTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "权限"))
        item = self.searchTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "身份证号"))
        item = self.searchTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "手机号"))
        self.searchName.setPlaceholderText(_translate("MainWindow", "搜索用户姓名"))
        self.label_74.setText(_translate("MainWindow", "选中部分修改为："))
        self.modifyvalue.setPlaceholderText(_translate("MainWindow", "修改值"))
        self.commitTableModify.setText(_translate("MainWindow", "确认修改"))
        self.label_78.setText(_translate("MainWindow", "*选中表格内可以进行修改和删除操作"))
        self.commitTableDel.setText(_translate("MainWindow", "确认删除"))
        self.toolButton_2.setText(_translate("MainWindow", "查询用户"))
        self.label_9.setText(_translate("MainWindow", "用户编号："))
        self.label_10.setText(_translate("MainWindow", "账户名："))
        self.label_11.setText(_translate("MainWindow", "用户姓名："))
        self.label_12.setText(_translate("MainWindow", "密码:"))
        self.label_13.setText(_translate("MainWindow", "用户性别："))
        self.label_14.setText(_translate("MainWindow", "权限："))
        self.label_15.setText(_translate("MainWindow", "登记入职时间："))
        self.label_16.setText(_translate("MainWindow", "身份证："))
        self.label_17.setText(_translate("MainWindow", "手机号："))
        self.inputsid.setPlaceholderText(_translate("MainWindow", "编号"))
        self.inputname.setPlaceholderText(_translate("MainWindow", "姓名"))
        self.inputuser.setPlaceholderText(_translate("MainWindow", "账号名"))
        self.inputpwd.setPlaceholderText(_translate("MainWindow", "密码"))
        self.inputrole.setPlaceholderText(_translate("MainWindow", "权限"))
        self.inputidcard.setPlaceholderText(_translate("MainWindow", "身份证"))
        self.inputphone.setPlaceholderText(_translate("MainWindow", "手机号"))
        self.toolButton_3.setText(_translate("MainWindow", "增添用户"))
        self.commitAdd.setText(_translate("MainWindow", "确认录入"))
        self.inputfemale.setText(_translate("MainWindow", "女"))
        self.inputmale.setText(_translate("MainWindow", "男"))
        self.toolButton_4.setText(_translate("MainWindow", "删除用户"))
        item = self.deleteTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "用户编号"))
        item = self.deleteTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.deleteTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "性别"))
        item = self.deleteTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "登记入职时间"))
        item = self.deleteTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "账户名"))
        item = self.deleteTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "密码"))
        item = self.deleteTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "权限"))
        item = self.deleteTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "身份证号"))
        item = self.deleteTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "手机号"))
        self.desid.setPlaceholderText(_translate("MainWindow", "编号"))
        self.label_18.setText(_translate("MainWindow", "用户编号："))
        self.dename.setPlaceholderText(_translate("MainWindow", "姓名"))
        self.label_19.setText(_translate("MainWindow", "用户姓名："))
        self.deidcard.setPlaceholderText(_translate("MainWindow", "身份证"))
        self.label_20.setText(_translate("MainWindow", "身份证："))
        self.commitDe.setText(_translate("MainWindow", "确认删除"))
        self.label_21.setText(_translate("MainWindow", "选择要删除的用户:"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "  个人信息"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "  查询用户*"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "  增添用户*"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "  删除用户*"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "*表示需要最高权限"))
        self.Search.setPlaceholderText(_translate("MainWindow", "搜索"))
