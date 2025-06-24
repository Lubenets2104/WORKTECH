from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_manager = Column(Integer, default=0)  # 0 = нет, 1 = да

    time_entries = relationship("TimeEntry", back_populates="user")

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    time_entries = relationship("TimeEntry", back_populates="project")

class TimeEntry(Base):
    __tablename__ = "time_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    date = Column(Date)
    hours = Column(Integer)

    user = relationship("User", back_populates="time_entries")
    project = relationship("Project", back_populates="time_entries")
