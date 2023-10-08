def convert(number):
    """В возврящаемую строку дописываются:
    'Pling', если число number делится на 3,
    'Plang', если число number делится на 5,
    'Plong', если число number делится на 7,
    само число number, если оно не делится ни на 3, ни на 5, ни на 7."""
    # Напишите ваш код здесь
    s = ''
    if number % 3 == 0:
        s += 'Pling'
    if number % 5 == 0:
        s += 'Plang'
    if number % 7 == 0:
        s += 'Plong'
    if s == '':
        return str(number)
    else:
        return (s)