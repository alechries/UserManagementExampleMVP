from Modules.Entities import User
from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from Modules.Entities import engine


class UserModule:

    def __init__(self):
        
        created_session_maker = sessionmaker(bind=engine)
        self.__session: Session = created_session_maker()

    def __del__(self):
        
        self.__session.close()

    def add_users(self, users: List[User]):

        for user in users:
            self.__session.add(user)
        self.__session.commit()

    def get_user(self, name=None, surname=None, profession=None) -> List[User]:

        filters = []

        def operation(key, predicate):
            if key is not None:
                filters.append(predicate)

        operation(name, User.name == name)
        operation(surname, User.surname == surname)
        operation(profession, User.profession == profession)

        return self.__session.query(User).filter(*filters).all()

    def del_user(self, user: User):
        
        self.__session.delete(user)
        self.__session.commit()

    def del_user_by_id(self, user_id: int):

        self.__session.query(User).filter(User.id == user_id).delete()
        self.__session.commit()
