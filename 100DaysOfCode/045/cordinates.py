members = []
for _ in range(int(input())):
    members.append(int(input()))

edges = {}
for _ in range(int(input())):
    cordinates = input().split()
    print(cordinates)
    if int(cordinates[0]) in edges:
        print(edges[int(cordinates[0])])
        array = edges[int(cordinates[0])]
        array.append(int(cordinates[1]))
        edges[int(cordinates[0])] = array
    else:
        array = [int(cordinates[1])]
        edges[int(cordinates[0])] = array


follower = int(input())
following = int(input())

print(follower)
print(following)
print(edges)

while True:
    print(follower)
    if not edges[follower]:
        print(0)
        break
    if edges[follower][0] == following:
        print(1)
        break
    else:
        follower = edges[follower].pop(0)