'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
45 -> 101101
3 -> 11
2 -> 10

'''


def convert_to_digital(decimal):
 digital=''
 znak=''
 if decimal<0 :
    znak+='-'
    decimal=decimal*(-1)
 while (decimal>1):
    #print(decimal) 
    digital+=str(decimal%2)
    decimal=decimal//2
    #print(digital) 
 digital+='1'+znak   
 print(f'Его двоичная версия: {digital[::-1]}')
 return
    
number=int(input("Введите число: "))
convert_to_digital(number)
