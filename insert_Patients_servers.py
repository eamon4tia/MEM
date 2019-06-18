import sqlite3
from builtins import print
from datetime import datetime
import pandas as pd
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QGridLayout, QSpacerItem, QSizePolicy, \
    QPushButton, QRadioButton, QVBoxLayout, QGroupBox, QComboBox, QLabel
from PySide2.QtWidgets import QTableWidgetItem
from pandas import read_excel
from widget.DatePicker import DatePicker
from widget.Spoiler import Spoiler

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = sqlite3.connect("C:\\Users\\PC WORLD\\Downloads\\test.sqlite")
        self.cursor = self.db.cursor()

    def on_excel_btn_clicked(self):
        out = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select excel file', './', 'Excel files (*.xls *.xlsx)')
        excel_file_names = out[0]

        if len(excel_file_names) > 0:
            self.ui.excel_file_name = excel_file_names[0]
            self.ui.excel_label.setText(self.ui.excel_file_name)
            if self.ui.sql_file_name is not None:
                self.ui.run_btn.setEnabled(True)

    def on_sql_btn_clicked(self):
        out = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select sql file', './', 'SQL files (*.sqlite *.sql *.db)')
        sql_file_names = out[0]
        if len(sql_file_names) > 0:
            self.ui.sql_file_name = sql_file_names[0]
            self.ui.sqlLabel.setText(self.sql_file_name)
            self.db = sqlite3.connect(self.ui.sql_file_name)
            self.cursor = self.db.cursor()
            if self.ui.excel_file_name is not None:
                self.ui.run_btn.setEnabled(True)

    def search_btn_clicked(self):
        query = "SELECT * FROM Subscribers WHERE WorkId='%s'" % (self.ui.searchLE.text())
        res = self.cursor.execute(query)
        if res:
            self.ui.tableWidget.clear()
            for raw_number, raw_data in enumerate(res):
                self.ui.tableWidget.insertRow(raw_number)

                for column_number, data in enumerate(raw_data):
                    item = QTableWidgetItem(str(data))
                    self.ui.tableWidget.setItem(raw_number, column_number, item)

    def searchBtnClick1(self):
        db= sqlite3.connect("C:\\Users\\PC WORLD\\Downloads\\test.sqlite")
        if (self.ui.h_values[self.ui.comboBox.currentIndex()]  != "all") and (self.ui.searchLE1.text()==""):
            print("ok")
            cur1 = db.cursor()
            date1 = (self.ui.label1.text())
            date2 = (self.ui.label2.text())
            format_date1 = "%Y-%m-%d"
            out_date1 = datetime.strptime(date1, format_date1)
            print(out_date1)
            format_date2 = "%Y-%m-%d"
            out_date2 = datetime.strptime(date2, format_date2)
            print(out_date2)
            v1 = self.ui.h_values[self.ui.comboBox.currentIndex()]
            df1 = ("SELECT * FROM PatientsServices WHERE HospitalName='%s' and date BETWEEN '%s' AND '%s'" % (v1, out_date1, out_date2))
            print(df1)
            #q = "SELECT * FROM sheet1 WHEDRE WorkId='%s'" % (self.ui.searchLE1.text(),)
            #q1 = "SELECT * FROM sheet1 WHERE date BETWEEN '%s' AND '%s'" %(lambda : self.__setLableDate__(, self.datePicker1.selectedDate()),lambda : self.__setLableDate__(self.label2, self.datePicker2.selectedDate()))
            print(v1)
            res1=cur1.execute(df1)
            if res1:
                # self.ui.tableWidget1.clear()
                for raw_number, raw_data in enumerate(res1):
                    self.ui.tableWidget1.insertRow(raw_number)
                    for column_number, data in enumerate(raw_data):
                        item1 = QTableWidgetItem(str(data))
                        self.ui.tableWidget1.setItem(raw_number, column_number, item1)
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(0)
                    item1.setText(_translate("MainWindow", "رقم الدخول", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(1)
                    item1.setText(_translate("MainWindow", "اسم المشترك", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(2)
                    item1.setText(_translate("MainWindow", "الرقم الوظيفي", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(3)
                    item1.setText(_translate("MainWindow", "اسم المستفيد", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(4)
                    item1.setText(_translate("MainWindow", "كود الخدمه", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(5)
                    item1.setText(_translate("MainWindow", "اسم الخدمه", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(6)
                    item1.setText(_translate("MainWindow", "التاريخ", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(7)
                    item1.setText(_translate("MainWindow", "السعر", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(8)
                    item1.setText(_translate("MainWindow", "الاجل", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(9)
                    item1.setText(_translate("MainWindow", "المدفوع", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(10)
                    item1.setText(_translate("MainWindow", "اسم المستشفى", None))
        elif (self.ui.h_values[self.ui.comboBox.currentIndex()]  != "all") and (self.ui.searchLE1.text()!=""):
            print("yes")
            cur= db.cursor()
            date1 = (self.ui.label1.text())
            date2 = (self.ui.label2.text())
            format_date1 = "%Y-%m-%d"
            out_date1 = datetime.strptime(date1, format_date1)
            print(out_date1)
            format_date2 = "%Y-%m-%d"
            out_date2 = datetime.strptime(date2, format_date2)
            print(out_date2)
            HospitalName= self.ui.h_values[self.ui.comboBox.currentIndex()]

            q = "SELECT * FROM PatientsServices WHERE WorkId='%s' and HospitalName='%s' and date BETWEEN '%s' AND '%s'" %  (self.ui.searchLE1.text(),HospitalName,out_date1,out_date2)
           # q1 = "SELECT * FROM sheet1 WHERE date BETWEEN '%s' AND '%s'" % (( self.datePicker1.selectedDate()),(self.label2, self.datePicker2.selectedDate()))
            print(q)
            res = cur.execute(q)

            if res:
                #self.ui.tableWidget1.clear()
                for raw_number, raw_data in enumerate(res):
                    self.ui.tableWidget1.insertRow(raw_number)

                    for column_number, data in enumerate(raw_data):
                        item1 = QTableWidgetItem(str(data))
                        self.ui.tableWidget1.setItem(raw_number, column_number, item1)

                    item1 = self.ui.tableWidget1.horizontalHeaderItem(0)
                    item1.setText(_translate("MainWindow", "رقم الدخول", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(1)
                    item1.setText(_translate("MainWindow", "اسم المشترك", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(2)
                    item1.setText(_translate("MainWindow", "الرقم الوظيفي", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(3)
                    item1.setText(_translate("MainWindow", "اسم المستفيد", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(4)
                    item1.setText(_translate("MainWindow", "كود الخدمه", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(5)
                    item1.setText(_translate("MainWindow", "اسم الخدمه", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(6)
                    item1.setText(_translate("MainWindow", "التاريخ", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(7)
                    item1.setText(_translate("MainWindow", "السعر", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(8)
                    item1.setText(_translate("MainWindow", "الاجل", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(9)
                    item1.setText(_translate("MainWindow", "المدفوع", None))
                    item1 = self.ui.tableWidget1.horizontalHeaderItem(10)
                    item1.setText(_translate("MainWindow", "اسم المستشفى", None))
            else:
                cur1 = db.cursor()
                date1 = (self.ui.label1.text())
                date2 = (self.ui.label2.text())
                format_date1 = "%Y-%m-%d"
                out_date1 = datetime.strptime(date1, format_date1)
                print(out_date1)

                format_date2 = "%Y-%m-%d"
                out_date2 = datetime.strptime(date2, format_date2)
                print(out_date2)

                v1 = self.ui.h_values[self.ui.comboBox.currentIndex()]
                q2 = "SELECT * FROM PatientsServices WHERE HospitalName='%s' and WorkId= '%s' and date BETWEEN '%s' AND '%s'" % (
                    self.ui.h_values[self.ui.comboBox.currentIndex()], self.ui.searchLE1.text(), out_date1, out_date2)

                res1 = cur1.execute(q2)
                if res1:
                    # self.ui.tableWidget1.clear()
                    for raw_number, raw_data in enumerate(res1):
                        self.ui.tableWidget1.insertRow(raw_number)

                        for column_number, data in enumerate(raw_data):
                            item1 = QTableWidgetItem(str(data))
                            self.ui.tableWidget1.setItem(raw_number, column_number, item1)

                        item1 = self.ui.tableWidget1.horizontalHeaderItem(0)
                        item1.setText(_translate("MainWindow", "رقم الدخول", None))
                        item1 = self.ui.tableWidget1.horizontalHeaderItem(1)
                        item1.setText(_translate("MainWindow", "اسم المشترك", None))
                        item1 = self.ui.tableWidget1.horizontalHeaderItem(2)
                        item1.setText(_translate("MainWindow", "الرقم الوظيفي", None))
                        item1 = self.ui.tableWidget1.horizontalHeaderItem(3)
                        item1.setText(_translate("MainWindow", "اسم المستفيد", None))
                        item1 = self.ui.tableWidget1.horizontalHeaderItem(4)
                        item1.setText(_translate("MainWindow", "كود الخدمه", None))
                        item1 = self.ui.tableWidget1.horizontalHeaderItem(5)
                        item1.setText(_translate("MainWindow", "اسم الخدمه", None))
                        item1 = self.ui.tableWidget1.horizontalHeaderItem(6)
                        item1.setText(_translate("MainWindow", "التاريخ", None))
                        item1 = self.ui.tableWidget1.horizontalHeaderItem(7)
                        item1.setText(_translate("MainWindow", "السعر", None))
                        item1 = self.ui.tableWidget1.horizontalHeaderItem(8)
                        item1.setText(_translate("MainWindow", "الاجل", None))
                        item1 = self.ui.tableWidget1.horizontalHeaderItem(9)
                        item1.setText(_translate("MainWindow", "المدفوع", None))
                        item1 = self.ui.tableWidget1.horizontalHeaderItem(10)
                        item1.setText(_translate("MainWindow", "اسم المستشفى", None))

    def on_run_btn_clicked(self):
        self.ui.run_btn.setEnabled(False)
        hospital_name = self.ui.values[self.ui.combo.currentIndex()]
        xls_file = read_excel(self.ui.excel_file_name)
        columns = xls_file.columns

        hospital_name = self.ui.values[self.ui.combo.currentIndex()]
        n_rows = len(xls_file)

        for i in range(0, n_rows):
            row = xls_file.loc[i]

            entry_number = int(row['EntryNumber'])
            subscriber_name = row['SubscriberName']
            work_id = int(row['WorkId'])
            beneficiary_name = row['BeneficiaryName']
            service_code = row['ServiceCode']
            service_name = row['ServiceName']
            timestamp = row['Date'].timestamp()
            cost = float(row['Cost'])
            paid = float(row['Paid'])
            debt = float(row['Debt'])

            table_code, daleel_code, error_type = self.get_additional_data(work_id, service_code, cost)

            insert_query = "INSERT INTO PatientsServices " \
                           "(" \
                               "EntryNumber," \
                               "SubscriberName," \
                               "WorkId," \
                               "BeneficiaryName," \
                               "ServiceCode," \
                               "ServiceName," \
                               "Date," \
                               "Cost," \
                               "Paid," \
                               "Debt," \
                               "HospitalName," \
                               "TableCode," \
                               "DaleelCode," \
                               "ErrorType)" \
                               " VALUES ({}, '{}', '{}','{}','{}','{}',{},{},{},{},'{}','{}','{}',{})"\
                               .format(entry_number, subscriber_name, work_id, beneficiary_name, service_code, service_name, timestamp, cost, paid, debt, hospital_name, table_code, daleel_code, error_type)

            self.cursor.execute(insert_query)

            if error_type == ErrorCodes.NO_ERRORS:
                query = "SELECT TotalCost FROM Subscribers WHERE WorkId='{}';".format(work_id)
                self.cursor.execute(query)
                total_cost= self.cursor.fetchone()[0]
                if total_cost is None:
                    raise TypeError("work id not found")
                total_cost += cost
                update_total_cost_query = "UPDATE Subscribers SET  TotalCost={} WHERE WorkId='{}'".format(total_cost, work_id)
                self.cursor.execute(update_total_cost_query)

        self.db.commit()
        self.ui.run_btn.setEnabled(False)
        self.ui.excel_label.setText("Successful")

    def get_additional_data(self, work_id, service_code, cost):
        error_code = ErrorCodes.NO_ERRORS
        table_code = None
        daleel_code = None

        self.cursor.execute("SELECT * FROM Subscribers WHERE WorkId='{}';".format(work_id))
        subscribers = self.cursor.fetchone()
        if subscribers is None:
            # There is no subscriber with this work id.
            print("Subscriber doesn't exist {}".format(work_id))
            error_code |= ErrorCodes.WORK_ID_NOT_FOUND

        hospital_name = str(self.ui.combo.currentText())
        query = "SELECT TableCode, DaleelCode, Cost FROM Services WHERE ServiceCode='{}' AND HospitalName='{}'".format(service_code, hospital_name)
        service = self.cursor.execute(query).fetchone()
        if service is None:
            # The Service doesn't exist in agreed upon services
            # print("Service doesn't exist {}".format(service_code))
            error_code |= ErrorCodes.SERVICE_CODE_NOT_FOUND
            table_code = -1
            daleel_code = -1
        else:
            # The Service is exist in agreed upon services
            table_code = service[0]
            daleel_code = service[1]
            _cost = service[2]
            if cost != _cost:
                if cost < _cost:
                    error_code |= ErrorCodes.COST_LESS_THAN
                if cost > _cost:
                    error_code |= ErrorCodes.COST_MORE_THAN

        return table_code, daleel_code, error_code

class ErrorCodes:
    NO_ERRORS = 0
    WORK_ID_NOT_FOUND = 1
    SERVICE_CODE_NOT_FOUND = 2
    COST_LESS_THAN = 4
    COST_MORE_THAN = 8


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        def fun(spoiler):
            if spoiler.isOpened():
                spoiler.close()
            else:
                spoiler.open()

       # app = QApplication(sys.argv)
        w = QMainWindow()
        cw = QWidget()
        mainLayout = QHBoxLayout()
        cw.setLayout(mainLayout)

        gridLayout = QGridLayout()

        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        gridLayout.addItem(spacerItem1, 0, 0, 1, 1)

        pushButton1 = QPushButton()
        pushButton1.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        pushButton1.setText("")
       # gridLayout.addWidget(pushButton1, 0, 1, 1, 1)

        self.label1 = QLabel()
        self.label1.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.label1.setObjectName("")
        gridLayout.addWidget(self.label1, 0, 2, 1, 1)

        datePicker1 = DatePicker()
        gridLayout.addWidget(datePicker1, 0, 1, 1, 1)

        datePicker1.selectionChanged.connect(lambda : self.__setLableDate__(self.label1, datePicker1.selectedDate()))

        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        gridLayout.addItem(spacerItem2, 0, 3, 1, 1)

        self.label2 = QLabel()
        self.label2.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.label2.setObjectName("")



        gridLayout.addWidget(self.label2, 0, 4, 1, 1)

        datePicker2 = DatePicker()
        gridLayout.addWidget(datePicker2, 0, 5, 1, 1)

        datePicker2.selectionChanged.connect(lambda: self.__setLableDate__(self.label2, datePicker2.selectedDate()))

        pushButton2 = QPushButton()
        pushButton2.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        pushButton2.setText("")
        #gridLayout.addWidget(pushButton2, 0, 5, 1, 1)

        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.      Expanding, QSizePolicy.Minimum)
        gridLayout.addItem(spacerItem3, 0, 6, 1, 1)

        groupBox = QGroupBox()
        groupBox.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        verticalLayout = QVBoxLayout(groupBox)

        radioButton1 = QRadioButton(groupBox)
        radioButton1.setText("Subscribers")
        verticalLayout.addWidget(radioButton1)

        radioButton2 = QRadioButton(groupBox)
        radioButton1.setText("PatientsServices")
        verticalLayout.addWidget(radioButton2)

        export_btn=QPushButton()
        export_btn.setText("export")
        gridLayout.addWidget(export_btn)
        export_btn.clicked.connect(lambda: self.onExport_btn())

        gridLayout.addWidget(groupBox, 1, 1, 1, 2, Qt.AlignTop)

        self.comboBox = QComboBox()
        self.h_values = [ "all","مستشفي الصفوة الدولي","مستشفي السلام الدولي", "مختبر مصراتة المركزي","مستشفي الحكمة الحديث","مستشفى المدينه السكنيه"]
        self.comboBox.addItems(self.h_values)



        self.comboBox.activated.connect(self.oncomboBoxChanged)
        gridLayout.addWidget(self.comboBox, 1, 4, 1, 2, Qt.AlignTop)
        btn = QPushButton("Click me")
        btn.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        spoiler = Spoiler(Spoiler.Orientation.VERTICAL)
        spoiler.setContentLayout(gridLayout)
        mainLayout.addWidget(btn)
        #self.searchGridLayout.addWidget(spoiler)
        # mainLayout.setAlignment(Qt.AlignRight)
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(716, 392)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.InsertTab = QtWidgets.QWidget()
        self.InsertTab.setObjectName(_fromUtf8("InsertTab"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.InsertTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtWidgets.QSpacerItem(20, 109, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.insertGridLayout = QtWidgets.QGridLayout()
        self.insertGridLayout.setObjectName(_fromUtf8("insertGridLayout"))
        self.run_btn = QtWidgets.QPushButton(self.InsertTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_btn.sizePolicy().hasHeightForWidth())
        self.run_btn.setSizePolicy(sizePolicy)
        self.run_btn.setMouseTracking(False)
        self.run_btn.setAutoFillBackground(False)
        self.run_btn.setStyleSheet(_fromUtf8("border: none"))
        self.run_btn.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(".\\icons\\run.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.run_btn.setIcon(icon)
        self.run_btn.setIconSize(QtCore.QSize(64, 64))
        self.run_btn.setObjectName(_fromUtf8("runBtn"))
        self.insertGridLayout.addWidget(self.run_btn, 0, 3, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.combo = QComboBox()
        self.values =["مستشفي الصفوة الدولي","مستشفي السلام الدولي","مختبر مصراتة المركزي","مستشفي الحكمة الحديث","مستشفى المدينه السكنيه"]
        self.combo.addItems(self.values)

        if self.combo.currentIndex()==1:
           print("kln")
        self.combo.activated.connect(self.oncomboChanged)
        self.insertGridLayout.addWidget(self.combo, 1, 4, 1, 2, Qt.AlignTop)
        self.insertGridLayout.addItem(spacerItem1, 0, 5, 1, 1)
        self.excel_label = QtWidgets.QLabel(self.InsertTab)
        self.excel_label.setText(_fromUtf8(""))
        self.excel_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.excel_label.setObjectName(_fromUtf8("excelLabel"))
        self.insertGridLayout.addWidget(self.excel_label, 1, 0, 1, 3)
        self.sqlBtn = QtWidgets.QPushButton(self.InsertTab)
        self.sqlBtn.setMinimumSize(QtCore.QSize(200, 0))
        self.sqlBtn.setObjectName(_fromUtf8("sqlBtn"))
        self.insertGridLayout.addWidget(self.sqlBtn, 0, 4, 1, 1)
        self.excelBtn = QtWidgets.QPushButton(self.InsertTab)
        self.excelBtn.setMinimumSize(QtCore.QSize(200, 0))
        self.excelBtn.setObjectName(_fromUtf8("excelBtn"))
        self.insertGridLayout.addWidget(self.excelBtn, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.insertGridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.sqlLabel = QtWidgets.QLabel(self.InsertTab)
        self.sqlLabel.setText(_fromUtf8(""))
        self.sqlLabel.setObjectName(_fromUtf8("sqlLabel"))
        self.insertGridLayout.addWidget(self.sqlLabel, 1, 4, 1, 2)
        self.verticalLayout_2.addLayout(self.insertGridLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 108, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.tabWidget.addTab(self.InsertTab, _fromUtf8(""))
        # self.filterBtn = QtWidgets.QPushButton(self.searchTab)
        # self.filterBtn.setStyleSheet(_fromUtf8("border: none"))
        # icon2 = QtGui.QIcon()
        # icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/filter_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.filterBtn.setIcon(icon2)
        # self.filterBtn.setObjectName(_fromUtf8("filterBtn"))
        # self.searchGridLayout.addWidget(self.filterBtn, 0, 3, 1, 1)
        # self.searchGridLayout.addWidget(spoiler)

        self.export_btn=QPushButton()
        self.export_btn.setText("export")
        #self.gridLayout.addWidget(export_btn)
        self.export_btn.clicked.connect(lambda: self.onExport_btn_subscribers())
        #self.exprt_btn = QtWidgets.QPushButton()
        #self.exprt_btn.setText("export")
        #self.exprt_btn.setObjectName(_fromUtf8("exprt_btn"))
        #self.searchGridLayout1.addWidget(self.exprt_btn, 0, 0, 2, 1)
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.excelBtn.clicked.connect(MainWindow, QtCore.SLOT("on_excel_btn_clicked()"))
        self.sqlBtn.clicked.connect(MainWindow, QtCore.SLOT("on_sql_btn_clicked()"))
        self.run_btn.clicked.connect(MainWindow, QtCore.SLOT("on_run_btn_clicked()"))
        self.excel_file_name = None
        self.sql_file_name = "C:\\Users\\PC WORLD\\Downloads\\test.sqlite"
        self.sqlLabel.setText(self.sql_file_name)
        conn = sqlite3.connect("C:\\Users\\PC WORLD\\Downloads\\test.sqlite")
        result = conn.execute("SELECT * FROM Subscribers")
        conn.close()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Search</span></p></body></html>", None))
        self.sqlBtn.setText(_translate("MainWindow", "select sql file", None))
        self.excelBtn.setText(_translate("MainWindow", "select exel file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.InsertTab), _translate("MainWindow", "INSERT", None))
    def oncomboChanged(self, index):
        name = self.values[index]
        print(name)

    def oncomboBoxChanged(self,index):
        h_name = self.h_values[index]
        print(h_name)

    def onExport_btn(self):
        db = sqlite3.connect("C:\\Users\\PC WORLD\\Downloads\\test.sqlite")
        if self.h_values[self.comboBox.currentIndex()]  != "all":
             date1 = (self.label1.text())
             date2 = (self.label2.text())

             format_date1 = "%Y-%m-%d"
             out_date1 = datetime.strptime(date1, format_date1)
             print(out_date1)

             format_date2 = "%Y-%m-%d"
             out_date2 = datetime.strptime(date2, format_date2)
             print(out_date2)

             df1 = pd.read_sql_query("SELECT * FROM PatientsServices WHERE HospitalName='%s' and date BETWEEN '%s' AND '%s'" % (self.h_values[self.comboBox.currentIndex()],out_date1,out_date2), db)
            # df.to_excel('output.xlsx')

            # Create a Pandas Excel writer using XlsxWriter as the engine.
             writer = pd.ExcelWriter(self.h_values[self.comboBox.currentIndex()]  + '.xlsx', engine='xlsxwriter')

            # Convert the dataframe to an XlsxWriter Excel object.
             df1.to_excel(writer, sheet_name='Sheet2')

            # Close the Pandas Excel writer and output the Excel file.
             writer.save()
             print(writer)

        else:
            date1 = (self.label1.text())
            date2 = (self.label2.text())

            format_date1 = "%Y-%m-%d"
            out_date1 = datetime.strptime(date1, format_date1)
            print(out_date1)

            format_date2 = "%Y-%m-%d"
            out_date2 = datetime.strptime(date2, format_date2)
            print(out_date2)

            df = pd.read_sql_query("SELECT * FROM PatientsServices WHERE WorkId='%s' and date BETWEEN '%s' AND '%s'" % (self.searchLE1.text(),out_date1,out_date2), db)
# df.to_excel('output.xlsx')

# Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
            df.to_excel(writer, sheet_name='Sheet2')

# Close the Pandas Excel writer and output the Excel file.
            writer.save()
            print(writer)

    def onExport_btn_subscribers(self):
            db = sqlite3.connect("C:\\Users\\PC WORLD\\Downloads\\test.sqlite")


            df1 = pd.read_sql_query("SELECT * FROM Subscribers " ,db )
                # df.to_excel('output.xlsx')

                # Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter('السقف.xlsx', engine='xlsxwriter')

                # Convert the dataframe to an XlsxWriter Excel object.
            df1.to_excel(writer, sheet_name='Roof1')

                # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            print(writer)
    #    def searchBtnClick(self):
     #   print("hhhhhhhhhhhhhhhhhhhhhhhh")

      #  db= sqlite3.connect("C:\\Users\\PC WORLD\\Downloads\\test.sqlite")
      #  cur = db.cursor()
       # q = "SELECT * FROM PatientsServices WHERE name='%s'" % (self.searchLE.text(),)
       # print(q)

        #res = cur.execute(q)
       # if res:
        #    self.tableWidget.clear()
         #   for raw_number, raw_data in enumerate(res):
          #      self.tableWidget.insertRow(raw_number)

           #     for column_number, data in enumerate(raw_data):
            #        item = QTableWidgetItem(str(data))
             #       self.tableWidget.setItem(raw_number, column_number, item)