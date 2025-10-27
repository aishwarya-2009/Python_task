def square_generator(n):
    for i in range(1, n+1):
        yield i * i   # yield returns values one by one

# Using the generator
n = int(input("Enter a number: "))
print(f"Squares from 1 to {n} are:")
for val in square_generator(n):
    print(val)
