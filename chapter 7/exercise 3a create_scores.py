# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 7, exercise 2

# creating empty list of best scores

# number of scores to save on list
MAX_SCORES = 3

print("Creating empty list of best scores. \n")
print("WARNING - THIS WILL RESET ALL SCORES! ")
answer = input("Do you want to continue? [Y/NO]: ")

if answer.lower() in ('y', 'yes'):
    file = open("exercise 3 top_scores.txt", "w")
    scores = []
    for i in range(MAX_SCORES):
        scores.append("0\n.....\n")
    file.writelines(scores)
    file.close()
    print("Empty scores seted. ")

input("\nPress ENTER to exit. ")
