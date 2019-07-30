# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 7, exercise 2

# creating empty list of best scores

import pickle

# number of scores to save on list
MAX_SCORES = 3

print("Creating empty list of best scores. \n")
print("WARNING - THIS WILL RESET ALL SCORES! ")
answer = input("Do you want to continue? [Y/NO]: ")

if answer.lower() in ('y', 'yes'):
    file = open("exercise 2 top_scores.dat", "wb")
    score = (0, ".....")
    scores = []
    for i in range(MAX_SCORES):
        scores.append(score)
    pickle.dump(scores, file)
    file.close()
    print("Empty scores seted. ")

input("\nPress ENTER to exit. ")
