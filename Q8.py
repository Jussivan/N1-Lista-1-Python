numeros = input("Digite uma lista de números separados por vírgula: ")
numeros_lista = numeros.split(",")
maior_numero = float('-inf')
for num in numeros_lista:
    if float(num) > maior_numero:
        maior_numero = float(num)
print("O maior número é ", maior_numero)