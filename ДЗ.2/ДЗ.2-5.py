year = int(input("Введіть рік:  "))

if (year>0):
    if (year%4==0) and not(year%100==0 and year%400!=0):
        print(366)
    else:
        print(365)
else:
    print("такого року не існує")