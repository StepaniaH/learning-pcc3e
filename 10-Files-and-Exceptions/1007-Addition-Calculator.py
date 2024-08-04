print("Give me two numbers, and I'll add them up for you.")

while True:
    try:
        a = int(input("First number: "))
        break
    except ValueError:
        print("First number must be an integer.")

while True:
    try:
        b = int(input("Second number: "))
        break
    except ValueError:
        print("Second number must be an integer.")

print(a + b)
