palavras = input("Digite uma lista de palavras separadas por vírgula: ")
palavras_lista = palavras.split(",")
palavra_mais_longa = ""
for palavra in palavras_lista:
    if len(palavra) > len(palavra_mais_longa):
        palavra_mais_longa = palavra
print("A palavra mais longa é ", palavra_mais_longa)