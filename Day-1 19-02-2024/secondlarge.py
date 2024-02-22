a = int(input("Enter the value a: "))
b = int(input("Enter the value b: "))
c = int(input("Enter the value c: "))
if (a>b and a>c):
    a = 0
elif b>c:
     b = 0
else:
    c = 0
if (a>b and a>c):
    print("The second largest value is : ".a)
elif b>c:
     print("The second largest value is : ",b)
else:
   print("The second largest value is : ",c)