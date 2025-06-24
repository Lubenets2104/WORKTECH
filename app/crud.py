from sqlalchemy.orm import Session
from datetime import date
from sqlalchemy import func
from app import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def create_time_entry(db: Session, entry: schemas.TimeEntryCreate):
    db_entry = models.TimeEntry(**entry.model_dump())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_users(db: Session):
    return db.query(models.User).all()

def get_projects(db: Session):
    return db.query(models.Project).all()

def get_time_entries(db: Session):
    return db.query(models.TimeEntry).all()


def get_project_report(db: Session, project_id: int, start_date: date, end_date: date):
    result = db.query(
        models.TimeEntry.user_id.label("id"),
        func.sum(models.TimeEntry.hours).label("hours")
    ).filter(models.TimeEntry.project_id == project_id) \
        .filter(models.TimeEntry.date >= start_date) \
        .filter(models.TimeEntry.date < end_date) \
        .group_by(models.TimeEntry.user_id) \
        .all()

    return [{"id": row.id, "hours": row.hours} for row in result]

