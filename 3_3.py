'''

Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
Пример:
[1.1, 1.2, 3.1, 5, 10.01] => 0.19

'''

def get_diff_between_max_min(lst):
    l=len(lst)
    
    new_lst = [lst[i]-int(lst[i]) for i in range(l)]
    while 0.0 in new_lst:
        new_lst.remove(0.0)
    #print(new_lst)   
    #print(f'Минимальная дробная часть: {round(min(new_lst),3)}')
    #print(f'Максимальная дробная часть: {round(max(new_lst),3)}')
    print(f'Разница между максимальным и минимальным значением дробной части: {round(max(new_lst),3)-round(min(new_lst),3)}')

print('Введите вещественные числа через запятую:') 
lst = list(map(float, input().split(",")))
get_diff_between_max_min(lst)

