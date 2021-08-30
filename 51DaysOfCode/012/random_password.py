import random
import string

chars = []
nums = []
special_char = []
chars[:] = string.ascii_letters
nums = [n for n in range(0,10)]
special_char [:] = string.punctuation

all = chars + nums + special_char

#print(all)
password = ""
#print(random.shuffle(all))
#print(all)
for i in range(10):
    random.shuffle(all)
    password = password + str(all[i])

print(password)
