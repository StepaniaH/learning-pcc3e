names = ['lil a', 'lil b', 'lil c', 'lil d']

regret = names.pop(1)

print(f"It is a pity that {regret.title()} can not make the appointment.")

new_name = names.insert(1, 'big b')

print(f"Hey, {names[0].title()}, come to have dinner with me!")
print(f"Hey, {names[1].title()}, come to have dinner with me!")
print(f"Hey, {names[2].title()}, come to have dinner with me!")