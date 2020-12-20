import os, sys, re

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

  num_1 = nums[0]
  for i in range(1, len(nums)):
    num_2 = nums[i]
    op = ops[i - 1]

    if op == '+':
      num_1 = num_1 + num_2
    elif op == '*':
      num_1 = num_1 * num_2
  
  return num_1


total_sum = 0
for problem in problems:
  total_sum += solveProblem(problem)

print(total_sum)

  




  

