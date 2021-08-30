'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
members = []
for _ in range(int(input())):
    members.append(int(input()))

edges = {}
for _ in range(int(input())):
    cordinates = input().split()
    if int(cordinates[1]) in edges:
        array = edges[int(cordinates[1])]
        array.append(int(cordinates[0]))
        edges[int(cordinates[1])] = array
    else:
        array = [int(cordinates[0])]
        edges[int(cordinates[1])] = array


follower = int(input())
following = int(input())

removable_followers = []

print(edges)

if following in edges:
    removable_followers.append(edges[following])
    i = 0
    while i< len(removable_followers):
        if removable_followers[i] in edges:
            if follower in edges[removable_followers[i]]:
                i += 1
                continue




#check(follower, following)
#for i in removable_followers:
#    print(i, end=" ")

