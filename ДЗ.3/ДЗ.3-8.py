N=-1
while not (N>0):
    N = int(input("Введіть ціле число N (>0) "))
flag=False
while N%10>=0 and N!=0:
    if (N%10==2):
        flag=True
        break
    N=N//10
print(flag)