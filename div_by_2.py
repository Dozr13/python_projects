def d(int):
    a = input("Type a number to divide by 2: ")
    a = int(a)
    b = 2
    if a % 2 == 0:
        print(a // b)
    else:
        print("Your number must be an even number.")

try:
    d(int)
except ValueError:
    print("Enter a number into the field.")
        

