import fileinput

doubles = 0
triples = 0


# Generates chars from c1 to c2 (inclusive)
# Borrowed from Ned Batchelder's answer to
# https://stackoverflow.com/questions/7001144/range-over-character-in-python
def char_range(c1, c2):
    for c in range (ord(c1), ord(c2)+1):
        yield chr(c)



for line in fileinput.input():
    doubleFound = False
    tripleFound = False
    
    for letter in char_range('a', 'z'):
        # Move to next line if a double and triple have already been found.
        if doubleFound and tripleFound:
            break
        
        occurances = line.count(letter)
        if occurances == 2 and not doubleFound:
            doubles += 1
            doubleFound = True
        elif occurances == 3 and not tripleFound:
            triples += 1
            tripleFound = True

checksum = doubles * triples

print(checksum)

fileinput.close()
