from PySide.QtUiTools import QUiLoader
from messenger.MessengerAPI.Messenger import Messenger
import getpass
from PySide.QtCore import *
from PySide.QtGui import *
import sys
import ui
from PySide import QtCore, QtGui


class MessengerColorChanger(QMainWindow):
    def __init__(self, parent=None):
        super(MessengerColorChanger, self).__init__(parent)
        self.setupUi(self)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(17, 250, 361, 34))
        self.pushButton.setObjectName("pushButton")
        self.login = QtGui.QLineEdit(Dialog)
        self.login.setGeometry(QtCore.QRect(120, 20, 261, 32))
        self.login.setMaxLength(128)
        self.login.setObjectName("login")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 58, 18))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 58, 18))
        self.label_2.setObjectName("label_2")
        self.haslo = QtGui.QLineEdit(Dialog)
        self.haslo.setGeometry(QtCore.QRect(120, 70, 261, 32))
        self.haslo.setMaxLength(64)
        self.haslo.setEchoMode(QtGui.QLineEdit.Password)
        self.haslo.setObjectName("haslo")
        self.id = QtGui.QLineEdit(Dialog)
        self.id.setGeometry(QtCore.QRect(120, 120, 261, 32))
        self.id.setMaxLength(30)
        self.id.setObjectName("id")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 81, 18))
        self.label_3.setObjectName("label_3")
        self.kolor = QtGui.QLineEdit(Dialog)
        self.kolor.setEnabled(True)
        self.kolor.setGeometry(QtCore.QRect(120, 170, 261, 32))
        self.kolor.setMaxLength(8)
        self.kolor.setObjectName("kolor")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 81, 18))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QtGui.QApplication.translate("Dialog", "Messenger Color Changer", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Zmień", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Hasło", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "ID rozmowy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Nowy kolor", None, QtGui.QApplication.UnicodeUTF8))

    def go(self, login, password, id, color):
        messenger = Messenger(login, password)
        konfa = messenger.get_thread(int(id))
        konfa.set_custom_color(color)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MessengerColorChanger()
    frame.show()
    app.exec_()

#haslo = getpass.getpass()
#messenger = Messenger("arturmotyka99@gmail.com", haslo)
#idkonfy = input("Podaj id konfy:")
#konfa = messenger.get_thread(int(idkonfy))
#obecny = konfa.custom_color
#nowy = input("Podaj nowy zajebisty kolor (bez hasza):")
#konfa.set_custom_color("#" + nowy)
#konfa.set_custom_color(obecny)