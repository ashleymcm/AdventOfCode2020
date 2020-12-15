import os, sys
from sympy.ntheory.modular import crt

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

#loop through input rows, or "input_data"
with open(os.path.join(dirname, "input.txt")) as input_data:
  input_data = input_data.read().split("\n")

#second line is bus routes/schedules, which question says is all that matters this time
routes = input_data[1].split(',')
schedule = []

#loop through routes and store as an array of arrays with first item being route number 
#and second being offset to timestamp
for index, route in enumerate(routes):
  if route != 'x':
    schedule.append([int(route), index])

# Now, this was kind of annoying, especially since I was trying to do it while sick and 
# wasn't 100% sure how I wanted to progress. I noticed the pattern of the timestamps and
# was able to write it out as a group of equations (using sample):

#     (timestamp + 0) % 7 == 0
#     (timestamp + 1) % 13 == 0
#     (timestamp + 4) % 59 == 0
#     (timestamp + 6) % 31 == 0
#     (timestamp + 7) % 19 == 0

# I kind of wracked my brain on how to solve this, similar to how one might solve a system of
# linear etc. equations but it just didn't come to me. Also, despite taking both combinatorics 
# number theory (back in the day), I couldn't remember ever seeing how to solve this mathematically.

# So, I turned to Google, and saw a bunch of stuff about this wild Chinese Remainder Theorem (this
# was the first site that got me on my way: https://www.dave4math.com/mathematics/chinese-remainder-theorem/ 
# so thanks!)

# I realized that I could probably solve it by looping as well if I could just get the iteration number
# down enough, but I wasn't having much fun trying to solve it with loops and my brain was simply NOT in the 
# mood to refine increments for iterating. Plus, I was kind of hooked on reading about this CRT, so I 
# decided to keep it fun, learn about that, and then call it a day. 

# I'm not going to explain the CRT in this
# code because other people do it way better, but I HAVE tried to make my code readable for beginners (hence
# all the comments) so it really does bum me out that this one has more "magic" than algorithms. I still hope
# to be able to refactor and optimize all this at a later date, so hey, maybe that'll happen. A girl can dream.

#the first item of each route in the schedule contains the bus #, or the modulus - i.e. how often the bus repeats
moduli = [route[0] for route in schedule]

#the second item has the offset but we need the remainder, so we subtract the offset from the bus # 
remainders = [route[0] - route[1] for route in schedule]

#now we perform the Chinese Number Theorem, which takes in the moduli and the remainders. I used sympy's helper 
#for this because recreating the algorithm wasn't super fun, but maybe that was just my sick brain and if so
#I'll prob add my own implementation later
timestamp = crt(moduli, remainders)[0]

print(timestamp)


