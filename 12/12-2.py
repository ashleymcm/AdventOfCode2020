import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#assigning ints to directions for ease of calculations
cardinalities = {
  'E': 0,
  'S': 1,
  'W': 2,
  'N': 3
}

#helper function that "cleans" a direction string by separating the action from 
#the number and converting the number to an int
def clean(direction):
  action = direction[0]
  number = int(direction[1:])
  return [action, number]

#loop through input rows, or "directions"
with open(os.path.join(dirname, "input.txt")) as directions_list:
  directions = [clean(direction) for direction in directions_list]

#helper function that rotates waypoint left around ship, assuming we're only turning in 
#multiples of 90 degress and no more than 270. Returns new direction.
def rotateLeft(degrees, x, y):
  quarter_turns = degrees / 90
  if quarter_turns == 1:
    return -y, x
  if quarter_turns == 2:
    return -x, -y
  if quarter_turns == 3:
    return y, -x

#helper function that rotates waypoint right around ship, assuming we're only turning in 
#multiples of 90 degress and no more than 270. Returns new direction.
def rotateRight(degrees, x, y):
  quarter_turns = degrees / 90
  if quarter_turns == 1:
    return y, -x
  if quarter_turns == 2:
    return -x, -y
  if quarter_turns == 3:
    return -y, x

#helper function that moves in the given direction the given amount. Returns
#new x, y coordinates. Unchanged from part 1.
def moveInDirection(direction, number, x, y):
  if direction == cardinalities['N']:
    y += number
  elif direction == cardinalities['S']:
    y -= number
  elif direction == cardinalities['W']:
    x -= number
  elif direction == cardinalities['E']:
    x += number

  return x, y

#helper function that takes in the ship's and waypoint's coordinates plus a 
#"multipler" and moves the ship's coordinates toward the waypoint's coordinates
#multipler-many times
def moveTowardWaypoint(waypoint_x, waypoint_y, ship_x, ship_y, multiplier):
  ship_x += multiplier * waypoint_x
  ship_y += multiplier * waypoint_y

  return ship_x, ship_y

#main method that loops thorugh all directions and "performs" then, then returns
#the Manhatten distance of the ship at the very end
def moveAndFindManhattenDistance(directions):
  #the problem says where our ship and waypoint starts
  ship_x = 0
  ship_y = 0
  waypoint_x = 10
  waypoint_y = 1

  #loop through directions and perform each action/move
  for direction in directions:
    action = direction[0]
    number = direction[1]
    
    if action == 'F':   #move toward waypoint
      ship_x, ship_y = moveTowardWaypoint(waypoint_x, waypoint_y, ship_x, ship_y, number)
    elif action == 'L': #rotate left
      waypoint_x, waypoint_y = rotateLeft(number, waypoint_x, waypoint_y)
    elif action == 'R': #rotate right
      waypoint_x, waypoint_y = rotateRight(number, waypoint_x, waypoint_y)
    else:               #if not one of the above, we just move waypoint in the given direction
      waypoint_x, waypoint_y = moveInDirection(cardinalities[action], number, waypoint_x, waypoint_y)

  #Manhatten distance calculation, given to us in the problem
  return abs(ship_x) + abs(ship_y)

print(moveAndFindManhattenDistance(directions))