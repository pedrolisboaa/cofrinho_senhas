from string import punctuation, ascii_letters, digits
from random import choices, shuffle

def gerador_de_senha(caracateres=5, letras=5, numeros=5):
    CARACTERES = list(punctuation)
    LETRAS = list(ascii_letters)
    NUMEROS = list(digits)

    senha_forte = choices(CARACTERES, k=caracateres) + choices(LETRAS, k=letras) + choices(NUMEROS, k=numeros)
    shuffle(senha_forte)

    return ''.join(senha_forte)

