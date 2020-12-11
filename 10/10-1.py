import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "joltages"
with open(os.path.join(dirname, "input.txt")) as joltages_list:
  joltages = [int(joltages) for joltages in joltages_list]

#helper method to get the arrangement using all adapters, which is just a sort
#plus some error checking to make sure the sorted arrangement is actually valid
#(i.e. no difference between consecutive items is greater than 3)
def arrangeAdapters(joltages):
  joltages.sort()
  for i in range(1,len(joltages)):
    difference = joltages[i] - joltages[i-1] 
    if difference > 3:
      raise Error("Sorting does not adequately arrange ALL adapters")
  return joltages

def findJoltageDifferences(joltages):
  #append the starting joltage of 0 and final backpack joltage of max + 3
  joltages.append(0)
  joltages.append(max(joltages) + 3)
  
  #arrange our adapters using our handy dandy helper above
  joltages = arrangeAdapters(joltages)

  #initialize our counts
  difference_1_count = 0
  difference_3_count = 0

  #loop through adapters and add to the appropriate counts
  for i in range(1, len(joltages)):
    difference = joltages[i] - joltages[i-1] 
    if difference == 3:
      difference_3_count += 1
    elif difference == 1:
      difference_1_count += 1

  #return the count product as requested
  return difference_1_count * difference_3_count

print(findJoltageDifferences(joltages))