import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#get the "rules" stored as a list from the input file
with open(os.path.join(dirname, "input.txt")) as raw_rules_rows:
  raw_rules = raw_rules_rows.read().splitlines()

#helper function to clean up messy input data into nice clean dict with format:
#{"STRING OF BAG COLOR": [LIST OF BAG COLORS IT CAN CONTAIN]}
def cleanRules(raw_rules):
  cleaned_rules = dict()
  for rule in raw_rules:
    split_rule = rule.split("contain")
    head = cleanHead(split_rule[0])
    body = cleanBody(split_rule[1])
    cleaned_rules[head] = body
  return cleaned_rules

#helper function for cleanRules function where we remove the trailing characters and get 
#just the color of the bag
def cleanHead(raw_head):
  return raw_head[:-6]

#helper function for cleanRules function where we parse the long string into a list of
#colors: first by splitting at the comma, then by splitting into words - colors are always the 
#second and third "words" after that split
def cleanBody(raw_body):
  cleaned_body = []
  if raw_body == " no other bags.":
    return cleaned_body
  raw_bags = raw_body.split(",")
  for bag in raw_bags:
    words = bag.split()
    color = words[1] + " " + words[2]
    cleaned_body.append(color)
  return cleaned_body

#recursive function to check if a given bag can contain a given color. if the given color is not found
#in its color list, it recursively searches the colors that ARE in the list until it finds it or reaches
#the end
def bagContainsColor(rules, bag, color):
  if len(rules[bag]) == 0:
    return False
  if color in rules[bag]:
    return True
  for sub_bag in rules[bag]:
    if bagContainsColor(rules, sub_bag, color):
      return True
  return False

#function that loops through all the rules and searches each for if it can contain the given color bag. 
#if it can, the color is added to the set, and the length of the set (or how many bags contain the given
#bag color) is returned
def countPossibleBags(raw_rules, color):
  rules = cleanRules(raw_rules)
  bags = set()
  for bag in rules:
    if bagContainsColor(rules, bag, color):
      bags.add(bag)

  return len(bags)

print(countPossibleBags(raw_rules, "shiny gold"))