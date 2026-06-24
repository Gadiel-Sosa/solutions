def is_armstrong_number(number):
    digitos = str(number)
    num_digitos = len(digitos)
    suma = 0

    for digito in digitos:
        suma = suma + (int(digito) ** num_digitos)

    return suma == number
    
