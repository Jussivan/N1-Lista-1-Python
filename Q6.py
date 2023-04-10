numeros = input("Digite uma lista de números separados por vírgula: ")
numeros_lista = numeros.split(",")
soma = 0
for num in numeros_lista:
    soma += int(num)
print("A soma dos números é igual a : ", soma)