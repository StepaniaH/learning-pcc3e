age = int(input('Enter your age: '))

if age < 2:
    print('You are a baby!')
elif 2 <= age < 4:
    print('You are a toddler!')
elif 4 <= age < 13:
    print('You are a kid!')
elif 13 <= age < 20:
    print('You are a teenager!')
elif 20 <= age < 65:
    print('You are an adult!')
else:
    print('You are an elder!')


# By the way, copilot is really useful for this kind of practices, which I must repeat many times.
