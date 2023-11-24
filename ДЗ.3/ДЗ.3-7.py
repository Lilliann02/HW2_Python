a=-1
while not (a>0):
    a = int(input("Введіть ціну цукерок a (>0) "))

for i in range(1,10+1):
    print(i,"кг цукерок коштує",i*a,"грн")
