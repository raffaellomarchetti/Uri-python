from string import ascii_uppercase
alfa_pos = {}
for letra in ascii_uppercase:
    alfa_pos[letra] = ascii_uppercase.index(letra)
n = int(input())
while n >0:
    l = int(input())
    linha = []
    while l > 0:
        linha.append(input())
        l=l-1
    valor = 0
    for index_linha in range(len(linha)):
        elemento_index = index_linha
        for index_letra in range(len(linha[elemento_index])):
            valor = valor + alfa_pos[linha[elemento_index][index_letra]]+ elemento_index + index_letra
    print(valor)
    n=n-1