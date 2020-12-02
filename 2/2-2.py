import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "password arrays"
with open(os.path.join(dirname, "input.txt")) as password_array_list:
  password_arrays = [password_arrays.split() for password_arrays in password_array_list]

def isValid(password_array): 
  #parse out min and max from array
  minMax = password_array[0].split('-')
  index1 = int(minMax[0]) - 1     #subtracting one from these indices for parity 
  index2 = int(minMax[1]) - 1     #between elf vs regular indexing standards

  #parse out the character we're looking for
  character = password_array[1].replace(':', '')

  #store the password in its own var for clarity
  password = password_array[2]
  
  #used the XOR operator here which means we return true if the character is at index1 in 
  #password or if the character is at index2 in password, but not if it is at both
  return bool(password[index1] == character) ^ bool(password[index2] == character)                               
  
def calculateNumValidPasswords(password_arrays):
  count = 0
  for password_array in password_arrays:
    if isValid(password_array):
      count += 1
  return count

#print result
print(calculateNumValidPasswords(password_arrays))