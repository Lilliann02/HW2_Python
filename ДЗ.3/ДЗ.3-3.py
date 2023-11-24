a = int(input("Введіть число a "))
b = int(input("Введіть число b "))

s=0
for i in range(100,500+1):
    s=s+i
print("сума всіх цілих чисел від 100 до 500 = ",s)

s=0
for i in range(a,500+1):
    s=s+i
print("сума всіх цілих чисел від a до 500 = ",s)

s=0
for i in range(-10,b+1):
    s=s+i
print("сума всіх цілих чисел від -10 до b = ",s)

s=0
for i in range(a,b+1):
    s=s+i
print("сума всіх цілих чисел від a до b = ",s)