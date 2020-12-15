import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "input_data"
with open(os.path.join(dirname, "input.txt")) as input_data:
  input_data = input_data.read().split("\n")

#helper that applies mask to an index (or address) and then returns the result
def applyMask(mask, index):
  #translate it to binary and then prepend it with zeroes to get the correct length
  index = bin(index)[2:].rjust(36, '0')

  #loop through characters and update mask if it is anything but a zero
  for i in range(len(mask)):
    char = mask[i]
    if char == 'X' or char == '1':
      index = index[:i] + char + index[i+1:]

  return index

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

#helper method that extrapolates all possible indices given an index and an optional
#prefix by recursing so long as there are more Xs
def getAllPossibleAddresses(index, prefix = ""):
  indices = []
  remaining_x = index.count('X')

  #loop through all characters in index
  for i in range(len(index)):
    #if character is an X, replace it with a 0 and a 1 and add the given prefix
    if index[i] == 'X':
      replace_0 = prefix + index[:i] + '0' + index[i+1:]
      replace_1 = prefix + index[:i] + '1' + index[i+1:]

      #if there are no more Xs append these two strings to indices
      if remaining_x == 1:
        indices.append(replace_0)
        indices.append(replace_1)
      #otherwise recurse along each string and append *those* results to indices
      else:
        indices += getAllPossibleAddresses(replace_0[i+1:], replace_0[:i+1])
        indices += getAllPossibleAddresses(replace_1[i+1:], replace_1[:i+1])
      
      #just break here because we really only care about the first occurrence of X
      break
  
  return indices

#helper method that stores value in all appropriate indices
def storeValueAtIndex(memory, mask, index, value):
  index = applyMask(mask, index)
  #get all possible indices using helper above
  indices = getAllPossibleAddresses(index)

  #loop through indices and store, pretty ez
  for i in indices:
    memory[i] = value

  #return updated memory
  return memory

mask = ""
memory = {}

#loop through input data and perform appropriate action using helper methods above
for row in input_data:
  if row[0:4] == "mask":  #if mask update the mask
    mask = getMask(row)
  else:                   #otherwise we store the masked value in the memory
    index, value = getIndexAndValue(row)
    memory = storeValueAtIndex(memory, mask, index, value)

#get sum of all values in memory
total = 0
for i in memory:
  total += memory[i]

print(total)
    