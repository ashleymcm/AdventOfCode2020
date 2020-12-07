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

#helper function for cleanRules function where we parse the long string into a dict of colors:quantity
#first by splitting at the comma, then by splitting into words - colors are always the 
#second and third "words" after that split and the quantity is the first
def cleanBody(raw_body):
  cleaned_body = dict()
  if raw_body == " no other bags.":
    return cleaned_body
  raw_bags = raw_body.split(",")
  for bag in raw_bags:
    words = bag.split()
    color = words[1] + " " + words[2]
    cleaned_body[color] = int(words[0])
  return cleaned_body

#recursive function to count all bags within bags of a given bag
def innerBagCount(rules, bag):
  count = 0
  sub_bags = rules[bag]

  if len(sub_bags) == 0:
    return count

  #loop through each sub_bag
  for sub_bag in sub_bags:
    #get the quantity, or multiplier for this sub_bag
    multiplier = sub_bags[sub_bag]
    #add it flat to the count since there are that many bags of that color in the given bag
    count += multiplier
    #then multiply all counts of inner bags by that number 
    count += multiplier * innerBagCount(rules, sub_bag)
  
  return count

rules = cleanRules(raw_rules)
print(innerBagCount(rules, "shiny gold"))