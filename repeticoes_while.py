# While(condiçao): <bloco>
#numero = int(input("Digite um numero? "))
import datetime
import time

# exibir numero de 1 a 100
# x = 1
# while x <= 100:
#     print(x, end=' ' )
#     x += 1
# print('----')
# x = 10
# c = 0
# while x >= 0:
#     time.sleep(1)
#     print(x, end=' ')
#     x-= 1
#
# print('\nFogo!')

# Acumuladores

# count = 1
# acum = 0
#
# while count <= 5:
#     x = int(input(f'Digite o {count} numero: '))
#     acum += x
#     count += 1
#
# print(acum / 5)

#Exercicio com acumulador
# print('****BANCO DA POUPANÇA DO BRASIL****')
# tempo_deposito = int(input('Por favor informe a quantidade meses que quer deixar seu dinheiro depositado? '))
# deposito_inicial = float(input("Digite um valor que deseja depositar em sua poupança? R$ "))
# taxa_juros_mes = (7.14 / 12) / 100
# dep_mensal = float(input('Se deseja efetuar um dep mensal, digite o valor? R$ '))
# def anos_de_deposito(meses):
#     x = 1
#     saldo = deposito_inicial
#     while x <= meses:
#         saldo += (saldo * taxa_juros_mes)
#         if x >= 2:
#             saldo += dep_mensal
#         x += 1
#     print(f'Saldo total em {meses} meses: {saldo:.2f}')
# anos_de_deposito(tempo_deposito)
print('--'*26)
#Exercicio de divida
print('****COBRANÇAS MEIRELIS****')

def divida():
    divida_inicial = float(input('Digite o valor inicial da divida? R$ '))
    return divida_inicial
divida = divida()
def juros_mensais():
    juros = float(input('Digite os juros mensais da dividas? '))
    return juros
juros = juros_mensais()
def pagamento_cliente():
    pagamento = float(input("Digite o valor mensal que o cliente deseja pagar? R$ "))
    return pagamento
def calculo_divida():
    saldo_divida = divida
    juros_mensal = juros
    pagamento_mensal = pagamento_cliente()
    meses = 1
    tot_juros = 0
    tot_pago = pagamento_mensal
    while meses <= saldo_divida:
        saldo_divida = saldo_divida + (saldo_divida * juros / 100)
        saldo_divida -= pagamento_mensal
        meses += 1
        tot_juros += juros_mensal
        tot_pago += pagamento_mensal
        tot_divida = divida + (divida * (tot_juros / 100))
    return print(f'Divida de R$ {divida} foi paga em {meses} meses com um total de {tot_juros:.2f}% de juros e pagamento total de R${tot_divida:.2f}, pagamento'
                 f' realizado pelo cliente {tot_pago}')
calculo_divida()