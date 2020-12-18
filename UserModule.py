from Entities import User
from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from Entities import engine


class UserModule:

    def __init__(self):
        created_session_maker = sessionmaker(bind=engine)
        self.session: Session = created_session_maker()

    def __del__(self):
        self.session.close()

    def add_user(self, users: List[User]):

        for user in users:
            self.session.add(user)
        self.session.commit()

    def get_user(self, name=None, surname=None, profession=None) -> List[User]:

        filters = []

        def operation(key, predicate):
            if key is not None:
                filters.append(predicate)

        operation(name, User.name == name)
        operation(surname, User.surname == surname)
        operation(profession, User.profession == profession)

        return self.session.query(User).filter(*filters).all()

    def del_user(self, user: User):
        self.session.delete(user)

    def accept_updates(self):
        self.session.commit()