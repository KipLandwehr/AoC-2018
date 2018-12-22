INPUTFILE="Day8/Input.txt"

# define myTree class
class MyTree:
    
    # define Node class
    class Node:
        def __init__(self, inList):
            self.numChildren = inList.pop()
            self.numMetaEntries = inList.pop()
            self.metaEntries = []
            self.children = []
            for _ in range(self.numChildren):
                self.children.append(MyTree.Node(inList))
            for _ in range(self.numMetaEntries):
                self.metaEntries.append(inList.pop())

        def getTotal(self):
            self.total = 0
            for x in range(self.numChildren):
                self.total += self.children[x].getTotal()
            for x in range(self.numMetaEntries):
                self.total += self.metaEntries[x]
            return self.total

    def __init__(self, inList):
        self.head = self.Node(inList)

    def getMetaTotal(self):
        return self.head.getTotal()

# get input from file and split into list of integers
data = ""
with open("{}".format(INPUTFILE)) as f:
    data = list(map(int, f.readline().strip().split()))

# reverse list to make pop() get the first number provided in the original input
data.reverse()

# create tree from "data" list
tree = MyTree(data)

# traverse tree and add metadata from all nodes
answer = tree.getMetaTotal()

#print(data)
print(answer)