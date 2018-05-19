# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 841)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/icons8-google-news-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("QWidget{\n"
"font-size:18pt;\n"
"font-family:\"WenQuanYi Micro Hei\";\n"
"font-weight: 400;\n"
"}\n"
"QPushButton{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 4px;\n"
"background-color:transparent;\n"
"padding:6px 12px;\n"
"}\n"
"QPushButton#url1ResetBtn, \n"
"QPushButton#url2ResetBtn{\n"
"color: #dc3545;\n"
"border-color: #dc3545;\n"
"}\n"
"QPushButton#url1CrawlBtn, \n"
"QPushButton#url2CrawlBtn,\n"
"QPushButton#detectBtn{\n"
"color: #28a745;\n"
"border-color: #28a745;\n"
"}\n"
"QPushButton:hover#url1CrawlBtn,  \n"
"QPushButton:hover#url2CrawlBtn,\n"
"QPushButton:hover#detectBtn{\n"
"color: #fff;\n"
"text-decoration: none;\n"
"background-color: #28a745;\n"
"border-color:#28a745;\n"
"text-decoration: none;\n"
"}\n"
"QPushButton:hover#url1ResetBtn, \n"
"QPushButton:hover#url2ResetBtn{\n"
"color: #fff;\n"
"text-decoration: none;\n"
"background-color: #dc3545;\n"
"border-color:#dc3545;\n"
"text-decoration: none;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.simiBtn = QtWidgets.QPushButton(self.centralwidget)
        self.simiBtn.setObjectName("simiBtn")
        self.horizontalLayout_10.addWidget(self.simiBtn)
        self.kwBtn = QtWidgets.QPushButton(self.centralwidget)
        self.kwBtn.setObjectName("kwBtn")
        self.horizontalLayout_10.addWidget(self.kwBtn)
        self.settingsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.settingsBtn.setObjectName("settingsBtn")
        self.horizontalLayout_10.addWidget(self.settingsBtn)
        self.gridLayout.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Page1 = QtWidgets.QWidget()
        self.Page1.setObjectName("Page1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.Page1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.url1 = QtWidgets.QLineEdit(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.url1.setFont(font)
        self.url1.setObjectName("url1")
        self.horizontalLayout_2.addWidget(self.url1)
        self.url1ResetBtn = QtWidgets.QPushButton(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.url1ResetBtn.setFont(font)
        self.url1ResetBtn.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.url1ResetBtn.setObjectName("url1ResetBtn")
        self.horizontalLayout_2.addWidget(self.url1ResetBtn)
        self.url1CrawlBtn = QtWidgets.QPushButton(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.url1CrawlBtn.setFont(font)
        self.url1CrawlBtn.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.url1CrawlBtn.setObjectName("url1CrawlBtn")
        self.horizontalLayout_2.addWidget(self.url1CrawlBtn)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.url2 = QtWidgets.QLineEdit(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.url2.setFont(font)
        self.url2.setObjectName("url2")
        self.horizontalLayout.addWidget(self.url2)
        self.url2ResetBtn = QtWidgets.QPushButton(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.url2ResetBtn.setFont(font)
        self.url2ResetBtn.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.url2ResetBtn.setObjectName("url2ResetBtn")
        self.horizontalLayout.addWidget(self.url2ResetBtn)
        self.url2CrawlBtn = QtWidgets.QPushButton(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.url2CrawlBtn.setFont(font)
        self.url2CrawlBtn.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.url2CrawlBtn.setObjectName("url2CrawlBtn")
        self.horizontalLayout.addWidget(self.url2CrawlBtn)
        self.horizontalLayout_9.addLayout(self.horizontalLayout)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title1 = QtWidgets.QLabel(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.title1.setFont(font)
        self.title1.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.title1.setObjectName("title1")
        self.verticalLayout_2.addWidget(self.title1)
        self.news1 = QtWidgets.QPlainTextEdit(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.news1.setFont(font)
        self.news1.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.news1.setReadOnly(True)
        self.news1.setObjectName("news1")
        self.verticalLayout_2.addWidget(self.news1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title2 = QtWidgets.QLabel(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.title2.setFont(font)
        self.title2.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.title2.setObjectName("title2")
        self.verticalLayout.addWidget(self.title2)
        self.news2 = QtWidgets.QPlainTextEdit(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.news2.setFont(font)
        self.news2.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.news2.setReadOnly(True)
        self.news2.setObjectName("news2")
        self.verticalLayout.addWidget(self.news2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.tag1 = QtWidgets.QTextEdit(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.tag1.setFont(font)
        self.tag1.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.tag1.setObjectName("tag1")
        self.verticalLayout_3.addWidget(self.tag1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_10.addWidget(self.label_6)
        self.tag2 = QtWidgets.QTextEdit(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.tag2.setFont(font)
        self.tag2.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.tag2.setObjectName("tag2")
        self.verticalLayout_10.addWidget(self.tag2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.distance = QtWidgets.QLabel(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.distance.setFont(font)
        self.distance.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.distance.setText("")
        self.distance.setObjectName("distance")
        self.horizontalLayout_3.addWidget(self.distance)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.detectBtn = QtWidgets.QPushButton(self.Page1)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.detectBtn.setFont(font)
        self.detectBtn.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.detectBtn.setObjectName("detectBtn")
        self.horizontalLayout_3.addWidget(self.detectBtn)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.Page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.page2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.lineEdit = QtWidgets.QLineEdit(self.page2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_11.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.page2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_11.addWidget(self.pushButton_2)
        self.closeStatBtn = QtWidgets.QPushButton(self.page2)
        self.closeStatBtn.setObjectName("closeStatBtn")
        self.horizontalLayout_11.addWidget(self.closeStatBtn)
        self.statBtn = QtWidgets.QPushButton(self.page2)
        self.statBtn.setObjectName("statBtn")
        self.horizontalLayout_11.addWidget(self.statBtn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.output = QtWidgets.QPlainTextEdit(self.page2)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.output.setFont(font)
        self.output.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.horizontalLayout_12.addWidget(self.output)
        self.result = QtWidgets.QPlainTextEdit(self.page2)
        self.result.setReadOnly(True)
        self.result.setObjectName("result")
        self.horizontalLayout_12.addWidget(self.result)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.page3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.page3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_7.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_7.addWidget(self.lineEdit_3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.page3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.page3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.page3)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_7.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.page3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_7.addWidget(self.pushButton_5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.page3)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.textEdit = QtWidgets.QTextEdit(self.page3)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_5.addWidget(self.textEdit)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.stackedWidget.addWidget(self.page3)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 26))
        self.menubar.setObjectName("menubar")
        self.about = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        self.about.setFont(font)
        self.about.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.about.setObjectName("about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("WenQuanYi Micro Hei")
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.about.addAction(self.exit)
        self.menubar.addAction(self.about.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.url1ResetBtn.clicked.connect(self.url1.clear)
        self.url2ResetBtn.clicked.connect(self.url2.clear)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "新闻相似度检测"))
        self.simiBtn.setText(_translate("MainWindow", "相似度检测"))
        self.kwBtn.setText(_translate("MainWindow", "关键词统计"))
        self.settingsBtn.setText(_translate("MainWindow", "设置"))
        self.label.setText(_translate("MainWindow", "新闻1"))
        self.url1ResetBtn.setText(_translate("MainWindow", "重置"))
        self.url1CrawlBtn.setText(_translate("MainWindow", "抓取"))
        self.label_2.setText(_translate("MainWindow", "新闻2"))
        self.url2ResetBtn.setText(_translate("MainWindow", "重置"))
        self.url2CrawlBtn.setText(_translate("MainWindow", "抓取"))
        self.title1.setText(_translate("MainWindow", "新闻1标题:"))
        self.title2.setText(_translate("MainWindow", "新闻2标题:"))
        self.label_5.setText(_translate("MainWindow", "新闻1标签:"))
        self.label_6.setText(_translate("MainWindow", "新闻2标签:"))
        self.label_3.setText(_translate("MainWindow", "相似度:"))
        self.detectBtn.setText(_translate("MainWindow", "开始检测"))
        self.label_8.setText(_translate("MainWindow", "关键词"))
        self.pushButton_2.setText(_translate("MainWindow", "重置"))
        self.closeStatBtn.setText(_translate("MainWindow", "停止统计"))
        self.statBtn.setText(_translate("MainWindow", "开始统计"))
        self.label_4.setText(_translate("MainWindow", "MONGODB_SERVER"))
        self.label_7.setText(_translate("MainWindow", "MONGODB_PORT"))
        self.lineEdit_2.setText(_translate("MainWindow", "localhost"))
        self.lineEdit_3.setText(_translate("MainWindow", "27017"))
        self.pushButton_3.setText(_translate("MainWindow", "检测"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_4.setText(_translate("MainWindow", "检测"))
        self.pushButton_5.setText(_translate("MainWindow", "确定"))
        self.label_11.setText(_translate("MainWindow", "配置清单:"))
        self.about.setTitle(_translate("MainWindow", "关于"))
        self.exit.setText(_translate("MainWindow", "退出"))
        self.exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

import resources_rc
