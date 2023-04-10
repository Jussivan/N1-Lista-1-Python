numeros = input("Digite uma lista de números separados por vírgula: ")
numeros_lista = numeros.split(",")
soma_impares = 0
for numero in numeros_lista:
    if int(numero) % 2 != 0:
        soma_impares += int(numero)
print("A soma dos números ímpares é:", soma_impares)