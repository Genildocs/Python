from random import sample
# def coordenadas():
#     return (10,20)
# x,y = coordenadas()
#
# lache = ("Suco","Hamburguer","Sorvete")
#
# for c in lache:
#     print(c)


#EXERCICIO 72
# numeros_por_extenso = (
#     "zero", "um", "dois", "três", "quatro",
#     "cinco", "seis", "sete", "oito", "nove",
#     "dez", "onze", "doze", "treze", "catorze",
#     "quinze", "dezesseis", "dezessete", "dezoito",
#     "dezenove", "vinte"
# )
#
# num = int(input("Digite um numero de 0 a 20: "))
# while True:
#     if num >= 0 and num <= 20:
#        print(f'Você digitou o numero {numeros_por_extenso[num]}.')
#        break
#     else:
#         num = int(input("Tente novamente. Digite um numero de 0 a 20: "))

# EXERCICIO 74
# numbers = sample(range(1, 100), 5)
# sort = tuple(numbers)
# print(f'Os valores sorteados foram: {sort}')
# print(f'O menor valor dentro da tupla é {min(sort)}')
# print(f'O maior valor dentro da tupla é {max(sort)}')

# EXERCICIO 75
# numbers = (int(input("Digite um numero: ")), int(input("Digite outro numero: ")), int(input("Digite mais um numero: ")), int(input("Digite o ultimo numero: ")))
# print(f'Você digitou os numeros {numbers}')
# print(f'O valor 9 apareceu {numbers.count(9)}')
# if 3 in numbers:
#     print(f'O valor 3 apareceu na {numbers.index(3) + 1}º posição')
# else:
#     print("O valor 3 não foi digitado em nenhuma posição")
# cont = 0
# for num in numbers:
#     if num % 2 == 0:
#         cont += 1
# print(f"Os valores pares digitados foram {cont}")

