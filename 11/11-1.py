import os, sys, itertools

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

#helper function that, given a coordinate of a seat, counts how many
#of the eight adjacent seats are occupied
def countOccupiedAdjacentSeats(seat_rows, seat_x, seat_y):
  length_x = len(seat_rows[0])
  length_y = len(seat_rows)
  min_x = seat_x - 1
  max_x = seat_x + 1
  min_y = seat_y - 1
  max_y = seat_y + 1

  if min_x < 0:
      min_x = seat_x
  elif max_x > length_x - 1:
      max_x = seat_x
  if min_y < 0:
      min_y = seat_y
  elif max_y > length_y - 1:
      max_y = seat_y

  range_x = range(min_x, max_x + 1)
  range_y = range(min_y, max_y + 1)
  all_seat_combos = list(itertools.product(range_x, range_y))
  
  count_occupied = 0

  for combo in all_seat_combos:
    x = combo[0]
    y = combo[1]
    
    if isOccupied(seat_rows, x, y):
      count_occupied += 1

  if isOccupied(seat_rows, seat_x, seat_y):
    count_occupied -= 1

  return count_occupied

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
      occupied_adjacent_seats = countOccupiedAdjacentSeats(seat_rows, x, y)
      if isEmpty(seat_rows, x, y) and occupied_adjacent_seats <= 0:
        coordinates_to_fill.append([x, y])
      if isOccupied(seat_rows, x, y) and occupied_adjacent_seats >= 4:
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

  
    
    