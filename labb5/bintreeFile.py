
# Första uppgiften: Skriv en klass för binära sökträd

class Node:   

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Bintree: 

    def __init__(self):
        self.root = None

    def put(self, newvalue):
        # Sorterar in newvalue i trädet

        if self.root == None: # om root saknas
            self.root = putta(newvalue, self.root) # blir root det nya värdet
        else:
            putta(newvalue, self.root) # annars anropar vi putta funktionen 

    def __contains__(self, value):
        # True om value finns i trädet, False annars
        return finns(value, self.root)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


# globala funktioner som anropas av klassens metoder

def putta(value, node): # notera node är rooten första gången 
    # ser till att en ny nod skapas på rätt ställe

    tmp = Node(value) # skapar en nod för value

    if node == None: # om det inte finns några noder
        return tmp # skapar vi en nod som blir vår root

    elif tmp.value < node.value: # fallet då nya värdet < noden 
        if node.left == None: # om det är tomt
            node.left = tmp # in nya värdet 
        else:
            putta(value, node.left) # rekusivt, nyavärdet jämförs med noden vi är på
          
    elif tmp.value > node.value:
        if node.right == None:
            node.right = tmp
        else:
            putta(value, node.right)

def finns(value, node): 

    if node == None: # om trädet är helt tomt
        return False

    elif value < node.value:
        return finns(value, node.left)

    elif value > node.value:
        return finns(value, node.right)

    elif value == node.value:
        return True

def skriv(node):
    # skriver ut trädet inorder: LPR
    if node.left != None:
        skriv(node.left)

    print(node.value, end = ' ')

    if node.right != None:
        skriv(node.right)

    # skriver ut trädet postorder: LRP
    '''if node.left != None:
        skriv(node.left)

    if node.right != None:
        skriv(node.right)

    print(node.value, end = ' ')'''

    # skriver ut trädet preorder: PLR

    '''print(node.value, end = ' ')

    if node.left != None:
        skriv(node.left)

    if node.right != None:
        skriv(node.right)'''


# test
'''
def makeTree():
    tree = Bintree()
    data = input().strip()
    while data != "#":
        tree.put(data)
        data = input().strip()
    return tree

def searches(tree):
    findme = input().strip()
    while findme != "#":
        if findme in tree:
            print(findme, "found")
        else:
            print(findme, "not found")
        findme = input().strip()

def main():
    tree = makeTree()
    searches(tree)
    
main()'''


# visar inorder, preorder, postorder
'''
tree = Bintree()

tree.put(7)
print(tree.__contains__(7))

tree.put(4)
tree.put(5)
tree.put(1)
tree.put(0)
tree.put(2)

#print(tree.__contains__(7))

tree.write()'''


        


