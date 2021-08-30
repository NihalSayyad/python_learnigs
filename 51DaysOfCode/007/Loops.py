#Break and Continue in Loops
#Break -- breaks the loop

for i in range(10):
    if i == 4:
        print('Breaking at 4')
        break

#Continue -- this will skip the current execution of further lines
i = 0 
while i < 10:
    print(i)
    i += 1
    if i == 4:
        print('Skipping 4')
        continue
    print('next condition')
    
