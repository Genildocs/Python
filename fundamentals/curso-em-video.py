# nome = str(input("Digite seu nome completo: ")).lstrip()
# print(f'Seu nome em  maiusculo é: {nome.upper()}')
# print(f'Seu nome em  minusculo é: {nome.lower()}')
# print(f'Seu nome possui: {len(nome.replace(" ", ""))} letras')
# primeiroNome = nome.split()
# print(f'Seu primeiro nome é {primeiroNome[0]} e tem {len(primeiroNome[0])} letras')
#


# verificar se o nome de uma cidade começa com "SANTOS"
# city = str(input("Digite o nome de uma cidade: ")).strip().upper()
#
# if city[:5] == "SANTO":
#     print(True)
# else:
#     print(False)
#

# EXERCICIO 25
# nome = str(input("Digite seu nome completo: ")).strip().upper()
# print(f'Seu nome tem Silva? {nome.count("SILVA") == 1}')

# EXERCICIO 26
# frase = str(input("Digite uma frase: ")).strip().lower()
#
# if 'a' in frase:
#     print(f'A letra A aparece {frase.count("a")} vezes na frase')
#     print(f'A primeira letra A aparece na posicao {frase.find("a") + 1}.')
#     print(f'A ultima letra A aparece na posicao {frase.rfind("a") + 1 }.')

# EXERCICIO 33
# n1 = int(input("Primeiro valor: "))
# n2 = int(input("Segundo valor: "))
# n3 = int(input("Terceira valor: "))
# n4 = int(input("Quarto valor: "))
# valores = [n1,n2,n3,n4]
# valores.sort()
# print(f'O menor valor digitado foi {valores[0]}')
# print(f'O maior valor digitado foi {valores[len(valores) - 1]}')

#EXERCICIO 47
# for i in range(2, 51, 2):
#    print(i, end=' ')

# EXERCICIO 48
# sum = 0
# acc = 0
# for i in range(3,500, 3):
#    if i % 2 == 1:
#        sum += i
#        acc += 1
#
# print(f'A soma de todos os {acc} solicitados é {sum}.')

# EXERCICIO 50
# sum = 0
# for n in range(1,7):
#     num = int(input(f'Digite o {n} numero: '))
#     if num % 2 == 0:
#         sum += num
#
#
# print(f'A soma dos numeros pares é: {sum}')

#EXERCICIO 53
# frase = str(input('Digite uma frase: ')).lower().replace(" ", "")
# inversao_da_palavra = frase[::-1]
# if inversao_da_palavra == frase:
#     print("A frase é um palíndromo")
# else:
#     print("A frase não é um palíndromo")


#EXERCICIO 57
# while True:
#     sexo = str(input("Informe seu sexo: [M/F] ")).strip()
#     if sexo != '' and sexo in 'MmFf':
#         print(f'Sexo informado {sexo.upper()}')
#         break
#     else:
#         print("Dados invalidos")