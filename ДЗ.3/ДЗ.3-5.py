a=-1
b=-1
while not (a>0):
    a = int(input("Введіть число a>0 "))
while not (b>0 and b>a):
    b = int(input("Введіть число b>0, b>a "))

for i in range(a,b+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print("")