import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "input_data"
with open(os.path.join(dirname, "input.txt")) as input_data:
  input_data = input_data.read().split("\n")

#helper that applies mask to a value and then returns the result as an int
def applyMask(mask, value):
  #translate it to binary and then prepend it with zeroes to get the correct length
  value = bin(value)[2:].rjust(36, '0')

  #loop through mask and if the character is not an X, replace it in value
  for i in range(len(mask)):
    char = mask[i]
    if char != 'X':
      value = value[:i] + char + value[i+1:]

  #translate it back to an int and return
  return int(value, 2)

#helper that just parses input data assuming it is a mask, simple string manipulation
def getMask(row):
  return row[7:]

#helper that just parses input data assuming it is an index-value pair, more simple
#string manipulation
def getIndexAndValue(row):
  split_row = row.split("] = ")
  index = int(split_row[0][4:])
  value = int(split_row[1])

  return index, value

mask = ""
memory = {}

#loop through input data and perform appropriate action using helper methods above
for row in input_data:
  if row[0:4] == "mask":  #if mask update the mask
    mask = getMask(row)
  else:                   #otherwise we store the masked value in the memory
    index, value = getIndexAndValue(row)
    memory[index] = applyMask(mask, value)

#get sum of all values in memory
total = 0
for i in memory:
  total += memory[i]

print(total)
    