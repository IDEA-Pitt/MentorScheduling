from Mentor import Mentor
from Hour import Hour #two objects to mixmatch
from Data import getData #Pulling data from the csv (downloaded from sheet)


DaysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
OpenHours = {}
for day in DaysOfTheWeek:
    OpenHours[day] = [Hour(x) for x in range(1, 12)]
    #Creats hours from 8-7 for each day
    #Will filter in the mentors for each day later

#getting the data from the downloaded excel sheet
mentors = getData()

#time to filter the mentors into the hours
#for each of the mentors. Now look through each day and hour to see if their available
for day in DaysOfTheWeek:
    for x in range(1, 12):
        #list comprehensions go crazy
        OpenHours[day][x] = [peep for peep in mentors if peep.available(day, x)]

"""
END OF PART ONE. NOW I'm going to start creating helper functions
"""

def sortHours():
    for day in DaysOfTheWeek:
        OpenHours[day].sort(key=lambda x: x.length()) #This should sort the hours in each day in order  
        #Since the contents of the dictionary are lists, and the lists are filled with objects
        #I can sort the object using class methods like length() show above

#I'm going to do the same thing for sortMentors() now too
def sortMentors(): 
    mentors.sort(key=lambda x:x.length())
    #mentors are stored in just the one list, so no fancy for loops

"""

before we get into recursion some quick notes
You should add classes through the google form as a class with LESS THAN 4 HOURS OF AVAILABILITY
IF THE Makerspace is going to be closed more than 4 hours because of a class, add another response

--- 

PART TWO
"""

