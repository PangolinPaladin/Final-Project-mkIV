import uvicorn
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

from datetime import datetime, timedelta, timezone
from sqlmodel import Session, select

import config

from models.Plant import Plants

from models.CommonName import CommonName
from models.LocationPurchased import LocationPurchased
from models.CurrentCondition import CurrentCondition
from models.ScientificName import ScientificName
from models.PurchasedCondition import PurchasedCondition
from models.DatePurchased import DatePurchased



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


# @app.get("/plants")
# async def get_all_plants(session: Session = Depends(get_session)):
 #   statement = select(Plants, ScientificName).join(ScientificName, Plants.scientificname_id == ScientificName.id)
  #  giveResults = session.exec(statement).all()

   # result_list = []
   # for plant, scientific_name in giveResults:
    #    plant_details = {
     #       "common_name": plant.commonname_id,
      #      "scientific_name": scientific_name.latinname,
       # }
      #  result_list.append(plant_details)
   # return result_list

@app.get("/plants")
async def get_all_plants(session: Session = Depends(get_session)):
    statement= select(Plants, CommonName, CurrentCondition, LocationPurchased, PurchasedCondition, ScientificName).join(CommonName, Plants.commonname_id == CommonName.id).join(CurrentCondition, Plants.currentcondition_id == CurrentCondition.id).join(LocationPurchased, Plants.locationpurchased_id ==LocationPurchased.id).join(PurchasedCondition, Plants.purchasedcondition_id ==PurchasedCondition.id).join(ScientificName, Plants.scientificname_id ==ScientificName.id)
    #statement = select(Plants, CommonName, CurrentCondition, LocationPurchased, PurchasedCondition, ScientificName).join(CommonName).join(CurrentCondition).join(
        #LocationPurchased).join(PurchasedCondition).join(ScientificName)
    giveResults = session.exec(statement).all()
   
    result_list = []
    for plant, common_name, current_condition, location_purchased, purchased_condition, scientific_name in giveResults:
        plant_details = {
            "common_name": common_name.name,
            "current_condition": current_condition.condition,
            "location_purchased": location_purchased.location,
            "purchased_condition": purchased_condition.condition,
            "scientific_name": scientific_name.latinname,
        }
        result_list.append(plant_details)

        
        return result_list

# READ specific data


@app.get("/plants/{id}")
async def get_single_plant(id: str, session: Session = Depends(get_session)):
    statement = select(Plants, CommonName, CurrentCondition, LocationPurchased, PurchasedCondition, ScientificName).join(CommonName).join(CurrentCondition).join(
        LocationPurchased).join(PurchasedCondition).join(ScientificName).where(Plants.id == id)
    result = session.exec(statement).one()
    plant, common_name, current_condition, location_purchased, purchased_condition, scientific_name = result
    return result


@app.get("/singleplants/{id}")
async def get_single_plant(id: str, session: Session = Depends(get_session)):
    statement = select(Plants).where(Plants.id == id)
    statement = select(Plants, CommonName, CurrentCondition, LocationPurchased, PurchasedCondition, ScientificName).join(CommonName).join(CurrentCondition).join(
        LocationPurchased).join(PurchasedCondition).join(ScientificName).where(Plants.id == id)
    result = session.exec(statement).one()
    return result

# CREATE data

# for below!! where does the latinname interaction happen? 
# I believe this is Plants not Plant, becuase it is calling the class not the model

@app.post("/plants/add")
async def add_plant(payload: Plants, session: Session = Depends(get_session)):
    new_plant = Plants(payload: commonname=payload.commonname, scientificname=payload.scientificname, locationpurchased=payload.locationpurchased, purchasedcondition=payload.purchasedcondition, datepurchased=payload.datepurchased, currentcondition=payload.currentcondition)

    session.add(new_plant)
    session.commit()
    session.refresh(new_plant)
    return {"message": f"Congratulations on your new plant! {new_plant.id}"}

# commonname_id: str
# scientificname_id: str
# locationpurchased_id: str
# purchasedcondition_id: str
# datepurchased_id: str
# currentcondition_id: str

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