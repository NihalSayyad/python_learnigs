def printMat(mat):
    for i in mat:
        for j in i:
            print(j, end="")
        print("\n", end="")

def floodFill(mat, i, j, ch, color):
    if i<0 or j<0 or i>=R or j>=C or mat[i][j] !=ch:
        return

    mat[i][j] = color

    floodFill(mat, i+1, j, ch, color)
    floodFill(mat, i, j+1, ch, color)
    floodFill(mat, i-1, j, ch, color)
    floodFill(mat, i, j-1, ch, color)

if __name__ == '__main__':
    mat = []
    with open('apple.txt', 'r') as f:
        line = f.readline().split()
        R, C = int(line[0]), int(line[1])
        for i in range(R):
            mat.append(list(f.readline()))

    printMat(mat)

    floodFill(mat, 8, 13, '.', 'R')
    printMat(mat)