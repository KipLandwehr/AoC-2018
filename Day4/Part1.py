input = []
with open('Day4/Input.txt', "r") as infile:
    input = list(map(lambda a: a.strip(), infile.readlines()))

input = map(lambda b: b.split(), input)

# Formats input and parses down to needed info
for item in input:
    # Fix date and time formatting
    item[0] = int(''.join(item[0][1:].split('-')))
    item[1] = int(''.join(item[1][:-1].split(':')))
    # "wakeup / fall asleep" lines
    if len(item) == 4:
        del item[3]
    # "Guard starts shift" lines
    else:
        item[2] = int(item[3][1:])
        for x in range(3):
            del item[3]

# Sort input by timestamp
input.sort(key=lambda c: (c[0],c[1]))

for item in input:
    print(item)

data = []
prevTime = 0

# Interprets input and stores in a list
for item in input:
    date = item[0]
    time = item[1]

    if item[2] == "wakes":
        for x in range(prevTime, time):
            data[-1][2][x] = '#'
    elif item[2] == "falls":
        prevTime = time
    else:
        currID = int(item[2])
        if item[1] > 59:
            date += 1
        data.append([date, currID, ['.' for x in range(60)]])

# Array for info about individual guards        
guards = []

# Returns True if a guard's ID (i) is already in the guards list
def containsID(l, i):
    retval = False
    for x in range(len(l)):
        if l[x][0] == i:
            retval = True
            break
    return retval

# Returns the index of guards where the ID and other data is located
def getIndexOfID(l, i):
    retval = 0
    for x in range(len(l)):
        if l[x][0] == i:
            retval = x
            break
    return retval

# Interprets the data for each day to determine how many total minutes a guard
# slept, and how many times he was asleep during each minute of the hour.
for elem in data:
    ID = elem[1]
    index = 0

    if containsID(guards, ID):
        index = getIndexOfID(guards, ID)
    else:
        guards.append([ID, 0, [0 for x in range(60)]])
        index = -1

    for x in range(len(elem[2])):
        if elem[2][x] == '#':
            guards[index][1] += 1
            guards[index][2][x] += 1


guardID = 0
maxMinutes = 0
minute = 0

# Determines which guard slept the most, and which minute that guard sleeps on
# most frequently.
for elem in guards:
    if elem[1] > maxMinutes:
        maxMinutes = elem[1]
        guardID = elem[0]
        minute = elem[2].index(max(elem[2]))

# Calculates and prints the AoC answer.
answer = guardID * minute
print(answer)
