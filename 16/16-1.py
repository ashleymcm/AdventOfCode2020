import os, sys, re

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#helper that takes a ticket string and turns it into a list of ints
def cleanTicket(ticket):
  return list(map(int, ticket.split(",")))

#helper to parse the rules section
def parseRules(rules):
  parsed_rules = rules.split("\n")
  #storing rules in a dict with a string as key and list as value
  cleaned_rules = dict()
  for rule in parsed_rules:
    rule = rule.split(": ")
    field = rule[0]
    #using regex to take all the integers out of the possible values
    numbers = list(map(int, re.findall('\d+', rule[1])))
    #storing as mentioned in the dict
    cleaned_rules[field] = numbers

  return cleaned_rules

#helper to parse my ticket section
def parseMyTicket(ticket):
  #easy to clean, just using helper above on second line (discarding first line)
  parsed_ticket = ticket.split("\n")[1]
  cleaned_ticket = cleanTicket(parsed_ticket)
  return cleaned_ticket

#helper to parse nearby tickets section
def parseNearbyTickets(tickets):
  #easy to clean, similar to above method but doing it over a list instead of a single string
  parsed_tickets = tickets.split("\n")[1:]
  cleaned_tickets = []
  for ticket in parsed_tickets:
    cleaned_ticket = cleanTicket(ticket)
    cleaned_tickets.append(cleaned_ticket)

  return cleaned_tickets

#helper that uses helpers above to parse input data into useable format
def parseData(data):
  data = data.read().split("\n\n")         #breaks the input into three sections
  
  rules = parseRules(data[0])
  my_ticket = parseMyTicket(data[1])
  nearby_tickets = parseNearbyTickets(data[2])

  return rules, my_ticket, nearby_tickets  #return parsed three sections

#read our input text file and parse using helper method above
with open(os.path.join(dirname, "input.txt")) as input_data:
  rules, my_ticket, nearby_tickets = parseData(input_data)

#helper function that, given a rule and a value, returns True if the value is valid for that rule
def isValidField(rule, value):
  global rules
  ranges = rules[rule]
  #since we stored the values as a list of ints, we can determine validity by testing if the 
  #value is between the first and second item (inclusive) or the third and fourth item (inclusive)
  inFirstRange = value >= ranges[0] and value <= ranges[1]
  inSecondRange = value >= ranges[2] and value <= ranges[3]

  return inFirstRange or inSecondRange

#helper function that, given a value, determines if it is valid for at least one of the rules
def isValidForAtLeastOneField(value):
  global rules
  
  #just calling above helper for each rule in rules and returning True if the helper is ever True
  for rule in rules:
    if isValidField(rule, value):
      return True
  
  return False

#list to store the invalid values we find
invalidValues = []

#loop through all nearby tickets
for ticket in nearby_tickets:
  #and loop again through all values in each ticket
  for value in ticket:
    #if the value is not valid for at least one rule, add it to the list
    if not isValidForAtLeastOneField(value):
      invalidValues.append(value)

#print the sum of the invalid values
print(sum(invalidValues))
