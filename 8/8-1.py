import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#get the "intructions" stored as a list from the input file
with open(os.path.join(dirname, "input.txt")) as intructions_rows:
  instructions = intructions_rows.read().splitlines()

#helper function to parse the input a little bit
def cleanInstruction(instruction):
  instruction = instruction.split()
  number = int(instruction[1][1:])
  if instruction[1][0] == '-':
    instruction[1] = 0 - number
  else:
    instruction[1] = number
  return instruction

#main function to run the code in "safe mode" aka terminate before an infinite loop
def runInSafeMode(instructions):
  #set up our variables that we'll use to keep track of it all
  accumulator = 0
  current_instruction = 0
  completed_instructions = []

  #loop through instructions according to the given problem UNTIL we encouter an index
  #we've already seen before
  while current_instruction not in completed_instructions:
    #add this index to the completed_instructions list so we mark that we've used it
    completed_instructions.append(current_instruction)

    #get the current instruction from the list and clean up the data with the helper
    instruction = instructions[current_instruction]
    instruction = cleanInstruction(instruction)

    #just for code clarity, mark that the action is at index 0 of the instruction and
    #the "number" is at index 1 - store them to use in our main logic below
    action = instruction[0]
    number = instruction[1]

    #if we encouter a jump command, go to the relative position given
    if action == "jmp":
      current_instruction += number
    #if we encounter an accumulate command, add the number to our counter
    #and then go to the next index in the list (current + 1)
    elif action == "acc":
      accumulator += number
      current_instruction += 1
    #if no operation just go to the next index in the list
    elif action == "nop":
      current_instruction += 1

  #if we've exited the loop, it means we've hit an instruction already seen before and would
  #have entered an infinite loop, so we return the accumulator now
  return accumulator

print(runInSafeMode(instructions))