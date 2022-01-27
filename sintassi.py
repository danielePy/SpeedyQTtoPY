path="C:\\Users\\es-523-8871\\costruttore\\ui"
mainwin="mainwindow.py"

A="#-*-coding: utf-8 -*-\n#base scripts generated with speedyQTtoPY\n#created by Porcari Daniele\n"
A=A+"import sys\nfrom PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow, QMessageBox)\n"
A=A+"from PyQt5.uic import loadUi\nfrom PyQt5 import QtCore, QtGui\n"
INIT="\tdef __init__(self,parent=None):\n\t\tsuper().__init__(parent)\n\t\tself.setupUi(self)\n\t\tself.connectSignalSlots()\n"
INIT=INIT+"\n\tdef connectSignalSlots(self):\n"
START="if __name__ == \"__main__\":\n\tapp = QApplication(sys.argv)\n\twin = Window()\n\twin.show()\n\tsys.exit(app.exec())"
