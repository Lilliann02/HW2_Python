A = int(input("Введіть число A:  "))
B = int(input("Введіть число B:  "))
C = int(input("Введіть число C:  "))

if (A<B and A>C) or (A>B and A<C):
    print(A)
elif (B<A and B>C) or (B>A and B<C):
    print(B)
elif (C<A and C>B) or (C>A and C<B):
    print(C)
else:
    print("такого числа немає")