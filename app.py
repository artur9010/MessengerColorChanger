from messenger.MessengerAPI.Messenger import Messenger
from PySide.QtCore import *
from PySide.QtGui import *
import sys
from PySide import QtCore, QtGui


class MessengerColorChanger(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MessengerColorChanger, self).__init__(parent)
        self.setupUi()


    def setupUi(self):
        #Todo: lista konf
        #todo: szukajka konf
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        # login
        login = QtGui.QLineEdit()
        login.setMaxLength(128)

        login_label = QtGui.QLabel("Login")

        grid.addWidget(login_label, 0, 0)
        grid.addWidget(login, 0, 1)

        # password
        #TODO: "pokaz haslo"
        #TODO: zapamietaj haslo
        password = QtGui.QLineEdit()
        password.setMaxLength(64)
        password.setEchoMode(QtGui.QLineEdit.Password)

        password_label = QtGui.QLabel("Hasło")

        grid.addWidget(password_label, 1, 0)
        grid.addWidget(password, 1, 1)

        # id
        id = QtGui.QLineEdit()
        id.setMaxLength(30)

        id_label = QtGui.QLabel("ID rozmowy")

        grid.addWidget(id_label, 2, 0)
        grid.addWidget(id, 2, 1)

        # color
        #todo: color picker
        color = QtGui.QLineEdit()
        color.setMaxLength(8)

        color_label = QtGui.QLabel("Kolor")

        grid.addWidget(color_label, 3, 0)
        grid.addWidget(color, 3, 1)

        # button
        button = QtGui.QPushButton()
        button.setText("Do dzieła!")
        #button.clicked.connect(go(login.text, password.text, id.text, color.text))
        #button.clicked.connect(syf("osiem"))
        grid.addWidget(button, 4, 0, 1, 0)


        # window
        self.setLayout(grid)

        self.setGeometry(600, 300, 600, 400) #polozeniex, polozeniey, x, y
        self.setWindowTitle("Messenger Color Changer")
        self.show()


def syf(text):
    print(text)


def go(login, password, id, color):
    if not bool(str(login).strip()):
        return
    if not bool(str(password).strip()):
        return
    if not bool(str(id).strip()):
        return
    if not bool(str(color).strip()):
        return
    messenger = Messenger(login, password)
    konfa = messenger.get_thread(int(id))
    konfa.set_custom_color(color)

def main():
    app = QApplication(sys.argv)
    frame = MessengerColorChanger()
    app.exec_()

if __name__ == '__main__':
    main()

#haslo = getpass.getpass()
#messenger = Messenger("arturmotyka99@gmail.com", haslo)
#idkonfy = input("Podaj id konfy:")
#konfa = messenger.get_thread(int(idkonfy))
#obecny = konfa.custom_color
#nowy = input("Podaj nowy zajebisty kolor (bez hasza):")
#konfa.set_custom_color("#" + nowy)
#konfa.set_custom_color(obecny)