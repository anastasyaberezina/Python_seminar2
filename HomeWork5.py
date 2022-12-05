# Реализуйте алгоритм генерации случайного числа.(Не используя библиотеки связанные с рандомом) (Доп задача, не влияющая на оценку )

def Ex5(first=0, last=100):
    import time
    ran=int(str(time.time())[-3:])
    while True:
        if ran<first:
            ran+=(last-first)
        if ran>last:
            ran-=(last-first)
        if first<=ran<=last:
            return ran
            break
print(Ex5(10, 100))    