import os, sys, collections

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#get "groups" stored as two-new-line-separated strings in the text file
with open(os.path.join(dirname, "input.txt")) as groups_lists:
  groups = groups_lists.read().split("\n\n")

#helper function where we determine the count for the group, i.e. total 
#number of questions ALL members of the group answered "yes" to
def getGroupYesCount(group):
  #split group into individual persons' answers and get group size based on length
  persons = group.split("\n")
  group_size = len(persons)
  
  #initialize count to 0 and "big_ol_string" to an empty string: in this string
  count = 0
  big_ol_string = ""

  #loop through every person and add that string to "big_ol_string", creating one
  #string that contains every single answer any group member has answered yes to
  for person in persons:
    big_ol_string += person

  #create a Counter from "big_ol_string" which will return an object listing counts 
  #each character in the given string
  counter = collections.Counter(big_ol_string)

  #create a set from "big_ol_string" to get only the unique characters, or "answers"
  character_set = set(big_ol_string)

  #loop through each unique character answered yes to 
  for i in character_set:
    #if the count for the character is as much as the group size then everyone has
    #answered "yes" to it, so we can add one to the overall count that we will return
    if counter[i] >= group_size:
      count += 1

  return count

#loop through all groups and get count for each, return sum of counts
def getSumOfCounts(groups):
  count_sum = 0
  for group in groups:
    count_sum += getGroupYesCount(group)

  return count_sum

print(getSumOfCounts(groups))