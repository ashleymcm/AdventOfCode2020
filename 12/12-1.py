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

#helper function that turns left, assuming we're only turning in multiples
#of 90 degress and no more than 270. Returns new direction.
def turnLeft(facing, degrees):
  quarter_turns = degrees / 90
  facing -= quarter_turns
  if facing < 0:
    facing += 4
  return facing

#helper function that turns right, assuming we're only turning in multiples
#of 90 degress and no more than 270. Returns new direction.
def turnRight(facing, degrees):
  quarter_turns = degrees / 90
  facing += quarter_turns
  if facing > 3:
    facing -= 4
  return facing

#helper function that moves in the given direction the given amount. Returns
#new x, y coordinates
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

#main method that loops thorugh all directions and "performs" then, then returns
#the Manhatten distance at the very end
def moveAndFindManhattenDistance(directions):
  #the problem says that we start by facing east at 0,0
  facing = cardinalities['E']
  x = 0
  y = 0

  #loop through directions and perform each action/move
  for direction in directions:
    action = direction[0]
    number = direction[1]
    
    if action == 'F':   #move forward
      x, y = moveInDirection(facing, number, x, y)
    elif action == 'L': #turn left
      facing = turnLeft(facing, number)
    elif action == 'R': #turn right
      facing = turnRight(facing, number)
    else:               #if not one of the above, we just move in the given direction
      x, y = moveInDirection(cardinalities[action], number, x, y)

  #Manhatten distance calculation, given to us in the problem
  return abs(x) + abs(y)

print(moveAndFindManhattenDistance(directions))