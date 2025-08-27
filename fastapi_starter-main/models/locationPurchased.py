from .base import Base

class LocationPurchased(Base, table=True):
    __tablename__ = "locationpurchased"
    location: str
    