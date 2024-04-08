"""
#### Exercício 3 - Comparando listas.

Receba duas listas de input do usuário. Ele digitará como um texto com os números separados por vígula. 
Para isso, pode-se utilizar o código disponibilizado que vai transformar esse texto em lista para você.

Eu quero que você me diga qual das listas tem o maior número dentro delas. 

Se a primeira lista tiver o maior número, imprima: "Primeira".
Se a segunda lista tiver o maior número, imprima: "Segunda".
Se ambas tiverem o mesmo número como maior, digite: "Ambas".

Exemplos:

----------------------------------

Digite a sua primeira lista (separando os números por vírgula): 1, 50, 2, 40
Digite a sua segunda lista (separando os números por vírgula): 0, 2, 99, 1, 1, 3

Resposta:
Segunda

----------------------------------

Digite a sua primeira lista (separando os números por vírgula): 1, 0, 2, 30
Digite a sua segunda lista (separando os números por vírgula): 9, 9, 9, 30

Resposta:
Ambas
"""

# Código para pegar as listas de input
primeira_lista = [*map(int, input("Digite a sua primeira lista (separando os números por vírgula): ").split(","))]
segunda_lista = [*map(int, input("Digite a sua segunda lista (separando os números por vírgula): ").split(","))]

# Fazer a partir daqui
maior_valor_primeira_lista = 0
maior_valor_segunda_lista = 0

for i in range(len(primeira_lista)):
    valor = primeira_lista[i]

    if i == 0:
        maior_valor_primeira_lista = valor
    elif valor > maior_valor_primeira_lista:
        maior_valor_primeira_lista = valor

for i in range(len(segunda_lista)):
    valor = segunda_lista[i]

    if i == 0:
        maior_valor_segunda_lista = valor
    elif valor > maior_valor_segunda_lista:
        maior_valor_segunda_lista = valor
        

print(maior_valor_primeira_lista, maior_valor_segunda_lista)

if maior_valor_primeira_lista > maior_valor_segunda_lista:
    print("Primeira")
elif maior_valor_primeira_lista < maior_valor_segunda_lista:
    print("Segunda")
else:
    print("Ambas")

