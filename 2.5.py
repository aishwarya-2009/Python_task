N = int(input("Enter N: "))

first, second=0,1

print("Fibonacci series:", end=" ")
for _ in range(N):
    print(first, end=" ")
    first, second = second, first+second
