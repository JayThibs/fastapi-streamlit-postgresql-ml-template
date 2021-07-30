from sqlalchemy import Integer, Float
from sqlalchemy.sql.schema import Column
from .database import Base


class BankNote(Base):
    __tablename__ = "banknote"

    id = Column(Integer, primary_key=True)
    variance = Column(Float, nullable=False)
    skewness = Column(Float, nullable=False)
    curtosis = Column(Float, nullable=False)
    entropy = Column(Float, nullable=False)
