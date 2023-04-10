numeros = input("Digite uma lista de números separados por vírgula: ")
numeros_lista = numeros.split(",")
produto = 1
for numero in numeros_lista:
    produto *= int(numero)
print("O produto dos números é:", produto)