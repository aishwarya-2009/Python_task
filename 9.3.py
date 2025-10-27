try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found!")
finally:
    print("Execution completed (finally block runs always).")
