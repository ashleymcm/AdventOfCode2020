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

#helper function that, given a rule and list of values, determines if they are all valid for the given rule
def isValidForAll(rule, index):
  global rules, valid_tickets
  
  #loop through all tickets and return False if we find one of them that is not valid at the given index for the rule
  for ticket in valid_tickets:
    if not isValidField(rule, ticket[index]):
      return False

  #or return True if we got this far since it means they were all valid
  return True

#helper to find all invalid tickets
def findInvalidTickets():
  global nearby_tickets

  #list to store the possible valid tickets we find
  invalid_tickets = []

  #loop through all nearby tickets to find invalid tickets to be removed
  for i, ticket in enumerate(nearby_tickets):
    #and loop again through all values in each ticket
    for value in ticket:
      #if the value is not valid for at least one rule, add it to the list
      if not isValidForAtLeastOneField(value):
        invalid_tickets.append(i)
        break
  
  return invalid_tickets

def determineWhichFieldIsWhich():
  global my_ticket

  #initialize a field_order dict which we will use to help us determine the field order
  field_order = dict()
  for rule in rules:
    field_order[rule] = []

  #loop through fields of all tickets and determine all possible indices that it could represent
  for i in range(len(my_ticket)):
    #loop through all rules and append to field_order if the index is validForAll - this means 
    #it could potentially be the correct index for that field
    for rule in rules:
      if isValidForAll(rule, i):
        field_order[rule].append(i)

  #sort field_order by size, ascending
  field_order = dict(sorted(field_order.items(), key=lambda i: len(i[1])))

  #from looking at what field_order looks like at this point we can see that the first item has 
  #an array of length 1, and each subsequent array has a length of the previous + 1. So, since we
  #know that if a field only has one possibility, it is the actual correct index. So we set its value
  #to that and remove it from all the other arrays since it is no longer a possibility. We do this in a 
  #loop and eventually we only have one index per field. Yay. 
  for field in field_order:
    val = field_order[field][0] # we should only have one item in the array each time we're here
    field_order[field] = val
    for oth in field_order:
      #if the value is an array and val is in that array, remove it because we know that it has already
      #been claimed by the current field and is no longer a possibility for any other field
      if isinstance(field_order[oth], list) and val in field_order[oth]:
        field_order[oth].remove(val)

  return field_order

#### MAIN CODE START HERE, BUT OBVIOUSLY TONS OF LOGIC IS IN HELPER FUNCTIONS
#### MY BRAIN IS VERY TIRED ZZZZZZZ 

#list to store the possible valid tickets we find
invalid_tickets = findInvalidTickets()

#find and store our valid tickets using what we know about our invalid tickets
valid_tickets = [i for j, i in enumerate(nearby_tickets) if j not in invalid_tickets]

#determine which field is which and store it to be used to calculate our product
field_indices = determineWhichFieldIsWhich()

#now that we know which field is which, we find all indices that represent a "departure" field
fields = []
for field in field_indices:
  if 'departure' in field:
    fields.append(field_indices[field])

#and then multiply all the fields found at those indices on our ticket together to get the requested product
product = 1
for i in fields:
  product *= my_ticket[i]

print(product)
