import uvicorn
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

from datetime import datetime, timedelta, timezone
from sqlmodel import Session, select

import config

from models.plants import Plants

from db import get_session

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/")
async def root():
    return {"message": "Plants make life better"}

# DELETE THE ROUTES BELOW
# DEMO PURPOSES ONLY

# READ data


@app.get("/plants")
async def get_all_plants(session: Session = Depends(get_session)):
    statement = select(Plants)
    giveResults = session.exec(statement).all()
    return giveResults

# READ specific data


@app.get("/plants/{id}")
async def get_single_plant(id: str, session: Session = Depends(get_session)):
    statement = select(Plants).where(Plants.id == id)
    result = session.exec(statement).one()
    return result

# CREATE data


@app.post("/plants/add")
async def add_plants(payload: Plants, session: Session = Depends(get_session)):
    new_plant = Plants(
        title=payload.title, 
        common_name=payload.common_name,
        scientific_name=payload.scientific_name,
        date_of_purchase=payload.date_of_purchase,
        location_of_purchase=payload.location_of_purchase,
        condition_at_purchase=payload.condition_at_purchase,
        current_condition=payload.current_condition)
    session.add(new_plant)
    session.commit()
    session.refresh(new_plant)
    return {"message": f"Congratulations on your new plant! {new_plant.id}"}

@app.post("/create")
async def create_todo(
    text: str, 
    is_complete: bool = False):
    todo = Todo(text=text, is_done=is_complete)
    session.add(todo)
    session.commit()
    return {"todo added": todo.text}

if __name__ == '__main__':
    uvicorn.run('main:app', 
    host='localhost', 
    port=8000, 
    reload=True)


    # common_name: str
    # scientific_name: str
    # date_of_purchase: date 
    # this may need to be adjusted to return the chosen date
    # location_of_purchase: str
    # condition_at_purchase: str
    # current_condition: str