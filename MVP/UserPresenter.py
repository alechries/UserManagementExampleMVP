from MVP.UserModule import UserModule
from MVP.UserView import UserView
import sys
from PyQt5 import QtWidgets


class UserPresenter:

    def __init__(self):

        self.__module = UserModule()
        app = QtWidgets.QApplication([])
        self.__view = UserView(self.__module)
        self.__view.show()
        sys.exit(app.exec())
