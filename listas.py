# lista_de_compras = ['Arroz','Feijão', 'Farinha', 'ovos']
# lista_de_compras[-1] = 'Manteiga'
# print(lista_de_compras)

# notas = [2,5,6,8,12,3]
# soma = 0
# count = 0
# while count < len(notas):
#     soma += notas[count]
#     count += 1
# print(soma / len(notas))

# numeros = [0,0,0,0,0]
# x = 0
# while x < 5:
#     numeros[x] = int(input(f'Número {x + 1}: '))
#     x += 1
# while True:
#     escolhido = int(input('Que posição você quer imprimir (0 para sair): '))
#     if escolhido == 0:
#         break
#     print(f'Você escolheu o numero: {numeros[escolhido - 1]}')

#copia de lista
# n = [0,5,6]
# n[0] = 8
# m = n[:] #para copiar uma lista usamos o par de colchetes com dois pontos dentro.
# m[0] = 10
# print(n)
# print(m)
# m.append('Metodo')
# print(m)
# list = []
# while True:
#     n = int(input("Digite um numero (0 para sair) :"))
#     if n == 0:
#         break
#     list.append(n)
#
# print(list)
#
# for i in list:
#     print(i)

# list_a = [1,2,3]
# list_b = [4,5,6]
# list_c = []
# list_c.extend(list_a)
# list_c.extend(list_b)
# print(list_c)

list_1 = []
list_2 = []
list_3 = []

a= 1
while True:
    n = int(input('Digite um numero para a primeira lista( 0 para sair): '))
    if n == 0:
        break
    list_1.append(n)
    a += 1

b = 1
while True:
    x = int(input('Digite um numero para a segunda lista( 0 para sair): '))
    if x == 0:
        break
    list_2.append(x)
    b += 1

list_3.extend(list_1)
list_3.extend(list_2)

x = 0
while x < len(list_3):
    # print(f'lista 3 na posição {x}: {list_3[x]}')
    x += 1



#Sem elementos repetidos
c = 0
while c < len(list_1):
    elemente = list_1[c]
    while list_1.count(elemente):
        list_1.remove(elemente)


    c += 1

print(list_1)