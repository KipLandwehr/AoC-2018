# Sample input:
# #1 @ 35,93: 11x13

# Sample of 'data' array
# [ [ [35, 93], [11, 13] ] ]

data = []
maxWidth = 0
maxHeight = 0

with open('Day3/Input.txt', "r") as file1:
    for line in file1:
        words = line.split()
        words[2] = words[2][:-1]
        words[2] = words[2].split(',')
        words[3] = words[3].split('x')
        data.append([words[2], words[3]])
        width = int(words[2][0]) + int(words[3][0])
        height = int(words[2][1]) + int(words[3][1])
        if width > maxWidth:
            maxWidth = width
        if height > maxHeight:
            maxHeight = height

fabric = [[0 for x in range(maxHeight)] for y in range(maxWidth)]
totalSquares = maxWidth * maxHeight
# Using claims to tell how many squares (value) are claimed how many times (index)
# In other words, how many squares are claimed 2 times? -> print(claims[2])
claims = [totalSquares]

for elem in data:
    wStart = int(elem[0][0])
    wEnd = wStart + int(elem[1][0])
    hStart = int(elem[0][1])
    hEnd = hStart + int(elem[1][1])
    for w in range(wStart, wEnd):
        for h in range(hStart, hEnd):
            #print(fabric[w][h])
            fabric[w][h] += 1
            if fabric[w][h] == len(claims):
                claims.append(0)
            index = fabric[w][h]
            claims[index] += 1
            claims[index-1] -= 1
            
print(claims)

answer = totalSquares - claims[0] - claims[1]

print(answer)
