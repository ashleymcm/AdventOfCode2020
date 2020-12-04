import os, sys, re

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#get "passports" stored as two-new-line-separated strings in the text file
with open(os.path.join(dirname, "input.txt")) as passport_chunks:
  raw_passports = passport_chunks.read().split("\n\n")

#helper method to clean the passport from a spacey mess into a list of creds
def cleanPassport(raw_passport):
  cleaner_passport = raw_passport.split()
  cleanest_passport = []
  for cred in cleaner_passport:
    cleanest_passport.append(cred.split(':'))
  return cleanest_passport

#helper method to return all cred titles that exist on the given passport
def getPassportCreds(passport):
  credTitles = []
  for cred in passport:
    credTitles.append(cred[0]) 
  
  return credTitles

#helper method that returns True iff the creds in a passport contain all creds
#in the given list necessary_credentials, which is now part of how we determine validity
def passportContainsAllCreds(passport, necessary_credentials):
  creds = getPassportCreds(passport)
  return all(item in creds for item in necessary_credentials)

def isValidYear(year, minimum, maximum):
  if not year.isdigit():
    return False
  
  year = int(year)
  return year >= minimum and year <= maximum

def isValidBirthYear(year):
  return isValidYear(year, 1920, 2002)

def isValidIssueYear(year):
  return isValidYear(year, 2010, 2020)

def isValidExpirationYear(year):
  return isValidYear(year, 2020, 2030)

def isValidPassportId(pid):
  return len(pid) == 9 and pid.isdigit()

def isValidEyeColor(color):
  valid_colors = ["amb","blu","brn","gry","grn","hzl","oth"]
  return color in valid_colors

def isValidHairColour(color):
  return re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color)

def isValidHeight(height):
  unit = height[-2:]
  number = height[:-2]

  if not number.isdigit():
    return False
  
  number = int(number)

  if unit == "in":
    return number >= 59 and number <= 76
  elif unit == "cm":
    return number >= 150 and number <= 193
  else:
    return False

def passportIsValid(passport, necessary_credentials):
  #if it doesn't even contain all the necessary creds we can determine it's false right away
  if not passportContainsAllCreds(passport, necessary_credentials):
    return False

  #now check that each specific credential matches its validitity criteria, determined by the given problem
  #and represented by each of the helper methods above
  for cred in passport:
    if cred[0] == "byr":
      if not isValidBirthYear(cred[1]):
        return False
    elif cred[0] == "iyr":
      if not isValidIssueYear(cred[1]):
        return False
    elif cred[0] == "eyr":
      if not isValidExpirationYear(cred[1]):
        return False
    elif cred[0] == "hgt":
      if not isValidHeight(cred[1]):
        return False
    elif cred[0] == "hcl":
      if not isValidHairColour(cred[1]):
        return False
    elif cred[0] == "ecl":
      if not isValidEyeColor(cred[1]):
        return False
    elif cred[0] == "pid":
      if not isValidPassportId(cred[1]):
        return False

  return True

def countValidPassports(raw_passports, necessary_credentials):
  #clean up our passport data and set our count to 0 to initialize
  passports = [cleanPassport(passport) for passport in raw_passports]
  validCount = 0

  #loop through all passports and increment count iff a passport is valid
  for passport in passports:
    if passportIsValid(passport, necessary_credentials):
      validCount += 1

  return validCount

#these were given by the question, i just put them in an easy-to-see-and-use list
necessary_credentials = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
print(countValidPassports(raw_passports, necessary_credentials))