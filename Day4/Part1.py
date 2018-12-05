input = []
with open('Day4/Input.txt', "r") as infile:
    input = list(map(lambda a: a.strip(), infile.readlines()))

input = map(lambda b: b.split(), input)

# Formats input and parses down to needed info
for item in input:
    # Fix date-time formatting
    item[0] = item[0] + " " + item[1]
    del item[1]
    # "wakeup / fall asleep" lines
    if len(item) == 3:
        del item[2]
    # "Guard starts shift" lines
    else:
        item[1] = int(item[2][1:])
        for x in range(3):
            del item[2]

# Sort input by timestamp
input.sort(key=lambda c: c[0])

data = []
IDs = []
currentID = -1

for item in input:
    if item[1] == "wakes":
        #do something
    elif item[1] == "falls":
        #do something else
    else:
        currentID = int(item[1])
        if currentID not in IDs:
            IDs.append(currentID)
            data.append([0, [0 for x in range(60)]])

    print(data)
