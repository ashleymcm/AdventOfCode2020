import os, sys, itertools

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "expenses"
with open(os.path.join(dirname, "input.txt")) as expenses_list:
  expenses = [int(expenses) for expenses in expenses_list]

def sumsTo2020(x, y, z): 
    return x + y + z == 2020

def calculateProduct(x, y, z):
    return x * y * z

def searchExpenses(expenses):
  #this helper from itertools allows you to loop through
  #every 3-length combination of items in expenses
  for x, y, z in itertools.combinations(expenses, 3):
    if sumsTo2020(x, y, z):
      return calculateProduct(x, y, z)

#print result
print(searchExpenses(expenses))