# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

list1 = [-24, 7, 14, 0, 10, -8, -3, 1, 17] 
path='fileforHW4.txt'
data=open(path, 'r')

n = int(input('Введите позицию: '))

def PositionMulti(list1, data):
    for line in data:
        print(line) 
        res=[int(data[n-1])]*[int(list1[n-1])]
        print(res)
        return res
print(PositionMulti(list1, data))        