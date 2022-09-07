#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
#Пример:
#67.82 -> 23
#0.56 -> 11



def example():
    try:
        num=float(input("Введи число: "))
        return num
    except ValueError:
        print("Ввели не число, попробуй еще")
        return example()
        
   
num=example()      

if num<0:
    num*=-1
str_num=str(num)
str_num=str_num.replace(".", "")
list_str=list(str_num)
print(list_str)
list_num=map(int, list_str)
summa=sum(list_num)
print (summa)




