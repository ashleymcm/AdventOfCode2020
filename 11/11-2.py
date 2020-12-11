import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "seat rows"
with open(os.path.join(dirname, "input.txt")) as seat_rows_list:
  seat_rows = seat_rows_list.read().split("\n")

#helper function that, when given a seat, determines if it is occupied
def isOccupied(seat_rows, seat_x, seat_y):
    return seat_rows[seat_y][seat_x] == "#"

#helper function that, when given a seat, determines if it is empty
def isEmpty(seat_rows, seat_x, seat_y):
    return seat_rows[seat_y][seat_x] == "L"

#helper function that, when given coordinates, determines if it is floor
def isFloor(seat_rows, seat_x, seat_y):
    return seat_rows[seat_y][seat_x] == "."

#the following helper functions are pretty straightforward - given coordinates
#they use recursion by moving along a single direction until either they reach
#the end of the grid or they reach a seat (something that isn't "."). The only
#difference between each is how we change x and y to represent direction

def getSeatN(seat_rows, seat_x, seat_y):
  if seat_y == 0:
    return "."
  seat_y -= 1
  if isFloor(seat_rows, seat_x, seat_y):
    return getSeatN(seat_rows, seat_x, seat_y)
  return seat_rows[seat_y][seat_x]

def getSeatS(seat_rows, seat_x, seat_y):
  if seat_y == len(seat_rows) - 1:
    return "."
  seat_y += 1
  if isFloor(seat_rows, seat_x, seat_y):
    return getSeatS(seat_rows, seat_x, seat_y)
  return seat_rows[seat_y][seat_x]

def getSeatW(seat_rows, seat_x, seat_y):
  if seat_x == 0:
    return "."
  seat_x -= 1
  if isFloor(seat_rows, seat_x, seat_y):
    return getSeatW(seat_rows, seat_x, seat_y)
  return seat_rows[seat_y][seat_x]

def getSeatE(seat_rows, seat_x, seat_y):
  if seat_x == len(seat_rows[0]) - 1:
    return "."
  seat_x += 1
  if isFloor(seat_rows, seat_x, seat_y):
    return getSeatE(seat_rows, seat_x, seat_y)
  return seat_rows[seat_y][seat_x]

def getSeatNW(seat_rows, seat_x, seat_y):
  if seat_y == 0 or seat_x == 0:
    return "."
  seat_x -= 1
  seat_y -= 1
  if isFloor(seat_rows, seat_x, seat_y):
    return getSeatNW(seat_rows, seat_x, seat_y)
  return seat_rows[seat_y][seat_x]

def getSeatNE(seat_rows, seat_x, seat_y):
  if seat_y == 0 or seat_x == len(seat_rows[0]) - 1:
    return "."
  seat_x += 1
  seat_y -= 1
  if isFloor(seat_rows, seat_x, seat_y):
    return getSeatNE(seat_rows, seat_x, seat_y)
  return seat_rows[seat_y][seat_x]

def getSeatSE(seat_rows, seat_x, seat_y):
  if seat_y == len(seat_rows) - 1 or seat_x == len(seat_rows[0]) - 1:
    return "."
  seat_x += 1
  seat_y += 1
  if isFloor(seat_rows, seat_x, seat_y):
    return getSeatSE(seat_rows, seat_x, seat_y)
  return seat_rows[seat_y][seat_x]

def getSeatSW(seat_rows, seat_x, seat_y):
  if seat_y == len(seat_rows) - 1 or seat_x == 0:
    return "."
  seat_x -= 1
  seat_y += 1
  if isFloor(seat_rows, seat_x, seat_y):
    return getSeatSW(seat_rows, seat_x, seat_y)
  return seat_rows[seat_y][seat_x]

#helper function that, given a coordinate of a seat, counts how many
#of the eight VISIBLE adjacent seats are occupied
def countOccupiedVisibleSeats(seat_rows, x, y):
  visible_seats = []
  visible_seats.append(getSeatS(seat_rows, x, y))
  visible_seats.append(getSeatN(seat_rows, x, y))
  visible_seats.append(getSeatW(seat_rows, x, y))
  visible_seats.append(getSeatE(seat_rows, x, y))
  visible_seats.append(getSeatNE(seat_rows, x, y))
  visible_seats.append(getSeatNW(seat_rows, x, y))
  visible_seats.append(getSeatSE(seat_rows, x, y))
  visible_seats.append(getSeatSW(seat_rows, x, y))

  return visible_seats.count("#")

#helper function to set a seat given its row, index, and what you want to set it to
def setSeat(row, x, character):
  new_row = row[:x] + character + row[x + 1:]
  return new_row

#helper functon to loop through all seats and note if a seat should be updated - at 
#the end of each loop the updates are "processed" and the new grid is returned along
#with a bool stating if any changes were made during this cycle
def cycleSeats(seat_rows):
  coordinates_to_fill = []
  coordinates_to_empty = []

  for y in range(len(seat_rows)):
    for x in range(len(seat_rows[y])):
      occupied_adjacent_seats = countOccupiedVisibleSeats(seat_rows, x, y)
      if isEmpty(seat_rows, x, y) and occupied_adjacent_seats <= 0:
        coordinates_to_fill.append([x, y])
      if isOccupied(seat_rows, x, y) and occupied_adjacent_seats >= 5:
        coordinates_to_empty.append([x, y])

  for coordinates in coordinates_to_fill:
    x = coordinates[0]
    y = coordinates[1]
    seat_rows[y] = setSeat(seat_rows[y], x, "#")

  for coordinates in coordinates_to_empty:
    x = coordinates[0]
    y = coordinates[1]
    seat_rows[y] = setSeat(seat_rows[y], x, "L")

  hasChanges = len(coordinates_to_fill) + len(coordinates_to_empty) > 0
  return seat_rows, hasChanges

#make changes according to the rules (and programmed in cycleSeats()) until
#no more changes are occurring. This means we've "stabilized" and can now return
#the number of occupied seats 
def countFinalOccupiedSeats(seat_rows):
  occupied_count = 0
  hasChanges = True

  while hasChanges:
    seat_rows, hasChanges = cycleSeats(seat_rows)

  for y in range(len(seat_rows)):
    for x in range(len(seat_rows[y])):
      if isOccupied(seat_rows, x, y):
        occupied_count += 1

  return occupied_count

print(countFinalOccupiedSeats(seat_rows))

  
    
    