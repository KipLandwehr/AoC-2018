import fileinput

IDs = []

for line in fileinput.input():
    IDs.append(line)
    
fileinput.close()

for indexA, itemA in enumerate(IDs):
    for indexB, itemB in enumerate(IDs[indexA+1:]):
        identical = True
        mismatch = 0
        for indexC in range(0, len(itemA)-1):
            if itemA[indexC] != itemB[indexC] and identical:
                identical = False
                mismatch = indexC
            elif itemA[indexC] != itemB[indexC] and not identical:
                break
        else:
            answer = itemA[:mismatch] + itemA[mismatch+1:]
            print(answer)
            break

