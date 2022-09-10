#Напишите такую программу, которая найдет палиндром введенного пользователем числа.

def input_num():
    try:
        num=int(input("Введи число: "))
        return num
    except ValueError:
        print("Ввели не число, попробуй еще")
        return input_num()

num=input_num()

while True:
    str_num=str(num)
    num_list=list(str_num) 
    num_list.reverse()
    inverse="".join(num_list)
    inverse_num=int(inverse)
    sum=(num+inverse_num)
    num2=sum 
    inverse=0
    count=num2

    while count != 0:
        palind=count%10
        inverse=inverse*10+palind
        count=int(count/10)

    if num2==inverse:
        print("палиндром")
        print(num2)
        print("конец")
        break
    else:
        print("не палиндром")
        num = num2
        print("круг")
    



        # Здесь просто ответ на введенное число, является ли оно само по себе палиндромом

# def input_num():
#     try:
#         num=int(input("Введи число: "))
#         return num
#     except ValueError:
#         print("Ввели не число, попробуй еще")
#         return input_num()

# num=input_num() 
# inverse=0
# count=num

# while count != 0:
#     palind=count%10
#     inverse=inverse*10+palind
#     count=int(count/10)

# if num==inverse:
#     print("палиндром") результат
# else:
#     print("не палиндром")

