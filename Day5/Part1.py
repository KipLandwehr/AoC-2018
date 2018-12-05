input = ""
with open("Day5/Input.txt") as f:
    input = list(f.readline().strip())

#def react(n):
#    if len(n) == 1:
#        return n
#    else:
#        if n[0].isupper() and n[1].islower() and n[0] == n[1].upper():
#            return react(n[2:])
#        elif n[0].islower() and n[1].isupper() and n[0] == n[1].lower():
#            return react(n[2:])
#        else:
#            return react(n[:2] + react(n[2:]))

foundOne = True

while foundOne:
    x = 0
    foundOne = False
    while x < len(input)-2:
        if input[x].isupper() and input[x+1].islower() and input[x] == input[x+1].upper():
            del input[x:x+2]
            foundOne = True
        elif input[x].islower() and input[x+1].isupper() and input[x] == input[x+1].lower():
            del input[x:x+2]
            foundOne = True
        else:
            x += 1

print(len(input))