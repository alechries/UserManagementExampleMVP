from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sqlalchemy.db')
created_session_maker = sessionmaker(bind=engine)
session: Session = created_session_maker()

Base = declarative_base()


class User(Base):
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    profession = Column(String(250), nullable=False)

    def __init__(self, name, surname, profession):

        self.name = name
        self.surname = surname
        self.profession = profession


Base.metadata.create_all(bind=engine)
