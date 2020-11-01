def f():
    '''
    Created a function that finds the square root of
    a number inputed by the User and prints it.
    '''
    a = input("Type a number to find the square root of: ")
    a = int(a)
    sq = a * a
    print(sq)

try:
    f()
except ValueError:
    print("I can't find the square root of that, enter a number!")



def f(str):
    '''
    Created a function that accepts a str for its parameter
    and also prints said str.
    '''
    str = "Howdy World!"
    print(str)

f(str)




def g(x, y=2, z=3):
    '''
    Created a function with 3 parameters, 2 optional,
    1 requred and doing a simple math calculation to
    find the value of the required param.
    '''
    return z - y

result = g(2)
print(result)





def h(int):
    '''
    Taking int of users choice and divides it by 2
    creating a global result and passing it into the
    following func.
    Also checking for errors and providing a print()
    statement explaining what the user must do.
    '''
    a = input("Type a number to divide by 2: ")
    a = int(a)
    b = 2
    global result
    result = a // b
    if a % 2 == 0:
        print(result)
        return result
    else:
        print("Your number must be an even number.")

try:
    h(int)
except ValueError:
    print("Enter a number into the field.")
        






def i(int):
    '''
    Pulled result from last function
    and multiplying it by 4.
    '''
    a = result
    b = 4
    answer = a * b
    print(answer)

i(int)






def j():
    '''
    converting the following str to a float class
    '''
    float("23.13")
    print(float)




try:
    j()
except ValueError:
    print("Oops, make sure you have a number in the box writer!")














