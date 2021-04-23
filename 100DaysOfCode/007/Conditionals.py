#Ternary operator
n = 5
print("Greter than 2") if n>2 else print("Smaller than 2")

#if elif and else
number = 5
if number > 2:
    print("Number is bigger than 2.")
elif number < 2: # Optional clause (you can have multiple elifs)
    print("Number is smaller than 2.")
else: # Optional clause (you can only have one else)
    print("Number is 2.")

#Lazy evaluation
#   first Left side will be evaluated

def print_me():
    print('Inside print me')

if 0 and print_me():
    print(True)
else:
    print(False)

if print_me() and 0:
    print(True)
else:
    print(False)

