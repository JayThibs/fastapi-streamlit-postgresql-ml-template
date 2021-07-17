# Import BaseModel to enforce type hints
# Provides user friendly errors when data is invalid.
from pydantic import BaseModel

# Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float
