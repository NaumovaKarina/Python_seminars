#3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

def GetCoordinatePlaneQuarter(x,y):
 if x==0 and y==0:
    print('эти координаты нельзя указывать по условию задачи')
    exit(0)
 elif x==0 or y==0:
      if x==0: 
        print('точка лежит на оси ординат') 
        exit(0)
      else: 
        print('точка лежит на оси обцисс') 
        exit(0)
 if x>0 and y>0:
    quarter = 1
 elif x<0 and y>0:
    quarter = 2
 elif x<0 and y<0:
    quarter = 3
 elif x>0 and y<0:
     quarter = 4
 print(f"Точка находится в {quarter}-й четверти плоскости")
 
 
x=float(input("Введите координату x:\n"))
y=float(input("Введите координату y:\n"))
GetCoordinatePlaneQuarter(x,y)