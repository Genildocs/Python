#Este kata consiste em multiplicar um determinado número por oito se for um número par e por nove caso contrário.
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9


print(simple_multiplication(8))