import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#get "seats" stored as line-separated strings in the text file
with open(os.path.join(dirname, "input.txt")) as seat_list:
  seats = seat_list.read().split("\n")

#helper function to determine row number, which is really just translating
#the string to a binary number where B=1 and F=0 and returning it as an int
def determineRowNumber(row):
  rowNum = row.replace("B", "1").replace("F", "0")
  return int(rowNum, 2)

#helper function to determine row number, which is really just translating
#the string to a binary number where R=1 and L=0 and returning it as an int
def determineColNumber(col):
  colNum = col.replace("R", "1").replace("L", "0")
  return int(colNum, 2)

#helper function to determine the seat id by using the helpers above and 
#using them in the math equation given in the problem
def determineSeatId(seat):
  row = seat[:-3]
  col = seat[-3:]

  rowNum = determineRowNumber(row)
  colNum = determineColNumber(col)

  return (rowNum * 8) + colNum

#loop through all seats and find the one that is missing
def findMissingSeatId(seats):
  #first loop through all seats and get + store their ids
  seat_ids = []
  for seat in seats:
    seat_ids.append(determineSeatId(seat))
  
  #sort the list so we can more easily find the missing id
  seat_ids.sort()

  #loop through the sorted ids and find the one that is missing: it will be a missing "step",
  #so it will be noticeable when the current id is 2 greater than the previous id rather than 
  #only 1 greater like usual
  for seat_id in range(1, len(seat_ids)):
    if seat_ids[seat_id] == seat_ids[seat_id - 1] + 2:
      return seat_ids[seat_id] - 1 #return current value minus 1, which is what was missing

print(findMissingSeatId(seats))