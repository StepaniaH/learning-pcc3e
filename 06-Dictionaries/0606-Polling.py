favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

researched_names = ['jen', 'phil', 'peter', 'tom']

print("\n")
for researched_name in researched_names:
    if researched_name in favorite_languages:
        print(f"Thanks for your participation, {researched_name.title()}!")
    else:
        print(f"{researched_name.title()}, welome to the polls!")
