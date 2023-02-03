'''

Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

a) Добавьте игру против бота

b) Подумайте как наделить бота 'интеллектом'

'''

from random import randint
number=int(input('Задайте количество  разыгрываемых конфет:  '))

def nameplayer(turnplayer):
 if turnplayer==True :
     return 'Карина'
 else:
     return 'Арни'
 

print ('Начинаем игру!')
turnplayer=bool(randint(0,1))
print (f'В ходе жеребьевки выяснилось, что начинает игру {nameplayer(turnplayer)}')

while number>0 :
    print(f'{nameplayer(turnplayer)}, тащи конфеты!')
    count=int(input())
    while count>28 :
       print ('Можно не больше 28 конфет взять! Ход переходит к другому') 
       turnplayer=not turnplayer
       print(f'{nameplayer(turnplayer)}, тащи конфеты!')
       count=int(input())
    number-=count
    turnplayer=not turnplayer
    
turnplayer=not turnplayer    
print (f'Все конфеты получает {nameplayer(turnplayer)}')
