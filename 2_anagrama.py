"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 * - las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def anagrama(word1:str, word2: str) -> bool:
    word1 = list(word1.lower())
    word2 = list(word2.lower())

    word1.sort()
    word2.sort()

    if word1 == word2:
        return True
    else:
        return False

if __name__ == "__main__":
    n1 = input()
    n2 = input()
    print(anagrama(n1, n2))