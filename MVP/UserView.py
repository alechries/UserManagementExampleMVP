from MVP.UserModule import UserModule
from Modules.Design import Ui_MainWindow
from Modules.Entities import User
from PyQt5 import QtWidgets, QtCore


class UserView(QtWidgets.QMainWindow):
    
    def __init__(self, module: UserModule):

        super(UserView, self).__init__()
        self.module = module

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.ui.add_btn.clicked.connect(self.add_btn_click_event)
        self.ui.del_btn.clicked.connect(self.del_btn_click_event)
        self.ui.cls_btn.clicked.connect(self.cls_btn_click_event)
        self.ui.fnd_btn.clicked.connect(self.fnd_btn_click_event)

    def add_btn_click_event(self):

        name = self.ui.name_edit.text()
        surname = self.ui.surname_edit.text()
        prof = self.ui.prof_edit.text()

        if len(name) == 0 or len(surname) == 0 or len(prof) == 0:
            self.ui.phrase_label.setText("Hey dude you didn't enter something")
            return

        user = User(name=name, surname=surname, profession=prof)
        self.module.add_users([user, ])
        self.fnd_btn_click_event()

        self.ui.phrase_label.setText("Bro, I added a user")

    def del_btn_click_event(self):

        item = self.ui.list_widget.currentItem()
        if item is None:
            self.ui.phrase_label.setText("Hmm... you didn't choose who to delete")
            return

        text = item.text()
        number = int(text.split()[0])

        self.module.del_user_by_id(number)
        self.ui.list_widget.removeItemWidget(item)
        self.fnd_btn_click_event()

        self.ui.phrase_label.setText("Well, I deleted it, man, what's next?")

    def cls_btn_click_event(self):

        self.ui.name_edit.clear()
        self.ui.surname_edit.clear()
        self.ui.prof_edit.clear()
        self.ui.list_widget.clear()

        self.ui.phrase_label.setText("I have cleared all fields and table")

    def fnd_btn_click_event(self):

        name = self.ui.name_edit.text() or None
        surname = self.ui.surname_edit.text() or None
        prof = self.ui.prof_edit.text() or None
        list_widget = self.ui.list_widget
        users = self.module.get_user(name=name, surname=surname, profession=prof)
        list_widget.clear()

        if len(users) == 0:
            self.ui.phrase_label.setText("Oops, brooo, but found no one")
            return

        for user in users:
            item = QtWidgets.QListWidgetItem()
            item.setText(f"{int(user.id)} User {user.name} {user.surname} with profession {user.profession}")
            list_widget.addItem(item)

        self.ui.phrase_label.setText("Here are all your bros that needed")
