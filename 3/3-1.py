import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#get a "map" stored as a list from the input file
with open(os.path.join(dirname, "input.txt")) as sled_map_rows:
  sled_map = sled_map_rows.read().splitlines()

def hasTree(sled_map, x, y): 
  #helper method that takes in a map and coordinates and returns 
  #True if and only if there is a tree (#) at that coordinate
  return sled_map[y][x] == '#'

def calculateX(current_x, slope_x, size_x):
  #helper method that calculates which x-coordinate to use from the
  #map - since we know the map repeats x-values, we can use the demodulo 
  #operator to find any repeating x-coordinate's value based on the map 
  return (current_x + slope_x) % size_x


def calculateNumTreesHit(sled_map, slope_x, slope_y):
  #given a sled_map and the x and y of the slope, calculate how
  #many trees would be hit along the path

  #initialize counts for calculations
  hit_count = 0             
  current_x = 0
  current_y = 0
  size_x = len(sled_map[0]) #since the map is a square, all rows will have same "width"
  size_y = len(sled_map)    #this is just the size of the list, or "height"

  #loop through rows until there are no rows left
  while (current_y < size_y):
    if (hasTree(sled_map, current_x, current_y)):
      hit_count += 1    #if there is a tree at the current position, increment hit count
    
    #augment the current_x and current_y values according to the slope and repeat (x-only)
    current_x = calculateX(current_x, slope_x, size_x)
    current_y += slope_y

  return hit_count

#print result
print(calculateNumTreesHit(sled_map, 3, 1))