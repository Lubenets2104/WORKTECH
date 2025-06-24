from pydantic import BaseModel
from datetime import date


# --- User ---

class UserBase(BaseModel):
    name: str
    is_manager: bool


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    model_config = {
        "from_attributes": True
    }


# --- Project ---

class ProjectBase(BaseModel):
    name: str


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int

    model_config = {
        "from_attributes": True
    }


# --- TimeEntry ---

class TimeEntryBase(BaseModel):
    user_id: int
    project_id: int
    date: date
    hours: int


class TimeEntryCreate(TimeEntryBase):
    pass


class TimeEntry(TimeEntryBase):
    id: int

    model_config = {
        "from_attributes": True
    }
