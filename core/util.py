from string import punctuation, ascii_letters, digits
from random import choices, shuffle

def gerador_de_senha(*args):

    caracteres, numeros, letras = args

    CARACTERES = list(punctuation)
    LETRAS = list(ascii_letters)
    NUMEROS = list(digits)


    senha_forte = choices(CARACTERES, k=int(caracteres)) + choices(LETRAS, k=int(letras)) + choices(NUMEROS, k=int(numeros))
    shuffle(senha_forte)

    return ''.join(senha_forte)


