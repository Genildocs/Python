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

# list_1 = []
# list_2 = []
# lista_3 = []
#
# a= 1
# while True:
#     n = int(input('Digite um numero para a primeira lista( 0 para sair): '))
#     if n == 0:
#         break
#     list_1.append(n)
#     a += 1
#
# b = 1
# while True:
#     x = int(input('Digite um numero para a segunda lista( 0 para sair): '))
#     if x == 0:
#         break
#     list_2.append(x)
#     b += 1
#
# lista_3.extend(list_1)
# lista_3.extend(list_2)
#
# x = 0
# while x < len(lista_3):
#     # print(f'lista 3 na posição {x}: {list_3[x]}')
#     x += 1
#
#
# #Sem elementos repetidos
# lista_3 = list_1[:]
# a = 0
# while a < len(list_2):
#     if list_2[a] not in lista_3:
#         lista_3.append(list_2[a])
#
#     a += 1
# lista_3 = list(set(lista_3))
# print(f'Lista sem numeros repetidos {lista_3}')

# lista = list(range(10))
# print(lista)

#Simulação de uma fila de banco
ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila.')
    print('ou A para realizar o atendimento. S para sair.')
    operacao = input('Operação (F, A ou S) : ')
    if operacao == 'A':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f'Cliente {atendido} atendido')
        else:
            print('fila vazia! Ninguem para atender')
    elif operacao == 'F':
        ultimo += 1 #incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == 'S':
        break
    else:
        print('Operação invalida! Digite apenas F, A ou S!')
