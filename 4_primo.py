"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

def prime_number(n: int) -> bool | str:
    """
    Retorna si un número es primo o no
    :param n: Número a verificar.
    :return: True si es primo, False en caso contrario.
    """
    if n == 1 or n == 2 or n == 3:
        return True
    if n % 2 == 0 and n != 2:
        return False

    for j in range(3, int(n / 2) + 1):
        if n % j == 0:
            return False

    return True

if __name__ == "__main__":
    for i in range(1, 101):
        if prime_number(i):
            print(f"{i} es primo")
            continue
        print(f"{i} no es primo")
