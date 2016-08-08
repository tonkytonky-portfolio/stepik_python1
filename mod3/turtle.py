steps = {"north": 0, "south": 0, "west": 0, "east": 0}

for _ in range(int(input())):
    step = input().split()
    steps[step[0]] += int(step[1])

print("{0} {1}".format(
    steps["east"] - steps["west"],
    steps["north"] - steps["south"]
))
