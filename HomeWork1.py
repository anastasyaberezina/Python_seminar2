# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = int(input('Введите число: '))

def Amount (num):
    res = 0
    while(num>0):
        num2=num%10
        res+=num2
        num=num//10
    return res
print(Amount(number))       

