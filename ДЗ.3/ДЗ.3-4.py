n=0
while not (n<=9 and n>=1):
    n = int(input("Введіть число n (1 <=n<= 9) "))

i=1
while i<=n:
    print(n,"*",i,"=",n*i)
    i=i+1
print("")

for i in range(1,n+1):
    print(n,"*",i,"=",n*i)