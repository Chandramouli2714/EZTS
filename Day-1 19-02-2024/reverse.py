num = int(input("enter the number: "))
if num>0:
    reversed_num = 0    
    while num!= 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    print(reversed_num)
elif num < 0:
    reversed_num = 0 
    num = num*-1  
    while num!= 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    print(reversed_num*-1)
else:
    print(num) 