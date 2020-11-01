print("Hello")
print("Welcome")
print("To Code!")




x = 13
if x >= 10:
    print("13 is greater than 10")
else:
    print("10 is not greater than 13!")



y = 23
if y <= 10:
    print("Your number is less than 10")
elif y > 10 and y < 25:
    print("Your number is greater than 10 but less than 25")
elif y > 25:
    print("Your number is greater than 25")
else:
    print("That is not a number")



z = y % x
print(z)


a = y // x
print(a)




age = 28
i = age
if i <= 15:
    print("You've got your whole life ahead of you")
elif i <= 25:
    print("Keep on learning!")
elif i <= 35:
    print("Life decision changes anyone?")
elif i <= 55:
    print("Senior citizen discount can't come quick enough")
elif i <= 65:
    print("Ah grandkids are awesome!")
elif i <= 80:
    print("Dang kids need to stay off my lawn!")
elif i <= 95:
    print("Kickin buckets")
else:
    print("You had a good run!")
