from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey



class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  age = Column(Integer, nullable=True)

  notes = relationship("Note")



class Note(Base):
  __tablename__ = "notes"
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey("users.id"))
  category = Column(String, nullable=False)
  content = Column(String, nullable=False)

  user = relationship("User")


