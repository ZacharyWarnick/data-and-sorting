
'''
File: TopoSort.py

Description: Identifies cycles and topologically sorts graphs.
'''

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top
  def peek (self):
    return self.stack[-1]

  # check if the stack is empty
  def is_empty (self):
    return (len(self.stack) == 0)

  # return the number of items in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []   # a list of Vertex objects
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a lable get the index of the vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if not self.has_vertex (label):
      self.Vertices.append (Vertex (label))

      # add a new column in the adjacency matric
      nVert = len(self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append(0)

      # add a new row for the new Vertex in the adjacency matrix
      new_row = []
      for i in range (nVert):
        new_row.append (0)
      self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat [start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat [start][finish] = weight
    self.adjMat [finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # do depth first search in a graph
  def dfs (self, v):
    # create a Stack
    theStack = Stack ()

    # mark vertex v as visited and push it on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  def bfs(self,v):

    idx = v

    v = self.Vertices[v]


    visited = [False] * len(self.Vertices)

    theQueue = Queue()

    theQueue.enqueue (v)
    v.visited = True


    while not theQueue.is_empty():

      v = theQueue.dequeue()
      print(v.label)

      for n in self.Vertices:
        if n.visited is not True:
          theQueue.enqueue(n)
          n.visited = True

     
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  def getEdgeWeigth(self,fromVertexLabel,toVertexLabel):

    return(self.adjMat [self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)])

  def deleteEdge(self,fromVertexLabel,toVertexLabel):

    self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)] = 0
    self.adjMat[self.get_index(toVertexLabel)][self.get_index(fromVertexLabel)] = 0

  def getNeighbors(self,vertex):

    idx = self.get_index(vertex)

    for i in range(len(self.adjMat[idx])):

      if self.adjMat[idx][i] >= 1:
        print(self.Vertices[i])

  def getDirEdgeTo(self,vertex):

    connectedList = []
    idx = self.get_index(vertex)

    for i in range(len(self.adjMat[idx])):

      if self.adjMat[i][idx] >= 1:
        connectedList.append(self.Vertices[i])

    return connectedList

  def getDirEdgeFrom(self,vertex):

    connectedList = []
    idx = self.get_index(vertex)

    for i in range(len(self.adjMat[idx])):

      if self.adjMat[idx][i] >= 1:
        connectedList.append(self.Vertices[i])

    return connectedList

  def hasCycleHelper(self,v):

    # create a Stack
    children = self.getDirEdgeTo(self.Vertices[v])
    theStack = Stack ()
  
  
    # mark vertex v as visited and push it on the stack
    (self.Vertices[v]).visited = True
    theStack.push (v)

    u = None
    # visit other vertices according to depth
    while (not theStack.is_empty()):

      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())        
      if (u == -1):
        u = theStack.pop()

      else:

        (self.Vertices[u]).visited = True
        if u in theStack.stack:
          return True
        else: 
          theStack.push (u)

      #if the current node is in the children which point to the first node, there is a cycle in the DFS
      if self.Vertices[u] in children:
        return True

    return False




    # the stack is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
        
  def hasCycle(self):

    for i in range(len(self.Vertices)):

      if self.hasCycleHelper(i):
        return True

    return False

  def initialize(self):

    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  def topoSortHelper(self, v, stack):

    global theStack
    children = self.getDirEdgeTo(v)
    #print([x.label for x in children])
    v.visited = True

    for vertex in children:
      if vertex.visited == False:
        self.topoSortHelper(vertex,theStack)

    theStack.push(v)
    #print([i.label for i in theStack.stack])

  def topoSort(self):

    global theStack 

    for v in self.Vertices:
      #print(v.label)
      if v.visited == False:
        self.topoSortHelper(v,theStack)

    #print([x.label for x in self.Vertices])
    return([i.label for i in theStack.stack])



  def deleteVertex(self,vertex):

    idx = self.get_index(vertex)

    for i in range(len(self.adjMat)):

      del self.adjMat[i][idx]

    del self.adjMat[idx]

    del self.Vertices[idx]

def main():
  # create a Graph object
  network = Graph()

  # open the file for reading
  in_file = open ("./topo.txt", "r")

  # read the Vertices
  num_vertices = int ((in_file.readline()).strip())


  for i in range (num_vertices):
    vert = (in_file.readline()).strip()

    network.add_vertex (vert)




  # read the edges
  num_edges = int ((in_file.readline()).strip())


  vertIndexes = [x.label for x in network.Vertices]
  for i in range(num_edges):
    edge = (in_file.readline()).strip().split()


    start = vertIndexes.index(edge[0])
    end = vertIndexes.index(edge[1])


    network.add_directed_edge(start,end)



  global theStack
  theStack = Stack()

  network.initialize()
  network.topoSort()

  print()
  print("Does the graph have a cycle:", network.hasCycle())
  print()
  print("Vertices of the graph:")
  print(([x.label for x in network.Vertices]))
  print()
  print("Topological sort of the graph:")
  print(network.topoSort())


if __name__ == "__main__":
  main()