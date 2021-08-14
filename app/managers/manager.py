
from app.schemas.schemas import CardNumber
from app.utils.functions import identify_franchise, lunh_algorithm
from fastapi import HTTPException, status


class CreditCard():

    @staticmethod
    def validate_card_no(card_number: CardNumber):
        card_number = card_number.translate(str.maketrans('', '', ' \n\t\r'))
        if not card_number.isdigit():
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='La tarjeta de credito ingresada no es un número')
        else:
            valid_card = lunh_algorithm(card_number)
            if valid_card:
                franchise = identify_franchise(card_number)
                return {
                    'luhn_valid': valid_card,
                    'card_type': franchise
                }
            else:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Tarjeta invalida')
