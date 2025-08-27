from .base import Base


class ScientificName(Base, table=True):
    __tablename__ = "scientificname"

    latinName: str