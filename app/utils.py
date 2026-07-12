import secrets
from string import ascii_lowercase, ascii_uppercase, digits


def generate_short_code():
    alph = ascii_lowercase + ascii_uppercase + digits
    short_code = ''

    for _ in range(6):
        short_code += secrets.choice(alph)

    return short_code