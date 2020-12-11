import os, sys, numpy

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "joltages"
with open(os.path.join(dirname, "input.txt")) as joltages_list:
  joltages = [int(joltages) for joltages in joltages_list]

#helper function to take list of joltages and create a dict (that represents
#edges in a graph)
def getEdges(joltages):
  edges = dict()

  for i in range(len(joltages)):
    maximum_range = 4
    if len(joltages) - i < 4:
      maximum_range = len(joltages) - i

    edges[joltages[i]] = []

    for j in range(1, maximum_range):
      difference = joltages[i + j] - joltages[i] 
      if difference < 4:
        edges[joltages[i]].append(joltages[i + j])

  return edges

#i had to go back to the ol' graph theory to remember this, but it takes a graph
#(or in this case edges and vertices) and creates an "adjacency matrix" which is
#really just a matrix representation of a graph that places a 1 at coordinates of
#all the edges and 0s otherwise
def getAdjacencyMatrix(edges, vertices):
  #create a square matrix representing the graph full of 0s
  matrix = [[0]*len(edges) for i in range(len(edges))]

  #initialize an index we'll use during our loop
  index = 0  

  #loop through all edges and place a 1 in all coordinates where an edge exists
  for edge in edges:
    for value in edges[edge]:
      matrix[index][vertices.index(value)] = 1
    index += 1

  #return as a matrix object with some help from numpy
  return numpy.matrix(matrix)

#i did not have the time or energy to name this better so it is what it is, but it uses
# the following theorem taken from a text:
# Theorem 1.1.3. Let A be the adjacency matrix of a simple graph G on vertices 
# v1, v2, . . . , vn. Let k be a positive integer. Then the entry in the (i, j)-position 
# of the matrix Ak is the number of walks of length k from vi to vj in G.
def letsDoMatrixMath(matrix, vertices):
  count = 0
  length = len(joltages) - 1

  #loop through the vertices
  for i in range(1, length + 1):
    #raise the matrix to the power of the loop/iteration #
    matrix_power = matrix**i
    #add the number in the (i, j)-position to the count, as it is the "number of walks of length k 
    #[or in this case i] from vi to vj" in our graph. Note that vi and vj are always 0 and the length
    #of our list of vertices because we are traversing from the starting adapter to the final adapter
    count += matrix_power.item(0, length)

  return count

#do the stupid thing
def countPossibleConfigurations(joltages):
  #append the starting voltage of 0 and then sort. Note that we don't have to append the backpack
  #because there's only ever the same path to it, so it is negligible.
  joltages.append(0)
  joltages.sort()
  
  #get our edges and then use em to create our matrix. Note that our vertices are just the joltages
  edges = getEdges(joltages)
  matrix = getAdjacencyMatrix(edges, joltages)
  
  return letsDoMatrixMath(matrix, joltages)

print(countPossibleConfigurations(joltages))