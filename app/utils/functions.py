from app.schemas.schemas import CardNumber


def lunh_algorithm(card_no: CardNumber):
    """
    Validates if the data entered corresponds to a valid credit card number.
    """

    sum = 0
    num_digits = len(card_no)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_no[count])
        digit = digit * 2 if not ((count & 1) ^ oddeven) else digit
        digit = digit - 9 if digit > 9 else digit

        sum = sum + digit

    return ((sum % 10) == 0)


def identify_franchise(card_no: CardNumber):
    """
    Verify which financial institution the credit card number entered belongs to.
    """

    maestro = (5018, 5020, 5038, 5893, 6304, 6759, 6761, 6762, 6763)
    diners_club = (300, 301, 302, 303, 304, 305)
    visa_electron = (4026, 4508, 4844, 4913, 4917)
    masterCard = (51, 52, 53, 54, 55)
    american_express = (34, 37)
    
    discover = (60,62,64,65)

    if int(card_no[:2]) in american_express:
        return f'American Express'
    elif int(card_no[:4]) in visa_electron:
        return f'Visa Electron'
    elif int(card_no[:3]) in diners_club:
        return f'Diners Club'
    elif int(card_no[:2]) in masterCard:
        return f'MasterCard'
    elif int(card_no[:2]) in discover:
        return f'Discover'
    elif int(card_no[:4]) in maestro:
        return f'Maestro'
    elif int(card_no[0]) == 4:
        return f'Visa'
    else:
        return f'Not Found'
