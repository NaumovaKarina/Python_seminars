#4.Напишите программу, которая по заданному номеру четверти, 
#показывает диапазон возможных координат точек в этой четверти (x и y).

def GetSetOfValues(q):
 if q==1:
    print('x ∈ (0;+∞), y ∈ (0;+∞)')
 elif q==2:
    print('x ∈ (-∞;0), y ∈ (0;+∞)')
 elif q==3:
    print('x ∈ (-∞;0), y ∈ (-∞;0)') 
 else: 
    print('x ∈ (0;+∞), y ∈ (-∞;0)')
  
quarter=int(input("Введите номер четверти:\n"))
if quarter in range(1,5): 
    GetSetOfValues(quarter)
else: print("номер четверти должен быть диапазоне от 1 до 4") 