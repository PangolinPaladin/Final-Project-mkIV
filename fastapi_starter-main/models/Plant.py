from .base import Base
from datetime import date



class Plants(Base, table=True):
    __tablename__ = "plants"

    commonname_id: str
    scientificname_id: str
    locationpurchased_id: str
    purchasedcondition_id: str
    datepurchased_id: str
    currentcondition_id: str

    # future adds would be container material and water date 
    