#Реализуйте выдачу случайного числа
import datetime

def input_num1():
    try:
        num1=int(input("Введи минимальное число: "))
        if num1 < 0:
            print ("Введи число больше 0")
        return num1
    except ValueError:
        print("Ввели не число, попробуй еще")
        return input_num1()

def input_num2():
    try:
        num2=int(input("Введи масимальное число: "))
        if num2 < 0:
            print ("Введи число больше 0")
        return num2
    except ValueError:
        print("Ввели не число, попробуй еще")
        return input_num2()
num1=input_num1()
num2=input_num2()

rand=int(datetime.datetime.now().strftime('%f'))/1000000
rand=int(rand*(num2-num1)+num1)

print("Случайное число", rand)
