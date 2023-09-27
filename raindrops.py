def convert(number):
    """В возврящаемую строку дописываются:
    'Pling', если число number делится на 3,
    'Plang', если число number делится на 5,
    'Plong', если число number делится на 7,
    само число number, если оно не делится ни на 3, ни на 5, ни на 7."""
    # Напишите ваш код здесь
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        return "PlingPlangPlong"
    elif number % 3 == 0 and number % 5 == 0:
        return "PlingPlang"
    elif number % 3 == 0 and number % 7 == 0:
        return "PlingPlong"
    elif number % 5 == 0 and number % 7 == 0:
        return "PlangPlong"
    elif number % 3 == 0:
        return "Pling"
    elif number % 5 == 0:
        return "Plang"
    elif number % 7 == 0:
        return "Plong"
    else:
        return str(number)