input = []
with open('Day4/Input-test.txt', "r") as infile:
    input = list(map(lambda a: a.strip(), infile.readlines()))

input = map(lambda b: b.split(), input)

# Formats input and parses down to needed info
for item in input:
    item[0] = item[0] + " " + item[1]
    del item[1]
    if len(item) == 3:
        del item[2]
    else:
        item[1] = item[2][1:]
        for x in range(3):
            del item[2]

input.sort(key=lambda c: c[0])

data = []

for item in input:
    print(item)
