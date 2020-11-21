from database import Base
from sqlalchemy import Column, Integer, String

class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key = True)
    e_mail = Column(String(50), unique = True, nullable = False)
    username = Column(String(20), unique = True, nullable = False)
    password = Column(String(16), nullable = False)
