import time
# Decorator function
def timer_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution Time: {end - start:.5f} seconds")
    return wrapper

# Function to be decorated
@timer_decorator
def display_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(0.5)  # just to simulate delay
# Calling the decorated function
display_numbers()
