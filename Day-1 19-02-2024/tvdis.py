test_case = int(input())
for i in range(test_case):
    a,b,c,d = map(int,input().split())
    tv_A  = (a-c)
    tv_B = (b-d)
if tv_A < tv_B:
    print("First")
elif tv_B < tv_A:
    print("Second")
else:
    print("Any")        
    
    