import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "input_data"
with open(os.path.join(dirname, "input.txt")) as input_data:
  input_data = input_data.read().split("\n")

#first line is timestamp, second is bus routes/schedules
timestamp = int(input_data[0])
routes = input_data[1].split(',')
waittimes = []

#loop through routes and append them to an array
for route in routes:
  if route != 'x':
    waittimes.append([int(route) - timestamp%int(route), int(route)])

#a simple sort means the first one is the... well, "first" re: time one
waittimes.sort()

#print the product as requested
print(waittimes[0][0] * waittimes[0][1])