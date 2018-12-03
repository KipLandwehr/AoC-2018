# Sample input:
# #1 @ 35,93: 11x13

# Sample of 'data' array
# [ [ [35, 93], [11, 13], 1 ] ]

data = []
maxWidth = 0
maxHeight = 0

with open('Day3/Input.txt', "r") as file1:
    for line in file1:
        words = line.split()
        words[0] = int(words[0][1:])
        words[2] = words[2][:-1]
        words[2] = words[2].split(',')
        words[3] = words[3].split('x')
        data.append([words[2], words[3], words[0]])
        width = int(words[2][0]) + int(words[3][0])
        height = int(words[2][1]) + int(words[3][1])
        if width > maxWidth:
            maxWidth = width
        if height > maxHeight:
            maxHeight = height

fabric = [[0 for x in range(maxHeight)] for y in range(maxWidth)]
answer = [x+1 for x in range(len(data))]

for elem in data:
    wStart = int(elem[0][0])
    wEnd = wStart + int(elem[1][0])
    hStart = int(elem[0][1])
    hEnd = hStart + int(elem[1][1])
    for w in range(wStart, wEnd):
        for h in range(hStart, hEnd):
            ID = elem[2]
            if fabric[w][h] == 0:
                fabric[w][h] = ID
            elif fabric[w][h] == -1:
                if ID in answer:
                    answer.remove(ID)
            else:
                if ID in answer:
                    answer.remove(ID)
                if fabric[w][h] in answer:
                    answer.remove(fabric[w][h])
                fabric[w][h] = -1
            
print(answer)
