# We always have 11 classes
clses = [
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0},
    {"height": 0, "students": 0}
]

with open("class_dataset.txt", "r") as cls_file:
    for line in cls_file:
        line = line.split("\t")

        # Count a student anf his height
        clses[int(line[0]) - 1]["students"] += 1
        clses[int(line[0]) - 1]["height"] += int(line[2])

# Print info about each class, getting average height
for ind, cls in enumerate(clses):
    print("{} {:.2f}".format(
        ind + 1, float(cls["height"]) / cls["students"] if cls["students"] else "-"
    ))
