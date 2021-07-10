def printMat(mat):
    for i in mat:
        for j in i:
            print(j, end="")
        print("\n", end="")



if __name__ == '__main__':
    mat = []
    with open('apple.txt', 'r') as f:
        line = f.readline().split()
        R, C = int(line[0]), int(line[1])
        for i in range(R):
            mat.append(list(f.readline()))

    printMat(mat)