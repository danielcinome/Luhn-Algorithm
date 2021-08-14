from app.managers.manager import CreditCard
from app.schemas.schemas import CardNumber
from fastapi import APIRouter

router = APIRouter()

@router.post("/credit_card")
def validate_credit_card(card_sc: CardNumber):
    """
    Validación de la Tarjeta de Crédito e identificación de la entidad a la que pertenece:

    - **card_number**: Número de Tarjeta de Credito proporcionada por el Usuario
    """
    return CreditCard.validate_card_no(card_sc.card_number)
