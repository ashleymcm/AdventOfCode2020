import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "password arrays"
with open(os.path.join(dirname, "input.txt")) as password_array_list:
  password_arrays = [password_arrays.split() for password_arrays in password_array_list]

def isValid(password_array): 
  #parse out min and max from array
  minMax = password_array[0].split('-')
  minimum = int(minMax[0])
  maximum = int(minMax[1])

  #parse out the character we're looking for
  character = password_array[1].replace(':', '')

  #store the password in its own var for clarity
  password = password_array[2]

  #count the number of instances of character in password
  count = password.count(character)

  #return bool for if the count is in range
  return count >= minimum and count <= maximum
  
def calculateNumValidPasswords(password_arrays):
  count = 0
  for password_array in password_arrays:
    if isValid(password_array):
      count += 1
  return count

#print result
print(calculateNumValidPasswords(password_arrays))