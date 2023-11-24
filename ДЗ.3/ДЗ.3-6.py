a=-1
b=-1
while not (a>0):
    a = int(input("Введіть число a>0 "))
while not (b>0 and b>a):
    b = int(input("Введіть число b>0, b>a "))

d=1
for i in range(a,b+1):
    if (i%2==0) and (i%3==0):
        d=d*i
        if (d==i):
            print(i,end="")
        else:
            print(" *",i,end="")
if d==1:
    print("таких чисел немає")
else:
    print("=",d)