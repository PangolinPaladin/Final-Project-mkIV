from .base import Base

class CurrentCondition(Base, table=True):
    __tablename__ = "currentcondition"

    ccondition: str