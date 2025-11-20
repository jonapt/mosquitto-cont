#!/usr/bin/env python3
"""
generador.py
Generador de contraseñas seguras para usar desde terminal:

    python generador.py username
    python generador.py username -l 20 --copy

Salida: imprime la contraseña en stdout (y opcionalmente la copia al portapapeles).
"""

import argparse
import secrets
import string
import sys

def generar_password(length: int = 16) -> str:
    """Genera una contraseña segura que garantiza al menos
    una minúscula, una mayúscula, un dígito y un símbolo.
    """
    if length < 4:
        raise ValueError("length must be >= 4")

    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%&*()-_=+[]{}<>?/:;"

    # Aseguramos al menos uno de cada categoría
    password_chars = [
        secrets.choice(lowers),
        secrets.choice(uppers),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    # Resto de caracteres elegidos aleatoriamente del conjunto completo
    all_chars = lowers + uppers + digits + symbols
    remaining = length - len(password_chars)
    password_chars += [secrets.choice(all_chars) for _ in range(remaining)]

    # Mezclamos para que la posición no sea predecible
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)

def main():
    parser = argparse.ArgumentParser(description="Generador de contraseñas seguras")
    parser.add_argument("username", help="Nombre de usuario (se acepta pero no se usa para derivar la contraseña por seguridad)")
    parser.add_argument("-l", "--length", type=int, default=16, help="Longitud de la contraseña (por defecto: 16)")
    parser.add_argument("--copy", action="store_true", help="Copiar contraseña al portapapeles (requiere pyperclip)")
    args = parser.parse_args()

    try:
        pwd = generar_password(args.length)
    except ValueError as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(1)

    # Mostrar resultado
    print(pwd)

    if args.copy:
        try:
            import pyperclip
            pyperclip.copy(pwd)
            print("(copiado al portapapeles)")
        except Exception:
            print("(no se pudo copiar: instala 'pyperclip' o configura el portapapeles)", file=sys.stderr)

if __name__ == "__main__":
    main()
