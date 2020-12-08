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

def swapAction(action):
  if action == "jmp":
    return "nop"
  elif action == "nop":
    return "jmp"

#large helper function to run the code in "safe mode" aka terminate before an infinite loop but also change 
#one instruction to try to find + fix the broken one
def runWithAlteringOneInstruction(instructions, changed_instructions):
  #set up our variables that we'll use to keep track of it all
  accumulator = 0
  current_instruction = 0
  completed_instructions = []
  changeable_types = ["jmp", "nop"]
  instruction_changed = False

  #loop through instructions according to the given problem UNTIL we encouter an index
  #we've already seen before OR we terminate the proper way by reaching the last + 1 instruction
  while current_instruction not in completed_instructions and current_instruction != len(instructions):
    #add this index to the completed_instructions list so we mark that we've used it
    completed_instructions.append(current_instruction)

    #get the current instruction from the list and clean up the data with the helper
    instruction = instructions[current_instruction]
    instruction = cleanInstruction(instruction)

    #just for code clarity, mark that the action is at index 0 of the instruction and
    #the "number" is at index 1 - store them to use in our main logic below
    action = instruction[0]
    number = instruction[1]

    #added this block here to check that if an instruction hasn't already been changed in this run, and 
    #the current_instruction hasn't been changed in ANY run (and is a changeable type) we will swap it
    if not instruction_changed and current_instruction not in changed_instructions and action in changeable_types:
      action = swapAction(action)
      #append it to the array for potential future runs to use so they don't try to change the same one again
      changed_instructions.append(current_instruction)
      #mark instruction_changed as True so we don't try to change any instructions in this run again
      instruction_changed = True 

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

  #if we've exited the loop, it means we've hit an instruction already seen before and would have entered an infinite
  #loop, OR we've ended gracefully and have found the incorrect instruction. It's the NOT graceful ending if the index
  #isn't equal to the length (aka one after the list of instructions, as stated in the problem). In this case, we set 
  #accumulator to a negative value, or a "sentinal" for the main function to know it needs to keep searching. 
  if current_instruction != len(instructions):
    accumulator = -1

  #return both the new set of changed_instructions and the accumulator
  return changed_instructions, accumulator

def findRealAccumulator(instructions):
  changed_instructions = []
  accumulator = 0

  #run through the instructions until accumulator isn't zero (which we said above is a sentinal value used to denote
  #that we have not found/fixed the broken instruction). Every time we loop we are changing a different instruction,
  #since we know only ONE is broken.
  while True:
    changed_instructions, accumulator = runWithAlteringOneInstruction(instructions, changed_instructions)
    if accumulator >= 0:
      break
  
  #once accumulator is no longer less than zero we know we've fixed the correct code and can return the accumulator
  return accumulator

print(findRealAccumulator(instructions))