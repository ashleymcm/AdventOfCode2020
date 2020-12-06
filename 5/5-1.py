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

#loop through all seats and calculate the seat id for each, storing it if it's 
#higher than the one saved, then returning that at the end
def findHighestSeatId(seats):
  highest = 0
  for seat in seats:
    seat_id = determineSeatId(seat)
    if seat_id > highest:
      highest = seat_id
  
  return highest

print(findHighestSeatId(seats))