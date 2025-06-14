name = input("What's your name? \n")
color = input("What's your favorite color? \n")
with open('example.txt', 'w') as file:
    file.write(f"{name} created this file. \n")
    file.write(f"{color} is the favorite color.")