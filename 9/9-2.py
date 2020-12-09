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

#helper function that loops through all numbers and returns the first invalid's index
def findFirstInvalidNumber(numbers, preamble_length):
  for index in range(25, len(numbers)):
    if not isValidNumber(numbers, index, preamble_length):
      return numbers[index]
  
  #for if it's never found, even though duh it will be
  return -1   

#helper function that, given a starting index and a target sum, determines if the given
#index can be the start of a contiguous set of numbers that sums to the target
def getIndexIfValidSum(numbers, index, target):
  total_sum = numbers[index]
  index_incrementor = 0

  #loop through the list starting at the given index until the sum is >= to the target
  while total_sum < target:
    index_incrementor += 1
    total_sum += numbers[index + index_incrementor]

  #if the sum is equal to the target, return the ending index index
  if total_sum == target:
    return index + index_incrementor

  #otherwise return a sentinel value
  return -1

#loop through the list and find the contiguous set of numbers that sums to the first
#invalid number, then return the sum of the minimum and maximum of that list
def calculateEncryptionSum(numbers, preamble_length):
  first_invalid_sum = findFirstInvalidNumber(numbers, preamble_length)

  for index in range(len(numbers)):
    result = getIndexIfValidSum(numbers, index, first_invalid_sum)
    if result >= 0:
      #if the result it positive it means we found the contiguous sum and result contains
      #the ending index of the list so we can find that sub list, or "sum_list"
      sum_list = numbers[index:result+1]
      #and then return the sum of it's minimum and maximum
      return max(sum_list) + min(sum_list)
      
  #return a sentinel value here just in case everything borks
  return -1

print(calculateEncryptionSum(numbers, 25))  
