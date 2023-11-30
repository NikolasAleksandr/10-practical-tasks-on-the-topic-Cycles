from math import *
from re import X

#for x in range(10):
#    R=float(input("{0}.R: ".format(x+1)))
#    if R>0:
#       S=pi*R**2
#    else:
#        S="R peab > kui 0 olema"
#    print("S={0}".format(S))

x=0
while x<1:
    R=float(input("{0}.R: ".format(x+1)))
    if R>0:
        S=pi*R**2
        x+=1
    else:
        S="R peab > kui 0 olema"
    print("S={0}".format(S))



#1.Вводят 15 чисел. Определить, сколько среди них целых.
#t=0
#for x in range(15):
#   A=float(input("Sisesta A: "))
#    if A.is_integer():# 5.0; 6=True; 2.45=False
#        t+=1
#print(t)

#2.Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.
summa=0
A=int(input("Sisesta A: "))
for x in range(1,A+1,1):
    summa+=x
print("Summa: {0}".format(summa))


#3.Вводят 8 чисел. Найти их произведение (только положительных).
t=1
for x in range (8):
    B=float(input("{0}. samm\nSisesta B: ".format(x+1)))
    if B>0:
        t*=B
print(t)

#4.Составьте программу, выводящую на экран квадраты чисел от 10 до 20.
for x in range(10,21):
    print(x **2)


#5.Составьте программу, которая вычисляет сумму только отрицательных из N чисел. Значение N вводится с клавиатуры.

N=int(input("Введите количество чисел N: "))
sum_negative = 0

for x in range(N):
    num=int(input(f"Введите число {x+1}: "))
    if num < 0:
        sum_negative += num
print(f"Сумма отрицательных чисел: {sum_negative}")

#6.С клавиатуры вводятся N чисел.Составьте программу, которая определяет количество отрицательных,
# количество положительных и количество нулей среди введенных чисел.   Значение N вводится с клавиатуры.
N=int(input("Введите количество чисел N: "))

count_positive = 0
count_negative = 0
count_zeros = 0

for x in range (N):
    num=int(input(f"Введите число {x+1}: "))
    if num > 0:
        count_positive += num
    elif num < 0:
        count_negative += num
    else:
         count_zeros += num
print(f"Сумма положительных чисел: {count_positive}")
print(f"Сумма отрицательных чисел: {count_negative}")
print(f"Количество нулей: {count_zeros}")


#7.Вывести на экран числа, кратные К из промежутка [А,В].

A=int(input("Введите начало промежутка A :"))
B=int(input("Введите конец промежутка B :"))
K=int(input("Введите значение K :"))

print(f"Числа, кратные {K}, в промежутке от {A} до {B}: ")
for num in range(A,B+1):
    if num % K==0:
       print(num)



#15 Написать программу, выводящую в столбик десять строк, в каждой печатая цифры от 0 до 9, то есть в таком виде:
    #0 1 2 3 4 5 6 7 8 9

for y in range (10):
    for x in range (10):
        print (x,end= " ")
    print()


#29
for i in range(10):
    for x in range(9):
        if x==0 or i==x:
           print("x",end=" ")
        else:
            print("0",end=" ")
    print()




#22.Найти сумму чисел от 100 до 200, кратных 17.

num_multiplies_17=0
for num in range (100,201):
    if num % 17==0:
        num_multiplies_17 += num
        print(f"Сумма чисел от 100 до 200, кратных 17: {num_multiplies_17}")



#18.Даны натуральные числа от 20 до 50. Напечатать те из них, которые делятся на 3, но не делятся на 5.
print("Натуральные числа от 20 до 50, которые делятся на 3, но не делятся на 5.")
for num in range (20,51):
    if num % 3==0 and num % 5!=0:
       print(num)


#19
print("Натуральные числа от 35 до 87,  которые при делении на 7 дают остаток 1, 2 или 5.")
for num in range (35,88):
    if num % 7 in [1,2,5]:
        print(num)


#20
print("Натуральные числа от 1 до 50, которые делятся на 5 или на 7.")
for num in range (1,51):
    if num % 5==0 and num % 7==0:
       print(num)


#10
print("Введите 10 пар чисел: ")

for i in range (10):
    num1=float(input("Введите первое число из пары: "))
    num2=float(input("Введите второе число из пары: "))

    if num1 > num2:
        print(f"Большее число в паре {i+1}: {num1}")
    elif num1 < num2:
        print(f"Большее число в паре {i+1}: {num2}")
    else:
        print(f"Числа в паре равны {i+1}: {num1}")





