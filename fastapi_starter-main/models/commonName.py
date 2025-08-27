from .base import Base

class CommonName(Base, table=True):
    __tablename__ = "commonname"

    name: str