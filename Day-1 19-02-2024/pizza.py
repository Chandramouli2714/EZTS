test_input = int(input())
for i in range(test_input):
    count,slices = map(int,input().split())
    total_slices  = count*slices
    total_pizzas = 0
    while total_slices > 4:
        total_pizzas = total_pizzas + 1
        total_slices = total_slices - 4
    if total_pizzas == 0:
        print(total_pizzas)
    else:
        print(total_pizzas+1)