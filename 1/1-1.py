import os, sys, itertools

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "expenses"
with open(os.path.join(dirname, "input.txt")) as expenses_list:
  expenses = [int(expenses) for expenses in expenses_list]

def sumsTo2020(x, y): 
    return x + y == 2020

def calculateProduct(x, y):
    return x * y

def searchExpenses(expenses):
  #this helper from itertools allows you to loop through
  #every 2-length combination of items in expenses
  for x, y in itertools.combinations(expenses, 2):
    if sumsTo2020(x, y):
      return calculateProduct(x, y)

#print result
print(searchExpenses(expenses))