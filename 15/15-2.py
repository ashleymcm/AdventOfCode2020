import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

with open(os.path.join(dirname, "input.txt")) as starting_numbers:
  starting_numbers = [int(starting_number) for starting_number in starting_numbers.read().split(",")]

#NOTE: my part 1 was absolutely not performant enough to tackle part 2 so I rewrote it... lol eff my life

#we using dicts now to keep track of the numbers where the key will be a number and its value will be the 
#last time it was said, aka its latest index
numbers = {}

#put our first starting numbers in, except the last one
for i in range(len(starting_numbers) - 1):
  numbers[starting_numbers[i]] = i

#set up our index for looping and get the last_num
i = len(numbers)
last_num = starting_numbers[-1]

#loop through 30000000 times as requested, ugh
while i < 29999999:
  #set as zero for now, we'll change it if the last_num exists in the dict
  next_num = 0

  #try getting the value for last_num, aka its index if it's been said before, otherwise return a sentinel of -1
  last_ind = numbers.get(last_num, -1)
  
  #as mentioned, if we found it update the next_num to be the "age" of the last_num, aka current index minus last index
  if last_ind >= 0:
    next_num = i - last_ind

  #store the last_num in our dict now that we know what our next_num will be
  numbers[last_num] = i

  #update last_num and incrememnt our counter
  last_num = next_num
  i += 1

#print the last_num "spoken"
print(last_num)

  



