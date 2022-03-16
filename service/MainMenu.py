import argparse

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import os
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'

import torch
torch.cuda.current_device()
from painter import *
import demo_prog

arg1 = {1:'oilpaintbrush',2:'watercolorink',3:'markerpen',4:'rectangle'}
arg3 = {1:'checkpoints_G_oilpaintbrush',2:'checkpoints_G_watercolor',3:'checkpoints_G_markerpen',4:'checkpoints_G_rectangle'}
arg2 = {'img_path':'',
        'canvas_color':'white',
        'canvas_size':512,
        'max_m_strokes':'500',
        'max_divide':'5',
        'renderer':'',
        'beta_l1':1.0,
        'with_ot_loss':False,
        'beta_ot':0.1,
        'lr':0.005,
        'output_dir':'./output',
        'renderer_checkpoint_dir':'',
        'net_G':'zou-fusion-net'}

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class Ui_MainWindow(QtWidgets.QMainWindow):
    #调用函数传递的参数集合
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 900, 720))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setObjectName("tabWidget")

    #选择文件
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

    #选择照片
        self.btn_chooseFile = QtWidgets.QPushButton(self.tab)
        self.btn_chooseFile.setGeometry(QtCore.QRect(10,50,130,30))

        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setFixedSize(800,720)
        self.label_4.move(150,10)
        self.label_4.setStyleSheet("QLabel{background:white;}"
                                   "QLabel{color:jpg(300,300,300,120);font-size:10px;font-weight:bold;font-family:STKaiti;}")

    #下拉列表框
        self.cd = QtWidgets.QComboBox(self.tab)
        self.cd.move(10,100)
        self.cd.setFixedSize(130,30)
        self.cd.addItem('选择创作风格')
        self.cd.addItem('oilpaintbrush')
        self.cd.addItem('watercolorink')
        self.cd.addItem('markerpen')
        self.cd.addItem('colortapes')
    #下拉列表信号
        self.cd.currentIndexChanged[int].connect(self.print_value)

    #提交按钮
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 150, 130, 30))
        self.pushButton.setIconSize(QtCore.QSize(50, 30))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 0, 281, 100))
        font = QtGui.QFont()
        font.setFamily("STKaiti")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于深度学习的油画创作系统"))
        self.pushButton

        #选择文件
        self.btn_chooseFile.setObjectName("btn_chooseFile")
        self.btn_chooseFile.setText("选取图片")
        #设置信号
        self.btn_chooseFile.clicked.connect(self.loadImage)

        self.pushButton.setText(_translate("MainWindow", "开始创作"))
        self.pushButton.clicked.connect(self.print_image)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "创作"))
        self.label.setText(_translate("MainWindow", "欢迎使用油画创作系统"))

    def loadImage(self):
        imgName,imgType= QFileDialog.getOpenFileName(self,'打开图片','','*.jpg')
        jpg = QtGui.QPixmap(imgName).scaled(self.label_4.width(),self.label_4.height())
        self.label_4.setPixmap(jpg)
        arg2['img_path'] = imgName

    #下拉列表传递函数
    def print_value(self,i):
        arg2['renderer'] = arg1[i]
        arg2['renderer_checkpoint_dir'] = arg3[i]

    #开始创作函数调用训练好的模型
    def print_image(self):
        print(arg2)
        parser = argparse.ArgumentParser(description='STYLIZED NEURAL PAINTING')
        parser.add_argument('--img_path', type=str, default=arg2['img_path'], metavar='str',
                            help='path to test image (default: ./test_images/sunflowers.jpg)')
        parser.add_argument('--renderer', type=str, default=arg2['renderer'], metavar='str',
                            help='renderer: [watercolor, markerpen, oilpaintbrush, rectangle (default oilpaintbrush)')
        parser.add_argument('--canvas_color', type=str, default=arg2['canvas_color'], metavar='str',
                            help='canvas_color: [black, white] (default black)')
        parser.add_argument('--canvas_size', type=int, default=512, metavar='str',
                            help='size of the canvas for stroke rendering')
        parser.add_argument('--max_m_strokes', type=int, default=500, metavar='str',
                            help='max number of strokes (default 500)')
        parser.add_argument('--max_divide', type=int, default=5, metavar='N',
                            help='divide an image up-to max_divide x max_divide patches (default 5)')
        parser.add_argument('--beta_L1', type=float, default=1.0,
                            help='weight for L1 loss (default: 1.0)')
        parser.add_argument('--with_ot_loss', action='store_true', default=False,
                            help='imporve the convergence by using optimal transportation loss')
        parser.add_argument('--beta_ot', type=float, default=0.1,
                            help='weight for optimal transportation loss (default: 0.1)')
        parser.add_argument('--net_G', type=str, default='zou-fusion-net', metavar='str',
                            help='net_G: plain-dcgan, plain-unet, huang-net, or zou-fusion-net (default: zou-fusion-net)')
        parser.add_argument('--renderer_checkpoint_dir', type=str, default=arg2['renderer_checkpoint_dir'],metavar='str',
                            help='dir to load neu-renderer (default: ./checkpoints_G_oilpaintbrush)')
        parser.add_argument('--lr', type=float, default=0.005,
                            help='learning rate for stroke searching (default: 0.005)')
        parser.add_argument('--output_dir', type=str, default=r'./output', metavar='str',
                            help='dir to save painting results (default: ./output)')
        args = parser.parse_args()
        pt = ProgressivePainter(args=args)
        demo_prog.optimize_x(pt)
