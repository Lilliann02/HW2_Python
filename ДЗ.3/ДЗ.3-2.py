X=0
while not ((X//10)!=0 and (X//100)==0):
    X = int(input("Введіть двозначне число "))
p10=X//10
p1=X%10
if p1>p10:
    print(p1,">",p10)
elif p10>p1:
    print(p10,">",p1)
else:
    print(p1,"=",p10)