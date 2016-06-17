from messenger.MessengerAPI.Messenger import Messenger
from PySide import QtGui
from PySide.QtGui import *
import sys, json, os

# druga wersja zmieniacza kolorkow

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
        self.password.setMaxLength(64)
        self.password.setEchoMode(QtGui.QLineEdit.Password)

        login_button = QPushButton("Zaloguj się")
        login_button.clicked.connect(self.login_to_facebook)

        self.remember_checkbox = QCheckBox("Zapamiętaj login (bez hasła)")

        grid.addWidget(login_label, 0, 0)
        grid.addWidget(self.login, 0, 1)
        grid.addWidget(password_label, 1, 0)
        grid.addWidget(self.password, 1, 1)
        grid.addWidget(login_button, 2, 0, 1, 0)
        grid.addWidget(self.remember_checkbox, 3, 0, 1, 0)

        self.remember_load()

        self.setLayout(grid)
        self.setGeometry(600, 300, 600, 250)  # polozeniex, polozeniey, x, y
        self.setWindowTitle("Zaloguj się")
        self.show()

    def login_to_facebook(self):
        if instance.remember_checkbox.checkState():
            self.remember_save()
        else:  # remove data.json if remeber checkbox is unchecked
            try:
                os.remove("data.json")
            except FileNotFoundError:
                print("data.json not found, not removing")
            except:
                print("Unexpected error:", sys.exc_info()[0])
        login = instance.login.text()
        password = instance.password.text()
        MessengerColorChanger(login, password, self)

    def remember_save(self):
        dict = {
            "login": instance.login.text(),
        }
        with open('data.json', 'w') as fp:
            json.dump(dict, fp) #write json to data.json

    def remember_load(self):
        try:
            with open('data.json', 'r') as fp:
                data = json.load(fp)
                instance.login.setText(data['login'])
                instance.remember_checkbox.setChecked(1)
        except:
            print("Unexpected error:", sys.exc_info()[0])

class MessengerColorChanger(QtGui.QWidget):
    def __init__(self, login, password, loginwindow, parent=None):
        super(MessengerColorChanger, self).__init__(parent)
        try:
            global messenger
            messenger = Messenger(login, password)
            global instance
            instance = self
            loginwindow.hide()
            self.setupUi(messenger)
        except:
            QMessageBox.critical(self, "Błędzik", "Nieprawidłowy login lub hasło.",
                                 QMessageBox.Ok)
            print("Unexpected error:", sys.exc_info()[0])

    def setupUi(self, messenger):
        grid = QtGui.QGridLayout()
        grid.setSpacing(5)

        self.search_box = QLineEdit()
        self.search_box.textChanged.connect(self.search)
        grid.addWidget(self.search_box, 0, 0)

        self.conversation_list = QListWidget()

        self.thread_list = messenger.ordered_thread_list
        for conversation in self.thread_list:
            self.conversation_list.addItem(conversation.get_name())
        grid.addWidget(self.conversation_list, 1, 0, 1, 1)

        self.color_picker = QColorDialog()
        #default facebook colors
        self.color_picker.setCustomColor(0, 34047)
        self.color_picker.setCustomColor(1, 4505287)
        self.color_picker.setCustomColor(2, 16761600)
        self.color_picker.setCustomColor(3, 16399436)
        self.color_picker.setCustomColor(4, 14063291)
        self.color_picker.setCustomColor(5, 6724044)
        self.color_picker.setCustomColor(6, 1298195)
        self.color_picker.setCustomColor(7, 16743977)
        self.color_picker.setCustomColor(8, 15107461)
        self.color_picker.setCustomColor(9, 7751423)
        self.color_picker.setCustomColor(10, 2150133)
        self.color_picker.setCustomColor(11, 6797416)
        self.color_picker.setCustomColor(12, 13936780)
        self.color_picker.setCustomColor(13, 16735393)
        self.color_picker.setCustomColor(14, 10917319)
        self.color_picker.setCustomColor(15, 16777215) #white
        #picker options
        self.color_picker.setOption(QColorDialog.NoButtons, True)
        self.color_picker.setOption(QColorDialog.DontUseNativeDialog, True)
        grid.addWidget(self.color_picker, 1, 1, 1, 1)

        button = QPushButton("Do dzieła!")
        button.clicked.connect(self.change_color)
        grid.addWidget(button, 2, 0, 1, 0)

        self.setLayout(grid)
        self.setGeometry(600, 300, 800, 350)  # polozeniex, polozeniey, x, y
        self.setWindowTitle("Messenger Color Changer")
        self.show()

    def change_color(self):
        conversation = instance.thread_list[instance.conversation_list.currentRow()]
        print(conversation.fbid)
        color = instance.color_picker.currentColor().name()
        print(color)
        thread = messenger.get_thread(conversation.fbid)
        thread.set_custom_color(color)

    def search(self):
        #todo: async
        if instance.search_box.text() == "":
            instance.thread_list = messenger.ordered_thread_list
            for conversation in instance.thread_list:
                instance.conversation_list.addItem(conversation.get_name())
        else:
            results = messenger.search(instance.search_box.text(), 20)
            instance.thread_list = list(results.values())
            instance.conversation_list.clear()
            for conversation in instance.thread_list:
                instance.conversation_list.addItem(conversation.get_name())





def main():
    app = QApplication(sys.argv)
    frame = MessengerColorChangerLogin()
    app.exec_()


if __name__ == '__main__':
    main()
