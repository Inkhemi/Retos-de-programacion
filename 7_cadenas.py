"""
 Crea un programa que invierta el orden de una cadena de texto
 sin usar funciones propias del lenguaje que lo hagan de forma automática.
  - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invert_chain(chain: str) -> str:
    inverted_chain = ''
    for i in range(len(chain)-1, -1, -1):
        inverted_chain += chain[i]
    return inverted_chain

if __name__ == '__main__':
    print(invert_chain('Hola mundo'))
