'''
Реализуйте алгоритм перемешивания списка.
НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
максимум использование библиотеки Random для и получения случайного int.
'''
from random import randint

my_dict = {}
length = int(input("Сколько элементов в списке? "))
print("Ввведите через ENTER элементы списка")
for element in range(0,length):
  my_key=randint(1,10000)
  my_dict[my_key] = input()
  #my_dict[my_key] = input(f'введите значение для ключа {my_key}: ')
#print(my_dict)
my_dict=sorted(my_dict.items())
my_dict=dict(my_dict)
print("Перемешанный список: ")
for item in my_dict.values():
    print(item, end=' ')    
    
