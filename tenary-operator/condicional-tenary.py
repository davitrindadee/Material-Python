#Se é ou não Adulto 

varIdade = input("Digite sua idade: ")
varIdade = int(varIdade)

if varIdade >= 18:
    print("é Adulto!")
else:
    print("Não é Adulto!")

#TERNÁRIO (Operadores ternários são uma forma curta de escrever uma condição (if/else) em uma única linha.)

print("Adulto!" if varIdade >= 18 else "Não é Adulto!")

media = input("Digite a média: ")
media = int(media)
print("Aprovado!" if media >= 7 else "Reprovado!")

#Operadores Ternários c/ Laços de Decisão 

ternarioRepeticao = []

for i in range(1, 10):
    ternarioRepeticao.append(i)
print(ternarioRepeticao)

ternarioRepeticao = [numero for numero in range(1, 10):]
print(ternarioRepeticao)

#Mapeando Iterações 

lista1 = [1, 2, 3, 4, 5]
lista2 = ["a", "b", "c", "d"]
for index in range(0,len(lista1)) :
print(lista1[index])
print(lista2[index])

print(Iteracoes)

#Desafio - Operadores Ternários com Laços de Repetição

#Lista de Númros de 1 até 20 com passo 1 usando operadores ternários:

numeros = [numero for numero in range(1,20,1)]
print(numeros)


