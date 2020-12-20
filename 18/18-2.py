import os, sys, re, math

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "problem_list"
with open(os.path.join(dirname, "input.txt")) as problem_list:
  problems = problem_list.read().split("\n")

def solveProblem(problem):
  problem = problem.replace(' ', '')

  #loop to get rid of those pesky parentheses
  while '(' in problem:
    i_start = problem.rfind('(')
    i_end = problem.find(')', i_start)
    number = doArithmetic(problem[i_start + 1:i_end])
    problem = problem[:i_start] + str(number) + problem[i_end + 1:]
  
  #should be no parentheses anymore
  return doArithmetic(problem)

def doArithmetic(arithmetic):
  #do arithmetic as long as there are no parentheses
  nums = re.split(r'\D+', arithmetic)
  nums = list(map(int, nums))
  ops = [i for i in arithmetic if not i.isdigit()]
  
  #loop through nums and ops and perform additions 
  i = 0
  while i < len(nums) - 1:
    if ops[i] == '+':
      num = nums[i] + nums[i + 1]
      nums[i] = num   #replace the first number with the new sum
      nums.pop(i + 1) #pop off the second number as its no longer needed
      ops.pop(i)      #remove the op as well because we've already used it
      i -= 1          #adjust the index to reflect that we just removed an item
    i += 1

  #all that remain are multiplications so just return the product
  return math.prod(nums)


total_sum = 0
for problem in problems:
  total_sum += solveProblem(problem)

print(total_sum)

  




  

