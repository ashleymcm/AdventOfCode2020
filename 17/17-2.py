import os, sys, itertools

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "starting_region"
with open(os.path.join(dirname, "input.txt")) as starting_region:
  starting_region = starting_region.read().split("\n")

ACTIVE = '#'
INACTIVE = '.'

def getCube(x, y, z, w):
  global dimension
  #get dimension with key of coordinates, return INACTIVE otherwise since we know
  #the dimension is infinite and default state is inactive
  return dimension.get((x, y, z, w), INACTIVE)

def isActive(x, y, z, w):
  return getCube(x, y, z, w) == ACTIVE

def findNeighbours(x, y, z, w):
  range_x = range(x - 1, x + 2)
  range_y = range(y - 1, y + 2)
  range_z = range(z - 1, z + 2)
  range_w = range(w - 1, w + 2)
  #get all combinations of coordinates
  neighbours = list(itertools.product(range_x, range_y, range_z, range_w))
  neighbours.remove((x, y, z, w)) #and then remove the current one since we are not our own neighbour

  return neighbours

def numberOfActiveNeighbours(x, y, z, w):
  neighbours = findNeighbours(x, y, z, w)
  active = 0

  for neighbour in neighbours:
    if isActive(*neighbour):
      active += 1

  return active

def initializeDimension(starting_region):
  dimension = dict()
  for y in range(len(starting_region)):
    for x in range(len(starting_region[0])):
      dimension[(x, y, 0, 0)] = starting_region[y][x]

  return dimension

def cycleCubes(dimension):
  cycled_dimension = dict()

  #loop through and apply the rules given to us in the problem
  for cube in dimension:
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
