import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QGridLayout, QApplication

from ui.report import Ui_MainWindow
from dao.dbOpChart import Chart,Figure_Canvas
from service import globalValue
import os
from dao.dbConfig import localSourceConfig as localConfig
from ui.test import QClickableImage

sys.path.append('C:\Program Files\MySQL\MySQL Server 5.7\bin')

class ChartOp(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(ChartOp, self).__init__(parent)
        self.setupUi(self)
        self.staff = globalValue.get_staff()
        self.welcome.setText(self.staff.sname)
        self.role.setText('权限：'+ self.staff.srole)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #实现页面切换
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.stackedWidget.setCurrentIndex(0)

        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox

        lineedit1 = self.path1
        lineedit2 = self.path2
        lineedit3 = self.path3
        self.scan.clicked.connect(lambda: self.setBrowerPath(lineedit1))
        self.scan_2.clicked.connect(lambda: self.setBrowerPath(lineedit2))
        self.scan_3.clicked.connect(lambda: self.setBrowerPath(lineedit3))
        #导出数据库文件
        self.tosql1.clicked.connect(self.toSQLDB)
        self.tosql2.clicked.connect(self.toSQLTable)
        self.toexcel.clicked.connect(self.toExcel)
        self.ask.clicked.connect(self.help)
        self.showfigure1.clicked.connect(self.start_img_viewer)

    def setBrowerPath(self,lineedit):
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self,"选择导出目录","D:\pictures")
        lineedit.setText(download_path)

    def toSQLDB(self):
        """导出整个库"""
        key = localConfig['passwd']
        path = self.path1.text()
        os.system("mysqldump -uroot -p%s dbdesign > %s/dbdesign.sql" % (key,path))
        QMessageBox().information(None, "提示", "导出数据库完成！", QMessageBox.Yes)

    def toSQLTable(self):
        """导出某个表"""
        key = localConfig['passwd']
        path = self.path2.text()
        table_name = self.name1.currentText()
        if table_name == '请选择...':
            QMessageBox.information(None,'提示','必须选择一个表',QMessageBox.Yes)
            return False
        os.system("mysqldump -uroot -p%s dbdesign %s > %s/%s.sql" %(key,table_name,path,table_name))
        QMessageBox().information(None, "提示", "导出数据库表完成！", QMessageBox.Yes)

    def toExcel(self):
        """导出某个表到excel"""
        key = localConfig['passwd']
        c = Chart()
        path = self.path3.text()
        table_name = self.name2.currentText()
        if table_name == '请选择...':
            QMessageBox.information(None,'提示','必须选择一个表',QMessageBox.Yes)
            return False
        c.toExcel(path,table_name)
        QMessageBox().information(None, "提示", "导出表格完成！", QMessageBox.Yes)

    def help(self):
        QMessageBox().information(None, "提示","staff -- 员工表\n", QMessageBox.Yes)

    def start_img_viewer(self):
        file_path = "./output"
        img_type = 'png'
        if file_path and img_type:
            png_list = list(i for i in os.listdir(file_path) if str(i).endswith('.{}'.format(img_type)))
            num = len(png_list)
            if num !=0:
                for i in range(num):
                    image_id = str(file_path + '/' + png_list[i])
                    print(image_id)
                    pixmap = QPixmap(image_id)
                    print(pixmap)
                    print(image_id)
                    self.addImage(pixmap, image_id)
                    QApplication.processEvents()
            else:
                QMessageBox.warning(self,'错误','生成图片文件为空')
                self.event(exit())
        else:
            QMessageBox.warning(self,'错误','文件为空，请稍后')

    def addImage(self, pixmap, image_id):
        #图像法列数
        nr_of_columns = self.get_nr_of_image_columns()
        #这个布局内的数量
        nr_of_widgets = self.gridLayout.count()
        self.max_columns =nr_of_columns

        if self.row < self.max_columns:
            self.row =self.row +1

        else:
            self.row = self.row + 1

        clickable_image = QClickableImage(self.displayed_image_size, self.displayed_image_size, pixmap, image_id)
        clickable_image.clicked.connect(self.on_left_clicked)
        clickable_image.rightClicked.connect(self.on_right_clicked)
        self.gridLayout.addWidget(clickable_image, self.row, self.col)

    def on_left_clicked(self,image_id):
        print('left clicked - image id = '+image_id)
    def on_right_clicked(self,image_id):
        print('right clicked - image id = ' + image_id)
    def get_nr_of_image_columns(self):
        #展示图片的区域
        scroll_area_images_width = 600
        if scroll_area_images_width > self.displayed_image_size:
            pic_of_columns = scroll_area_images_width // self.displayed_image_size  #计算出一行几列；
        else:
            pic_of_columns = 1
        return pic_of_columns