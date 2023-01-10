# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


def mult_lst(lst):
    l = len(lst)
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)


lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)
