from sqlalchemy import Column, Integer, String

from database import Base

class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key = True)
    e_mail = Column(String(50), unique = True, nullable = False)
    username = Column(String(20), unique = True, nullable = False)
    password = Column(String(16), nullable = False)

class Podcast(Base):
    __tablename__= 'Podcast'

    id = Column(Integer, primary_key = True)
    title = Column(String(100),  nullable = False)
    image = Column(String(100))
    audio = Column(String(100), nullable = False)
    description = Column(String(500))
