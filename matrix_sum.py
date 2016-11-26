mtrix = []

while True:
    inpt = input()
    if inpt == "end":
        break
    mtrix.append([int(i) for i in inpt.split()])

height = len(mtrix)
length = len(mtrix[0])
mtrix_new = [[0 for j in range(length)] for i in range(height)]

for i in range(height):
    for j in range(length):
        mtrix_new[i][j] = sum((
            mtrix[(i + 1) % height][j],
            mtrix[(i - 1) % height][j],
            mtrix[i][(j + 1) % length],
            mtrix[i][(j - 1) % length]
        ))

for row in mtrix_new:
    print("\t".join([str(i) for i in row]))
