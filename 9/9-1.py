import os, sys, itertools

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "numbers"
with open(os.path.join(dirname, "input.txt")) as numbers_list:
  numbers = [int(numbers) for numbers in numbers_list]

#helper function to determine if the number is valid as per the problem, i.e 
#a number is valid if it is the sum of any of its 2 previous 25 numbers
def isValidNumber(numbers, index, preamble_length):
  start = index - preamble_length 
  #calling this the preamble even though it's technically not but I wanted a 
  #name for it - it's the previous 25 (or whatever number is given) numbers
  preamble = numbers[start:index] 

  #loops combination of the preamble and returns True if any sum correctly
  for x, y in itertools.combinations(preamble, 2):
    if x + y == numbers[index]:
      return True

  return False

#loop through all numbers and return the first one that is not valid
def findFirstInvalidNumber(numbers, preamble_length):
  for index in range(25, len(numbers)):
    if not isValidNumber(numbers, index, preamble_length):
      return numbers[index]

  #for if it's never found, even though duh it will be
  return -1

print(findFirstInvalidNumber(numbers, 25))  
