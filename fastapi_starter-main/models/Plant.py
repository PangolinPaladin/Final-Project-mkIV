from .base import Base
from datetime import date
from sqlmodel import Field, Session, SQLModel, create_engine



class Plants(Base, table=True):
    __tablename__ = "plants"
    commonname_id: str | None = Field(
        default=None, foreign_key="commonname.id")
    scientificname_id: str | None = Field(
        default=None, foreign_key="scientificname.id")
    locationpurchased_id: str | None = Field(
        default=None, foreign_key="locationpurchased.id")
    purchasedcondition_id: str | None = Field(
        default=None, foreign_key="purchasedcondition.id")
    datepurchased_id: str | None = Field(
        default=None, foreign_key="datepurchased.id")
    currentcondition_id: str | None = Field(
        default=None, foreign_key="currentcondition.id")



    #commonname_id: str
    #scientificname_id: str
    #locationpurchased_id: str
    #purchasedcondition_id: str
    #datepurchased_id: str
    #currentcondition_id: str

    # future adds would be container material and water date 
    