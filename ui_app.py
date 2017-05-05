from PyQt5 import QtCore, QtGui, QtWidgets
from ui_methed_test import *
import threading
import random
import datetime
import data_filter

class Ui_MainWindow(object):
    ticker_time = 0
    ticker_rest = True

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1209, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(10, 30, 113, 32))
        self.connect_button.setObjectName("connect_button")
        self.ticker_table = QtWidgets.QTableWidget(self.centralwidget)
        self.ticker_table.setGeometry(QtCore.QRect(390, 10, 781, 81))
        self.ticker_table.setAutoFillBackground(False)

        self.ticker_table.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))

        self.ticker_table.setObjectName("ticker_table")
        self.ticker_table.setColumnCount(7)
        self.ticker_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.ticker_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticker_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticker_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticker_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticker_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticker_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticker_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticker_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticker_table.setItem(0, 0, item)
        self.status_label = QtWidgets.QLabel(self.centralwidget)

        self.status_label.setGeometry(QtCore.QRect(130, 30, 241, 31))
        self.status_label.setObjectName("status_label")

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(20, 60, 194, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1209, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.connect_button.clicked.connect(self.to_connect)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.operate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def operate(self):
        dt = datetime.datetime.now()
        now = dt.timestamp() * 1000
        print('operate !!!!!!!!!', self.ticker_time, now)
        if self.ticker_time:
            interval = int(now - self.ticker_time)
            if interval < 1000:
                self.timer.stop()
                self.timer.start(1000 - interval)
            else:
                self.timer.stop()
                self.timer.start(1000)
                if self.ticker_rest:
                    print('send rest')
                    ui_thread_rest_ticker(self)
                    self.ticker_rest = False

    def to_connect(self):
        self.timer.start(1000)
        ui_thread_websocket_start(self)
        ui_change_status_label(self)
        ui_thread_display_ticker_table(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.connect_button.setText(_translate("MainWindow", "连接"))
        item = self.ticker_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "BTC"))
        item = self.ticker_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "时间"))
        item = self.ticker_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "买"))
        item = self.ticker_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "卖"))
        item = self.ticker_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "最高"))
        item = self.ticker_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "最低"))
        item = self.ticker_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "最新"))
        item = self.ticker_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "成交量"))
        __sortingEnabled = self.ticker_table.isSortingEnabled()
        self.ticker_table.setSortingEnabled(False)
        self.ticker_table.setSortingEnabled(__sortingEnabled)
        self.status_label.setText(_translate("MainWindow", "状态："))
