import os, sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#get "passports" stored as two-new-line-separated strings in the text file
with open(os.path.join(dirname, "input.txt")) as passport_chunks:
  raw_passports = passport_chunks.read().split("\n\n")

#helper method to clean the passport from a spacey mess into a list of creds
def cleanPassport(raw_passport):
  return raw_passport.split()

#helper method to return all cred titles that exist on the given passport
def getPassportCreds(passport):
  credTitles = []
  for cred in passport:
    credTitles.append(cred.split(':')[0]) 
  
  return credTitles

#helper method that returns True iff the creds in a passport contain all creds
#in the given list necessary_credentials, which is how we determine validity
def passportContainsAllCreds(passport, necessary_credentials):
  creds = getPassportCreds(passport)
  return all(item in creds for item in necessary_credentials)

def countValidPassports(raw_passports, necessary_credentials):
  #clean up our passport data and set our count to 0 to initialize
  passports = [cleanPassport(passport) for passport in raw_passports]
  validCount = 0

  #loop through all passports and increment count iff a passport is valid
  for passport in passports:
    if passportContainsAllCreds(passport, necessary_credentials):
      validCount += 1

  return validCount

#these were given by the question, i just put them in an easy-to-see-and-use list
necessary_credentials = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
print(countValidPassports(raw_passports, necessary_credentials))