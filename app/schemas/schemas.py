from pydantic import BaseModel


class CardNumber(BaseModel):
    card_number: str
