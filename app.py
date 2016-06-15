from messenger.MessengerAPI.Messenger import Messenger
from PySide import QtGui
from PySide.QtCore import *
from PySide.QtGui import *
import sys, json, os

#for tests:
#id 100002217879841
#color #2137ff

class MessengerColorChanger(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MessengerColorChanger, self).__init__(parent)
        global instance
        instance = self
        self.setupUi()

    def setupUi(self):
        # Todo: lista konf
        # todo: szukajka konf
        grid = QtGui.QGridLayout()
        grid.setSpacing(5)

        self.infobox = QtGui.QLineEdit()
        self.infobox.setEnabled(False)

        grid.addWidget(self.infobox, 0, 0, 1, 0)

        # login
        self.login = QtGui.QLineEdit()
        self.login.setMaxLength(128)

        login_label = QtGui.QLabel("Login")

        grid.addWidget(login_label, 1, 0)
        grid.addWidget(self.login, 1, 1)

        # password
        # TODO: "pokaz haslo"
        self.password = QtGui.QLineEdit()
        self.password.setMaxLength(64)
        self.password.setEchoMode(QtGui.QLineEdit.Password)

        password_label = QtGui.QLabel("Hasło")

        grid.addWidget(password_label, 2, 0)
        grid.addWidget(self.password, 2, 1)

        # pokaz haslo
        self.show_password = QtGui.QCheckBox("Pokaż hasło", self)
        self.show_password.clicked.connect(self.show_password_text)

        grid.addWidget(self.show_password, 3, 0)

        # id
        self.id = QtGui.QLineEdit()

        id_label = QtGui.QLabel("ID rozmowy")

        grid.addWidget(id_label, 4, 0)
        grid.addWidget(self.id, 4, 1)

        # color
        # todo: color picker
        self.color = QtGui.QLineEdit()
        self.color.setMaxLength(8)
        #self.color = QtGui.QColorDialog()

        color_label = QtGui.QLabel("Kolor")

        grid.addWidget(color_label, 5, 0)
        grid.addWidget(self.color, 5, 1)

        # button
        self.button = QtGui.QPushButton()
        self.button.setText("Do dzieła!")
        print("debug 1")
        self.button.clicked.connect(self.button_click)
        print("debug 2")
        grid.addWidget(self.button, 6, 0, 1, 0)

        # zapamietaj
        # TODO: działać
        self.remember_checkbox = QtGui.QCheckBox("Zapamiętaj hasło (odznacz aby usunąc zapisane dane)", self)
        self.remember_checkbox.clicked.connect(self.remember_save)

        grid.addWidget(self.remember_checkbox, 7, 0, 1, 0)

        # zaladuj dane
        self.remember_load()

        # window
        self.setLayout(grid)

        self.setGeometry(600, 300, 600, 250)  # polozeniex, polozeniey, x, y
        self.setWindowTitle("Messenger Color Changer")
        self.show()


    def button_click(self):
        instance.infobox.setText("Sprawdzam dane...")
        print("debug start")
        print(instance.login.text())
        print("debug 3")
        #print(instance.password.text())
        print("debug 4")
        print(instance.id.text())
        print("debug 5")
        print(instance.color.text())
        print("debug 6")
        if not self.go(instance.login.text(), instance.password.text(), instance.id.text(), instance.color.text()):
            print("debug = brakuje czegos")
            instance.infobox.setText("Któreś z poniższych pól jest puste lub dane są nieprawidłowe!")
            QMessageBox.critical(self, "Błędzik", "Któreś z powyższych pól jest puste lub dane są nieprawidłowe.", QMessageBox.Ok)
        else:
            print("debug = ok")
            instance.infobox.setText("Kolor zmieniony!")
        print("debug end")
        print("")

    def go(self, login, password, id, color):
        if not str(login).strip():
            return False
        if len(str(login)) < 5:
            return False
        if not str(password).strip():
            return False
        if len(str(password)) < 5:
            return False
        if not str(id).strip():
            return False
        if not str(color).strip():
            return False
        if len(str(color)) < 6:
            return False
        try:
            messenger = Messenger(login, password)
            konfa = messenger.get_thread(int(id))
            konfa.set_custom_color(color)
            instance.infobox.setText("Kolor zmieniony!")
            if instance.remember_checkbox.checkState():
                self.remember_save()
            else: #remove data.json if remeber checkbox is unchecked
                try:
                    os.remove("data.json")
                except FileNotFoundError:
                    print("data.json not found")
                except:
                    print("Unexpected error:", sys.exc_info()[0])
            return True
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return False

    def show_password_text(self):
        if instance.show_password.checkState():
            instance.password.setEchoMode(QtGui.QLineEdit.Normal)
        else:
            instance.password.setEchoMode(QtGui.QLineEdit.Password)

    def remember_save(self):
        dict = {
            "login": instance.login.text(),
            "password": instance.password.text(),
            "id": instance.id.text(),
            "color": instance.color.text()
        }
        with open('data.json', 'w') as fp:
            json.dump(dict, fp) #write json to data.json

    def remember_load(self):
        try:
            with open('data.json', 'r') as fp:
                data = json.load(fp)
                instance.login.setText(data['login'])
                instance.password.setText(data['password'])
                instance.id.setText(data['id'])
                instance.color.setText(data['color'])
                instance.remember_checkbox.setChecked(1)
        except:
            print("Unexpected error:", sys.exc_info()[0])


def main():
    app = QApplication(sys.argv)
    frame = MessengerColorChanger()
    app.exec_()


if __name__ == '__main__':
    main()
