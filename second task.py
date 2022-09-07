#Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
#Не используйте функцию math.factorial.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)



def input_num():
    try:
        num=int(input("Введи число: "))
        if num < 0:
            print ("Нельзя вычислить факториал отрицательного числа")
        elif num == 0:
            print ("Факториал 0 = 1")
        return num
    except ValueError:
        print("Ввели не число, попробуй еще")
        return input_num()

num=input_num()
count=1
print(count)

while(num>1):
    count=count*num
    num-=1
    print(count)

    
