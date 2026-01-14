"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 * - la que el siguiente siempre es la suma de los dos anteriores.
 * - 0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci():
    fib = [0, 1]
    for i in range(2, 51):
        fib.append(fib[i - 1] + fib[i - 2])
    print(*fib, sep=", ")

if __name__ == "__main__":
    fibonacci()