names = ['lil a', 'lil b', 'lil c', 'lil d']

regret = names.pop(1)

print(f"It is a pity that {regret.title()} can not make the appointment.")

names.insert(1, 'big b')

print(f"Hey, {names[0].title()}, come to have dinner with me!")
print(f"Hey, {names[1].title()}, come to have dinner with me!")
print(f"Hey, {names[2].title()}, come to have dinner with me!")

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