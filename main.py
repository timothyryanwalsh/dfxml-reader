#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import * 
import sys

import design

class ProcessorApp(QMainWindow, design.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ProcessorApp, self).__init__(parent)
        self.setupUi(self)

        # build browse functionality buttons
        self.pushButton.clicked.connect(self.browse_source)

        # build start functionality
        self.pushButton_3.clicked.connect(self.start_processing)

    @pyqtSlot()
    def readStdOutput(self):
        self.textEdit.append(QString(self.proc.readAllStandardOutput()))

    @pyqtSlot()
    def readStdError(self):
        self.textEdit.append(QString(self.proc.readAllStandardError()))

    def browse_source(self):
        self.source.clear() # clear directory source text
        file = QFileDialog.getOpenFileName(self, "Select file")

        if file: # if user didn't pick directory don't continue
            self.source.setText(file)

    def on_finished(self):
    	self.lineEdit.setText('Finished')

    def start_processing(self):
        # clear reports
        self.textEdit.clear()
        
        # path to script
        self.processing_script = "/usr/share/ccatools/dfxmlreader/cca_read_dfxml.py"

        # start QProcess
        self.proc = QProcess()

        # acknowledge process has started
        self.lineEdit.setText('Started')

        # build QStringList
        call = QStringList()
        call.append(self.processing_script)
        if self.allocBtn.isChecked():
            call.append("-a")
            
        call.append(self.source.text())

        # call program and redirect stdout to GUI
        self.proc.start("python3", call)
        self.proc.setProcessChannelMode(QProcess.MergedChannels);
        QObject.connect(self.proc, SIGNAL("readyReadStandardOutput()"), self, SLOT("readStdOutput()"));
        QObject.connect(self.proc, SIGNAL("readyReadStandardError()"), self, SLOT("readStdError()"));

        # update status when finished
        self.proc.finished.connect(self.on_finished)

def main():
    app = QApplication(sys.argv)
    form = ProcessorApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()