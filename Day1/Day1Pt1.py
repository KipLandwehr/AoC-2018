import fileinput

total = 0

for line in fileinput.input():
    total += int(line)

print(total)

fileinput.close()