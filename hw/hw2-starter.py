import math
import csv
from collections import Counter

ATHLETES_FILE = 'hw2-athletes.csv'


#########################################
#  PART ONE: LOAD DATA
#########################################

def get_user_athlete():
    """
    Prompts user for an age, height, and weight.
    """
    athlete = {}

    try:
        athlete['age'] = int(input("Age (years)? "))
        athlete['height'] = int(input("Height (cm)? "))
        athlete['weight'] = int(input("Weight (kg)? "))
        athlete['sport'] = input("Actual Sport (or leave blank)?")
    except:
        print('Invalid age/height/weight entered!')

    return athlete


def load_athlete_data(filename):
    """
    Loads athlete data from 'filename' into a list of rows.

    Each row contains an athlete's attributes, where
      the last element is a list of events the athlete
      competed in.

    The header line is skipped, and rows are removed
      if missing a value for the age, height, or weight.

    For example:
    [...,
     {'name': 'Svitlana Cherniavska', 'event': ["Women's +75kg"], 'weight': 103, ...},
     ...
    ]
    """
    assert(type(filename) is str)
    assert(len(filename) > 0)

    athletes = []

    return athletes


#########################################
#  PART TWO: NEAREST NEIGHBORS
#########################################


def dist(x, y):
    """
    Euclidean distance between vectors x and y.
    Each element of x and y must be numeric or a numeric string.

    Requires that len(x) == len(y).

    For example:
        dist((0, 0), (0, 5)) == 5.0
        dist((1, 1, 1), (2, 2, 2)) == 1.7320508075688772
        dist(('1', '1', '1'), ('2', '2', '2')) == 1.7320508075688772
    """

    assert(len(x) == len(y))

    return 0.0


def nearest_athletes(athlete, athletes, k = 1):
    """
    Returns the 'k' 'athletes' closest to 'athlete'.
    Sorts the athletes based on distance to 'point', then return the closest.
    """
    assert(type(athletes) is list)

    return []


def most_common_sport(athletes):
    """
    Returns a string of the most frequently occuring sport in the 'athletes'.
        Consider using Counter.
    """

    return ''



#########################################
# PART III: CROSS VALIDATION
#########################################

def cross_validate(athletes, k = 20):
    """
    Uses each athlete as a test point and sees whether k-NN correctly predicts
      the athlete's sport.

    Finds each athlete's nearest neighbors, then tests if the predicted k-NN sport
      matches the athlete's sport. This is an objective measure of
      classifier performance called 'leave-one-out cross-validation'.

    Returns the accuracy: num_correct / (num_incorrect + num_correct)
    """

    num_correct = 0
    num_incorrect = 1       # Only to avoid division-by-zero -- should be 0!

    for index, athlete in enumerate(athletes):

        #######
        ## Cross-validation code here!
        #######

        # Display progress so far every 500 athletes
        if index % 500 == 0:
            print("{} of {}, accuracy so far={}".format(
                index, len(athletes),
                num_correct / (num_correct + num_incorrect)))

    return num_correct / (num_correct + num_incorrect)



#########################################
# APP ENTRY POINT
#########################################


####################
# LOAD DATA
####################

athletes = load_athlete_data(ATHLETES_FILE)

#  Jurgen Spiess, Weightlifting
test_athlete = {'age': 28, 'height': 174, 'weight': 105, 'sport': 'Weightlifting'}

# test_athlete = get_user_athlete()          # Uncomment for user input


####################
# NEAREST NEIGHBORS
####################


# Get the k nearest athletes to the test_athlete
test_nearest = nearest_athletes(test_athlete, athletes, k=2)
if len(test_nearest) > 1:
    print('NEAREST (does this match?): ', test_nearest[0])
    print('SECOND NEAREST (do age/ht/wt look close?): ', test_nearest[1], "\n")


# Find the most common sport of the nearest athletes
recommended_sport = most_common_sport(test_nearest)
actual_sport = test_athlete['sport']
print("RECOMMENDED SPORT: ", recommended_sport)
print("ACTUAL SPORT OF TEST ATHLETE: ", actual_sport, "\n")

####################
# CROSS-VALIDATION
####################
print("PERFORMING CROSS-VALIDATION ...")

# What is the accuracy of the k-nearest neighbors classifier?
accuracy = cross_validate(athletes, k=1)

print("FINAL ACCURACY: ", accuracy)
