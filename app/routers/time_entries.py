from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db
from datetime import date

router = APIRouter(prefix="/time-entries", tags=["time entries"])

@router.post("/", response_model=schemas.TimeEntry)
def create_entry(entry: schemas.TimeEntryCreate, db: Session = Depends(get_db)):
    return crud.create_time_entry(db, entry)

@router.get("/", response_model=list[schemas.TimeEntry])
def read_entries(db: Session = Depends(get_db)):
    return crud.get_time_entries(db)

@router.get("/report/")
def project_report(
    project_id: int,
    start_date: date,
    end_date: date,
    db: Session = Depends(get_db)
):
    return crud.get_project_report(db, project_id, start_date, end_date)
