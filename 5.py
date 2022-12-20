#5.Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
def GetDistance(a,b):
 dist = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
 return dist   


a=[]  
b=[]
a.append(float(input("Введите координату X для точки А:\n")))
a.append(float(input("Введите координату Y для точки A:\n")))
b.append(float(input("Введите координату X для точки B:\n")))
b.append(float(input("Введите координату Y для точки B:\n")))
distance=round(GetDistance(a,b),2)
    
print(f"Расстояние между точками = {distance}")     