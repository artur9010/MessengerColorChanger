from messenger.MessengerAPI.Messenger import Messenger
from PySide.QtCore import *
from PySide.QtGui import *
import sys
from PySide import QtCore, QtGui

login_value = ""
password_value = ""
id_value = 0
color_value = "#2137ff"

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
        self.login = QtGui.QLineEdit()
        self.login.setMaxLength(128)
        self.login.setText("")

        login_label = QtGui.QLabel("Login")

        grid.addWidget(login_label, 0, 0)
        grid.addWidget(self.login, 0, 1)

        # password
        #TODO: "pokaz haslo"
        #TODO: zapamietaj haslo
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
        #todo: color picker
        self.color = QtGui.QLineEdit()
        self.color.setMaxLength(8)

        color_label = QtGui.QLabel("Kolor")

        grid.addWidget(color_label, 3, 0)
        grid.addWidget(self.color, 3, 1)

        # button
        self.button = QtGui.QPushButton()
        self.button.setText("Do dzieła!")
        self.button.clicked.connect(self.buttonClick)
        print("[DEBUG]")
        print(self.login.text())
        grid.addWidget(self.button, 4, 0, 1, 0)


        # window
        self.setLayout(grid)

        self.setGeometry(600, 300, 600, 400) #polozeniex, polozeniey, x, y
        self.setWindowTitle("Messenger Color Changer")
        self.show()

        def buttonClick():
            print("[DEBUG] buttonClick")
            go(self.login.text(), self.password.text(), self.id.text(), self.color.text())


def button_click():
    print("test")
    #go("arturmotyka99@gmail.com", "kziciota", 818700278230570, "#515151")
    print("test2")
    print("")



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