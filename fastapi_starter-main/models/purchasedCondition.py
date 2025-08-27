from .base import Base

class PurchasedCondition(Base, table=True):
    __tablename__ = "purchasedcondition"

    history: str