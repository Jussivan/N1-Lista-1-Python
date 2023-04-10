numeros = input("Digite uma lista de números separados por vírgula: ")
numeros_lista = numeros.split(",")
menor_numero = float('inf')
for num in numeros_lista:
    if float(num) < menor_numero:
        menor_numero = float(num)
print("O menor número é : ", menor_numero)