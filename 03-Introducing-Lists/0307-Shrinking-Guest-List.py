names = ['lil a', 'lil b', 'lil c', 'lil d']

regret = names.pop(1)

names.insert(1, 'big b')

print("Congratulations! I found a bigger dinner table!")

names.insert(0, 'big a')
names.insert(3, 'big c')
names[-1] = 'big d'
names.append('lil d')

print(f"Hey, {names[0].title()}, come to have dinner with me!")
print(f"Hey, {names[1].title()}, come to have dinner with me!")
print(f"Hey, {names[2].title()}, come to have dinner with me!")
print(f"Hey, {names[3].title()}, come to have dinner with me!")
print(f"Hey, {names[4].title()}, come to have dinner with me!")
print(f"Hey, {names[5].title()}, come to have dinner with me!")
print(f"Hey, {names[6].title()}, come to have dinner with me!")

print("I can only invite two guests due to the suck AWS!")

print(f"Sorry, {names.pop().title()}!")
print(f"Sorry, {names.pop().title()}!")
print(f"Sorry, {names.pop().title()}!")
print(f"Sorry, {names.pop().title()}!")
print(f"Sorry, {names.pop().title()}!")

print(f"{names[0].title()}, you are still in my list.")
print(f"{names[1].title()}, you are still in my list.")

del names[0:]
print(names)
