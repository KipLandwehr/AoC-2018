input = []
with open("Day5/Input.txt") as f:
    input = list(f.readline().strip())


def char_range(c1, c2):
    for c in range (ord(c1), ord(c2)+1):
        yield chr(c)

def react(n):
    foundOne = True
    while foundOne:
        x = 0
        foundOne = False
        while x < len(n)-2:
            if n[x].isupper() and n[x+1].islower() and n[x] == n[x+1].upper():
                del n[x:x+2]
                foundOne = True
            elif n[x].islower() and n[x+1].isupper() and n[x] == n[x+1].lower():
                del n[x:x+2]
                foundOne = True
            else:
                x += 1

def rm(a, n):
    while a.upper() in n:
        n.remove(a.upper())
    while a.lower() in n:
        n.remove(a.lower())

minLength = -1

for letter in char_range('a', 'z'):
    workCopy = list(input)
    rm(letter, workCopy)
    react(workCopy)
    length = len(workCopy)
    if minLength == -1 or length < minLength:
        minLength = length


print(minLength)