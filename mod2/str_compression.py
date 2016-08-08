def pairwise(itrbl):
    """
    Takes in an iterable. Returns its items pairwise with overlap.
    For example, it returns 1st and 2nd elements, then 2nd and 3rd and so on.
    Uses `\0` symbol to indicate the end of the sequence.
    """
    for ind in range(len(itrbl)):
        try:
            yield (itrbl[ind], itrbl[ind + 1])

        except IndexError:
            yield (itrbl[ind], '\0')


cmprsed = []
count = 1

for cur, nxt in pairwise(input()):
    if cur == nxt:
        count += 1
    else:
        cmprsed.append(cur + str(count))
        count = 1

print("".join(cmprsed))
