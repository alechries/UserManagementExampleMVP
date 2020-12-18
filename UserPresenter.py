from UserModule import UserModule
from UserView import UserView


class UserPresenter:

    def __init__(self, module: UserModule, view: UserView):
        self.module = module
        self.view = view