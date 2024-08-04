from random import choices


list = ["1", "2", "3", "4", "5", "6", "7",
        "8", "9", "10", "a", "b", "c", "d", "e"]

my_list = ["1", "2", "3", "a"]
j = 0
i = 0
while True:
    j += 1
    while True:
        i += 1
        lottery = choices(list, k=4)
        if lottery == my_list:
            # print(f"You won in {i} tries!")
            break
    if i < 10:
        break
    else:
        i = 0

print(f"Through {j} tries, I matched my list in {i} tries, finally.")

# This is a ultra luck game!
# If you trap in an infinite loop, you're probably not a lucky person, and you can type `control + c` to escape.
