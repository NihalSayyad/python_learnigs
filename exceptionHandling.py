
a = 5
b = 0

try:
    #Will try to perform below activity
    #If it has any exceptions or errors, will execute except
    print("resource open")
    print(a/b)

except ZeroDivisionError as a:
    print("Hey, you cannot divide a num by zero", a)

except ValueError as a:
    print("Hey, value is not an integer")

except Exception as a:
    print("Something wen wrong")

finally:
    print("resource close")

print("Bye")