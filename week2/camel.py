word = input("camelCase:  ").strip()

snake_case = ""

for i in word:
    if i.isupper():
        snake_case += '_' + i.lower()
    else:
        snake_case += i

print(f"snake_case: {snake_case}")