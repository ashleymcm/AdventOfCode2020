import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#get "groups" stored as two-new-line-separated strings in the text file
with open(os.path.join(dirname, "input.txt")) as groups_lists:
  groups = groups_lists.read().split("\n\n")

#helper function where we determine the count for the group, i.e. total 
#number of unique questions answered "yes" to
def getGroupYesCount(group):
  #keep track of an overall set, which only keeps unique members
  yes_set = set()
  persons = group.split("\n")

  #loop through each person's answer and add the letters to the set
  for person in persons:
    person_set = set(person)
    yes_set.update(person_set)

  #return the length of the set, which is the number of unique letters
  return len(yes_set)

#loop through all groups and get count for each, return sum of counts
def getSumOfCounts(groups):
  count_sum = 0
  for group in groups:
    count_sum += getGroupYesCount(group)

  return count_sum

print(getSumOfCounts(groups))