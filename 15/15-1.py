import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#helper function to look through list backward and send index of found item, sentinal of -1 if not found
def findLatestIndexInList(numbers, number):
  for i, val in reversed(list(enumerate(numbers))):
    if val == number:
      return i
  return -1


#loop through input rows, or "starting_numbers"
with open(os.path.join(dirname, "input.txt")) as starting_numbers:
  starting_numbers = [int(starting_number) for starting_number in starting_numbers.read().split(",")]

#setup our array of numbers and starting index for our loop
numbers = starting_numbers + []
i = len(numbers) - 1

#loop 2020x (2019 because we know our arrays start at 0 and not 1)
while i < 2019:
  #find latest index of current number, excluding the one we just put in
  find = findLatestIndexInList(numbers[:-1], numbers[i])

  #if it's greater than zero, we append the "age" to the array
  if find >= 0:
    age = i - find
    numbers.append(age)
  #otherwise it's brand new! and we append 0
  else:
    numbers.append(0)
  
  #increment our index
  i += 1

#print the last item in our numbers array, could've done numbers[2019] since we know that's the
#location but i like slicing the end off and don't super care about performance rn
print(numbers[-1])
