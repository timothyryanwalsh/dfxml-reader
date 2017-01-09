# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Mon Dec 19 14:44:25 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(789, 933)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.source = QtGui.QLineEdit(self.centralwidget)
        self.source.setObjectName(_fromUtf8("source"))
        self.verticalLayout.addWidget(self.source)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.allocBtn = QtGui.QCheckBox(self.centralwidget)
        self.allocBtn.setObjectName(_fromUtf8("allocBtn"))
        self.verticalLayout.addWidget(self.allocBtn)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DFXML Reader", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Path to DFXML file</span></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "Browse", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Options</span></p></body></html>", None))
        self.allocBtn.setText(_translate("MainWindow", "Allocated files only", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Output</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Status</span></p></body></html>", None))
        self.pushButton_3.setText(_translate("MainWindow", "Start", None))

