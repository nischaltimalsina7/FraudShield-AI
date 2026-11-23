

# Import tools for defining and validating data
from pydantic import BaseModel, Field


# Define the required transaction information
class TransactionInput(BaseModel):
    amount: float = Field(ge=0)
    merchant_category: str
    transaction_hour: int = Field(ge=0, le=23)
    card_type: str
