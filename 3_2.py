# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


def mult_lst(lst):
    l = len(lst)
    new_lst = [lst[i]*lst[l-i-1] for i in range(l//2)]
    if l%2==1:
        new_lst.append(lst[l//2]*lst[l//2])
    print(new_lst)


lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)
