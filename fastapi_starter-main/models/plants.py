from .base import Base
from datetime import date


class Plants(Base, table=True):
    __tablename = "plants"

    common_name: str
    scientific_name: str
    date_of_purchase: date 
    # this may need to be adjusted to return the chosen date
    location_of_purchase: str
    condition_of_purchase: str
    current_condition: str

    # future adds would be container material and water date 
    