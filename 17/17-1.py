import os, sys, itertools

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "starting_region"
with open(os.path.join(dirname, "input.txt")) as starting_region:
  starting_region = starting_region.read().split("\n")

ACTIVE = '#'
INACTIVE = '.'

def getCube(x, y, z):
  global dimension

  return dimension.get((x, y, z), INACTIVE)

def isActive(x, y, z):
  return getCube(x, y, z) == ACTIVE

def findNeighbours(x, y, z):
  range_x = range(x - 1, x + 2)
  range_y = range(y - 1, y + 2)
  range_z = range(z - 1, z + 2)
  neighbours = list(itertools.product(range_x, range_y, range_z))
  neighbours.remove((x, y, z))

  return neighbours

def numberOfActiveNeighbours(x, y, z):
  neighbours = findNeighbours(x, y, z)
  active = 0

  for neighbour in neighbours:
    if isActive(*neighbour):
      active += 1

  return active

def initializeDimension(starting_region):
  dimension = dict()
  for y in range(len(starting_region)):
    for x in range(len(starting_region[0])):
      dimension[(x, y, 0)] = starting_region[y][x]

  return dimension

def cycleCubes(dimension):
  cycled_dimension = dict()

  for cube in dimension:
    #add neighbours to dimension 
    number_of_active_neighbours = numberOfActiveNeighbours(*cube)
    if isActive(*cube):
      if number_of_active_neighbours == 2 or number_of_active_neighbours == 3:
        cycled_dimension[cube] = ACTIVE
      else:
        cycled_dimension[cube] = INACTIVE
    else: #cube is currently inactive
      if number_of_active_neighbours == 3:
        cycled_dimension[cube] = ACTIVE
      else:
        cycled_dimension[cube] = INACTIVE
    
  return cycled_dimension

dimension = initializeDimension(starting_region)

for i in range(6):
  #add any missing and possibly relevant neighbours to the dimension
  beeg_dimension = dimension.copy()
  for cube in dimension:
    neighbours = findNeighbours(*cube)
    for neighbour in neighbours:
      beeg_dimension[neighbour] = getCube(*neighbour)
  dimension = beeg_dimension

  #do a cycle on our updated dimension
  dimension = cycleCubes(dimension)

count = 0
for cube in dimension:
  if isActive(*cube):
    count += 1

print(count)
