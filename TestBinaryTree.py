'''
Demonstration of binary tree creation and methods
'''

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # insert some data into the tree
  def insert (self, data):

    new_node = Node(data)
    if self.search(data):
      return

    if (self.root == None):
      self.root = new_node

    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current

        if ((data) < (current.data)):
          current = current.lchild
        else:
          current = current.rchild

      if ((data) < (parent.data)):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # search for a node with a given data, returns boolean if present, can stop duplicates
  def search (self, data):
    current = self.root
    while (current is not None) and (current.data != data):
      if (data < current.data):
        current = current.lchild
      else:
        current = current.rchild

    return current != None




  def step_search(self,ch):

    output = ""
    current = self.root

    if not self.search(ch):
      output += ""

    elif ch == self.root.data:
      output +=  "*"

    while (current is not None) and (current.data != ch):
      if (ch < current.data):
        current = current.lchild
        output += "<"
      else:
        current = current.rchild
        output += ">"

    return output #returns the instructions to get to a particular character in the tree

  def in_order_print(root):

    if not root:
      return
    in_order_print(root.lchild)
    print (root.data)
    in_order_print(root.rchild)

  def print_node (self, data):
    current = self.root
    while (current is not None) and (current.data != data):
      if (data < current.data):
        current = current.lchild
      else:
        current = current.rchild

    return current

  def traverse(self,st):
    #print(st)

    current = self.root

    for ch in st:
      if ch == ">" and current is not None:
        current = current.rchild
      elif ch == "<" and current is not None:
        current = current.lchild
      else:
        return ""

    try:
      return current.data
    except AttributeError:
      return ""

  def encrypt(self,st):

    output = ""
    for n in st:

      output += self.step_search(n)
      output += "!"
    
    output = output[:-1]

    return output

  def decrypt(self,st):
    
    output = ""
    temp = ""
    current = self.root
    temp = ""

    for ch in (st):
      if ch == "*":   #Add root and look for new instruction
        temp = ""
        continue

      elif ch == "!": #Indicates a new set of instructions to follow, so preint the last set's character and go on
        output += self.traverse(temp)
        temp = ""
        continue

      elif ch == ">" or ch == "<":
        temp += ch

    output += self.traverse(temp)





    return(output)

  def is_similar(self,other):

    selfStart = self.root
    otherStart = other.root

    if selfStart is None and otherStart is None: 
        return True 

    if selfStart is not None and otherStart is not None: 
        return ((selfStart.data == otherStart.data) and 
                is_similarRecurse(selfStart.lchild, otherStart.lchild)and
                is_similarRecurse(selfStart.rchild, otherStart.rchild))

  def printLevel(self , level): 

    if self.root is None:
      return

    elif level == 1:
      print (self.root.data, end = " ")

    else:
      printLevelRecurse(self.root.lchild,level - 1)
      printLevelRecurse(self.root.rchild,level -1 )

  def getHeight(self):

    start = self.root

    if start is None:
      return 0

    else:
      lHeight = getHeightRecurse(start.lchild)
      rHeight = getHeightRecurse(start.rchild)

      if lHeight > rHeight:
        return lHeight + 1
      else:
        return rHeight + 1

  def getNumNodes(self):

    start = self.root


    if start is None:
      return 0

    left = GLH(start) + 1
    right = GRH(start) + 1

    if left == right:
      return (2 << left-1) -1 

    else:
      return getNumNodesRecurse(self.root) + getNumNodesRecurse(self.root)



def GLH(node):

  if node is None:
    return 0

  else:
    height = 0

    while node.lchild != None:
      height +=1
      node = node.lchild

  return height

def GRH(node):

  if node is None:
    return 0

  else:
    height = 0

    while node.rchild != None:
      height +=1
      node = node.rchild

  return height  

def is_similarRecurse(first,second):

  if first is None and second is None: 
      return True 

  if first is not None and second is not None: 
              return ((first.data == second.data) and 
              is_similarRecurse(first.lchild, second.lchild) and
              is_similarRecurse(first.rchild, second.rchild))

def getNumNodesRecurse(node):

  if node is None:
    return 0

  left = GLH(node) + 1
  right = GRH(node) + 1

  if left == right:
    return ((2 * left) - 1)

  else:
    return getNumNodesRecurse(node.lchild) + getNumNodesRecurse(node.rchild)

def printLevelRecurse(node, level):

  if node is None:
    return 

  elif level == 1:
    print (node.data, end = " ")

  else:
    printLevelRecurse(node.lchild,level - 1)
    printLevelRecurse(node.rchild,level -1 )  

def getHeightRecurse(node):

  if node == None:
    return 0

  lHeight = getHeightRecurse(node.lchild)
  rHeight = getHeightRecurse(node.rchild)

  if lHeight > rHeight:
    return lHeight + 1
  else:
    return rHeight + 1

def main():

  print()

  tree1 = Tree(); tree2 = Tree(); tree3 = Tree()

  pop = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]

  antipop = [3, 31, 43, 51, 4, 19, 20, 104, 39, 2]

  for n in (pop):
    tree1.insert(n); tree2.insert(n)

  for n in antipop:
    tree3.insert(n)


  print("Trees 1 and 2 are made from the list: ", pop)
  print("Tree 3 is made from: ", antipop)
  print()

    
  print("Are trees 1 and 2 similar? ", tree1.is_similar(tree2))
  print("Are trees 1 and 3 similar? ", tree1.is_similar(tree3))
  print()

  print("Level 2 of tree 1:", end = " ")
  print(tree1.printLevel(2))
  print("Level 4 of tree 1:", end = " ")
  print(tree1.printLevel(4)) 

  print()
  print("Height of tree 2: ", tree2.getHeight())
  print("Height of tree 3: ", tree3.getHeight())  

  print()
  print("Number of nodes in tree 1: ",(tree1.getNumNodes()))
  print("Number of nodes in tree 3: ",(tree3.getNumNodes()))


if __name__ == '__main__':
  main()