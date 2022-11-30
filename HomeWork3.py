# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.

n = int(input('Введите число: '))
dct = {}
sum=0
for i in range(1, n+1):
    dct[i] = round(((1 + (1/i))**n), 2)
    print(dct[i], end=" ") 
    sum+=dct[i]
print()
print(sum)   

