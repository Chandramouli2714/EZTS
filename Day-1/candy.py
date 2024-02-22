test_input = int(input())
for i in range(test_input):
    student, candies = map(int,input().split())
    if student > candies:
        remaining_students = student - candies
        if remaining_students % 4 == 0:
            print(remaining_students//4)
        else:
            print((remaining_students//4)+1)
    else:
        print(0)