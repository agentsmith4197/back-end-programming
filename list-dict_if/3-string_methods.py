myString = "python is a cool program, python is love, python is fun"
python_count = myString.split().count("python")
print(f'the word python appears {python_count} times \n ')
capitalized = myString.title()
print(f'{capitalized} \n ')

target = "python"
targeted = target.capitalize()
capital = myString.replace(target, targeted, 1)
print(capital)