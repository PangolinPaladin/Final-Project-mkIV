from .base import Base

class DatePurchased(Base, table=True):
    __tablename__ = "datepurchased"

    date: str