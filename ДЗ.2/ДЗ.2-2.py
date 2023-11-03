A = int(input("Введіть число A:  "))
B = int(input("Введіть число B:  "))
C = int(input("Введіть число C:  "))
s=0
if (A+abs(A)==0):
    s+=1
if (B+abs(B)==0):
    s+=1
if (C+abs(C)==0):
    s+=1
if (s==2):
    print("«Рівно одне з чисел A, B, C позитивне» - TRUE")
else:
    print("«Рівно одне з чисел A, B, C позитивне» - FALSE")