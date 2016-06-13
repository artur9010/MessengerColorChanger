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
        # Todo: lista konf
        # todo: szukajka konf
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        # login
        self.login = QtGui.QLineEdit()
        self.login.setMaxLength(128)
        self.login.setText("")

        login_label = QtGui.QLabel("Login")

        grid.addWidget(login_label, 0, 0)
        grid.addWidget(self.login, 0, 1)

        # password
        # TODO: "pokaz haslo"
        # TODO: zapamietaj haslo
        self.password = QtGui.QLineEdit()
        self.password.setMaxLength(64)
        self.password.setEchoMode(QtGui.QLineEdit.Password)

        password_label = QtGui.QLabel("Hasło")

        grid.addWidget(password_label, 1, 0)
        grid.addWidget(self.password, 1, 1)

        # id
        self.id = QtGui.QLineEdit()
        self.id.setMaxLength(30)

        id_label = QtGui.QLabel("ID rozmowy")

        grid.addWidget(id_label, 2, 0)
        grid.addWidget(self.id, 2, 1)

        # color
        # todo: color picker
        self.color = QtGui.QLineEdit()
        self.color.setMaxLength(8)

        color_label = QtGui.QLabel("Kolor")

        grid.addWidget(color_label, 3, 0)
        grid.addWidget(self.color, 3, 1)

        # button
        self.button = QtGui.QPushButton()
        self.button.setText("Do dzieła!")
        print("debug 1")
        self.button.clicked.connect(button_click)
        print("debug 2")
        grid.addWidget(self.button, 4, 0, 1, 0)

        global instance
        instance = self

        # window
        self.setLayout(grid)

        self.setGeometry(600, 300, 600, 250)  # polozeniex, polozeniey, x, y
        self.setWindowTitle("Messenger Color Changer")
        self.show()


def button_click():
    print("debug start")
    print(instance.login.text())
    print("debug 3")
    #print(instance.password.text())
    print("debug 4")
    print(instance.id.text())
    print("debug 5")
    print(instance.color.text())
    print("debug 6")
    if not go(instance.login.text(), instance.password.text(), instance.id.text(), instance.color.text()):
        print("debug = brakuje czegos")
    else:
        print("debug = ok")
    print("debug end")
    print("")


def go(login, password, id, color):
    if not str(login).strip():
        return False
    if not str(password).strip():
        return False
    if not str(id).strip():
        return False
    if not str(color).strip():
        return False
    messenger = Messenger(login, password)
    konfa = messenger.get_thread(int(id))
    konfa.set_custom_color(color)
    return True


def main():
    app = QApplication(sys.argv)
    frame = MessengerColorChanger()
    app.exec_()


if __name__ == '__main__':
    main()
