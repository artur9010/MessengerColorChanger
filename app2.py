from messenger.MessengerAPI.Messenger import Messenger
from PySide import QtGui
from PySide.QtCore import *
from PySide.QtGui import *
import sys, json, os

#for tests:
#id 100002217879841
#color #2137ff

# druga wersja zmieniacza kolorkow
# todo: lista konf
# todo: color picker
# todo: zapamietywanie hasla
# todo: logowanie przed cala reszto [done]

class MessengerColorChangerLogin(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MessengerColorChangerLogin, self).__init__(parent)
        global instance
        instance = self
        self.setupUi()

    def setupUi(self):
        grid = QtGui.QGridLayout()
        grid.setSpacing(15)

        login_label = QLabel("Login")
        self.login = QLineEdit()

        password_label = QLabel("Hasło")
        self.password = QLineEdit()

        login_button = QPushButton("Zaloguj się")
        login_button.clicked.connect(self.login_to_facebook)

        grid.addWidget(login_label, 0, 0)
        grid.addWidget(self.login, 0, 1)
        grid.addWidget(password_label, 1, 0)
        grid.addWidget(self.password, 1, 1)
        grid.addWidget(login_button, 2, 0, 1, 0)

        self.setLayout(grid)
        self.setGeometry(600, 300, 600, 250)  # polozeniex, polozeniey, x, y
        self.setWindowTitle("Zaloguj się")
        self.show()

    def login_to_facebook(self):
        login = instance.login.text()
        password = instance.password.text()
        MessengerColorChanger(login, password, self)

class MessengerColorChanger(QtGui.QWidget):
    def __init__(self, login, password, loginwindow, parent=None):
        super(MessengerColorChanger, self).__init__(parent)
        try:
            messenger = Messenger(login, password)
            global instance
            instance = self
            loginwindow.hide()
            self.setupUi(messenger)
        except:
            QMessageBox.critical(self, "Błędzik", "Nieprawidłowy login lub hasło.",
                                 QMessageBox.Ok)

    def setupUi(self, messenger):
        grid = QtGui.QGridLayout()
        grid.setSpacing(5)

        self.conversation_list = QListWidget()

        thread_list = messenger.ordered_thread_list
        for user in thread_list:
            print("---")
            #print(user.name)
            print(user.fbid)
            print("")
        #print(thread_list)

        self.setGeometry(600, 300, 600, 250)  # polozeniex, polozeniey, x, y
        self.setWindowTitle("Messenger Color Changer")
        self.show()


def main():
    app = QApplication(sys.argv)
    frame = MessengerColorChangerLogin()
    app.exec_()


if __name__ == '__main__':
    main()
