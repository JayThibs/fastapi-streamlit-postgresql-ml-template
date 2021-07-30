from sqlalchemy import Integer, String, Boolean
from sqlalchemy.sql.schema import Column
from .database import Base


class BankNote(Base):
    __tablename__ = "banknote"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
