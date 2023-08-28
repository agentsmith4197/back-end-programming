myString = "python is a cool program, python is love, python is fun"
python_count = myString.split().count("python")
print(python_count)
capitalized = myString.title()
print(f'{capitalized} \n ')

target = "python"
targeted = target.capitalize()
capital = myString.replace(target, targeted)
print(capital)
