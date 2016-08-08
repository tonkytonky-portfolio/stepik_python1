def step(i, j, drct):
    # Coordinates to move right, down, left or up
    di, dj = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}[drct]

    # If the next cell, intended to move in is empty -- move there
    # and return new coordinates and old direction
    if mtrix[(i + di) % mtrix_len][(j + dj) % mtrix_len] == 0:
        i, j = (i + di, j + dj)
        return i, j, drct

    # If the next cell, intended to move in is not empty -- change direction
    # and make step according to it
    else:
        drct = (drct + 1) % 4
        return step(i, j, drct)


n = int(input())
mtrix = [[0 for mj in range(n)] for mi in range(n)]
mtrix_len = len(mtrix)

# Initial cell -- start moving from out of the matrix.
# Initial direction -- right. Where 0 -- right, 1 -- down, 2 -- left, 3 -- up.
i, j, drct = 0, -1, 0

# In range of numbers to insert in the matrix:
#   1. Make step to an empty matrix cell
#   2. Put the current number there
for n_ins in range(1, n ** 2 + 1):
    i, j, drct = step(i, j, drct)
    mtrix[i][j] = n_ins

for row in mtrix:
    print("\t".join([str(i) for i in row]))
