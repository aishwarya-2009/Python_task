try:
    num = int(input("Enter a number: "))
    print("Square:", num ** 2)
except ValueError:
    print("Error: Invalid input, please enter a number!")
except Exception as e:
    print("Unexpected error:", e)
