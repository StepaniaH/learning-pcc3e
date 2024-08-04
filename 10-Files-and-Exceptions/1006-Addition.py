print("Give me two numbers, and I'll add them up for you.")


try:
    a = int(input("First number: "))
except ValueError:
    print("First number must be an integer.")
    exit()

try:
    b = int(input("Second number: "))
except ValueError:
    print("Second number must be an integer.")
    exit()

print(a + b)
