import random

print ("------------------------------------\nProblem 1:\n\n")

yr = random.randint(1800,2200)
mth = random.randint(1,12)

# Problem 1:
# A leap year can be calculated using the following algorithm
# that takes as input a year as an integer, suppose we have variable called
# yr, then yr is a leap year if:
#
#   - yr can be evenly divided by 4, or
#   - yr cannot be evenly divided by 100, or
#   - yr is evenly divided by 100, and is also
#   - evenly divisible by 400.
#
# Given variables yr and mth for the year and the month, print to the screen
# the number of days in that month in the format:
#
#    In year yr, mth has n days.
#
# where n is the number of days.

##if mth == 1:
##    print ("In year "+str(yr)+", "+str(mth)+" has 31 days.")
##elif mth == 2:
##    ?
##elif mth == 3:
##    print ("In year "+str(yr)+", "+str(mth)+" has 31 days.")
##elif mth == 4:
##    print ("In year "+str(yr)+", "+str(mth)+" has 30 days.")
##elif mth == 5:
##    print ("In year "+str(yr)+", "+str(mth)+" has 31 days.")
##elif mth == 6:
##    print ("In year "+str(yr)+", "+str(mth)+" has 30 days.")
##elif mth == 7:
##    print ("In year "+str(yr)+", "+str(mth)+" has 31 days.")
##elif mth == 8:
##    print ("In year "+str(yr)+", "+str(mth)+" has 31 days.")
##elif mth == 9:
##    print ("In year "+str(yr)+", "+str(mth)+" has 30 days.")
##elif mth == 10:
##    print ("In year "+str(yr)+", "+str(mth)+" has 31 days.")
##elif mth == 11:
##    print ("In year "+str(yr)+", "+str(mth)+" has 30 days.")
##elif mth == 12:
##    print ("In year "+str(yr)+", "+str(mth)+" has 31 days.")
##
##if mth == 2: # leap year
##    if yr % 4 == 0:
##        # leap year!
##        print ("In year "+str(yr)+", "+str(mth)+" has 29 days.")
##    else:
##        if yr % 100 != 0:
##            # leap year!
##            print ("In year "+str(yr)+", "+str(mth)+" has 29 days.")
##        else:
##            if yr % 400 == 0:
##                # leap year!
##                print ("In year "+str(yr)+", "+str(mth)+" has 29 days.")
##            else:
##                # not a lear year :-(
##                print ("In year "+str(yr)+", "+str(mth)+" has 28 days.")
##elif mth == 4 or mth == 6 or mth == 9 or mth == 11: # 30 days
##    print ("In year "+str(yr)+", "+str(mth)+" has 30 days.")
##else: # 31 days
##    print ("In year "+str(yr)+", "+str(mth)+" has 31 days.")
##
### Wrong simplification, simplified the else to the outside!!
##if (mth == 2 and yr % 4 == 0) or (yr % 100 != 0 or yr % 400 == 0):# leap year
##    print ("In year "+str(yr)+", "+str(mth)+" has 29 days.")
##else: # not a lear year :-(
##    print ("In year "+str(yr)+", "+str(mth)+" has 28 days.")
##elif mth == 4 or mth == 6 or mth == 9 or mth == 11: # 30 days
##    print ("In year "+str(yr)+", "+str(mth)+" has 30 days.")
##else: # 31 days
##    print ("In year "+str(yr)+", "+str(mth)+" has 31 days.")


if mth == 2: # leap year
    if (yr % 4 == 0 or yr % 100 != 0) or (yr % 100 == 0 and yr % 400 == 0):
        # leap year!
        print ("In year "+str(yr)+", "+str(mth)+" has 29 days.")
    else:        
        # not a lear year :-(
        print ("In year "+str(yr)+", "+str(mth)+" has 28 days.")
elif mth == 4 or mth == 6 or mth == 9 or mth == 11: # 30 days
    print ("In year "+str(yr)+", "+str(mth)+" has 30 days.")
else: # 31 days
    print ("In year "+str(yr)+", "+str(mth)+" has 31 days.")
    
print ("------------------------------------\nProblem 2:\n\n")

is_neutered = random.choice([True, False])
is_dog = random.choice([True, False])
weight = random.randint(1,150)

# Problem 2:
#
# Give the following facts about your pet:
#    - Are they neutered?
#    - Is your pet a dog?
#    - What is the weight of your pet?
# Then we can calculate the caloric needs of your pet.
#
# First, their weight must be convererd into KG by dividing their
# weight by 2.2, and calculating their rest-energy requirement (RER)
# by raising their weight in KG to the power of 3/4 and multiplying that by
# 70.  Then:
#     - if your pet is a dog and neutered, then their caloric needs is 1.6
#       times their RER, but if they are not neutered, then it's 1.8 times
#       their RER.
#
#     - if your pet is not a dog and neutered, then their caloric needs is 1.2
#       times their RER, but if they are not neutered, then it's 1.4 times
#       their RER.
#
# Write a program that calculates the calroic needs of a pet given variables:
#    is_neutered, is_dog, weight.

print("Dog: "+str(is_dog))
print("Neutered: "+str(is_neutered))
print("Weight: "+str(weight))

weight_kg = weight / 2.2
pet_rer = 70 * (weight_kg ** 0.75)

if is_dog and is_neutered:
    print ("Calorie needs: "+str(1.6 * pet_rer))
elif is_dog and not is_neutered:
    print ("Calorie needs: "+str(1.8 * pet_rer))
elif not is_dog and is_neutered:
    print ("Calorie needs: "+str(1.2 * pet_rer))
else:
    print ("Calorie needs: "+str(1.4 * pet_rer))

if is_dog:
    if is_neutered:
        print ("Calorie needs: "+str(1.6 * pet_rer))
    else:
      print ("Calorie needs: "+str(1.8 * pet_rer))
else:
    if is_neutered:
        print ("Calorie needs: "+str(1.2 * pet_rer))
    else:
        print ("Calorie needs: "+str(1.4 * pet_rer))

