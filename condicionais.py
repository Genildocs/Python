import math


def ponto():
    print('-'*50)
#if
# number1 = int(input('Digite um numeros? '))
# number2 = int(input('Digite um numeros? '))
#
# if number1 > number2:
#     print('Number1 é maior')
# else:
#     print('Number 2 é maior ou os numeros são iguais')
ponto()
# # Escreva um programa que leia três numeros e que imprime o maior e o menor
# num1 = int(input('Digite um numero? '))
# num2 = int(input('Digite um numero? '))
# num3 = int(input('Digite um numero? '))
#
# maior = num1
# if num2 > maior:
#     maior = num2
# if num3 > maior:
#     maior = num3
#
#
# menor = num1
# if num2 < maior:
#     menor = num2
# if num3 < maior:
#     menor = num3
#
# if maior == menor:
#     print('São iguais')
#
#
# print(maior, menor)
#
# maior =max(num1,num2,num3)
# menor =min(num1,num2,num3)
# print(maior)
ponto()
# Aumento de salario
# salario = float(input('Qual seu salario? '))
# aumento1 = float(input('Digite a porcentagem de aumento? ')) / 100
# aumento2 = 0.10
# total = 0;
# if salario > 1250:
#     total = salario + (salario * aumento1)
# else:
#     total = salario + (salario * aumento2)
# print(f'Seu salario após o aumentou é de: {total}.')
print()
# calculadora
num1 = int(input('Digite um numero? '))
num2 = int(input('Digite mais um numero? '))
operacao = input('Digite a operação que deseja realizar, para: \n'
                 'Multiplicação: 1 \n'
                 'Divisão: 2 \n'
                 'Soma: 3 \n'
                 'Subtração: 4 \n'
                 'Potência: 5 \n'
                 'Digite sua opção: ')

if operacao == '1':
    print(num1 * num2)
elif operacao == '2':
    print(num1 / num2)
elif operacao == '3':
    print(num1 + num2)
elif operacao == '4':
    print(num1 - num2)
elif operacao == '5':
    print(pow(num1,num2))
else:
    print('Opção invalidade!')