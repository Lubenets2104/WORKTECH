from fastapi import FastAPI
from app.database import Base, engine
from app.routers import projects, users, time_entries

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(projects.router)
app.include_router(time_entries.router)
