from Mentor import Mentor
from Hour import Hour #two objects to mixmatch
from Data import getData #Pulling data from the csv (downloaded from sheet)

#adding a timeout exception to my backtracking formula
import multiprocessing
import time

Schedule = {}
MentorsDone = []

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
#do I need to make this sort
def sortHours():
    for day in DaysOfTheWeek:
        OpenHours[day].sort(key=lambda x: x.length()) #This should sort the hours in each day in order  
        #Since the contents of the dictionary are lists, and the lists are filled with objects
        #I can sort the object using class methods like length() show above


#I'm going to do the same thing for sortMentors() now too
def sortMentors(grp): 
    grp.sort(key=lambda x:x.length())
    #mentors are stored in just the one list, so no fancy for loops

#since We're removing stuff from the Hours list, we need to store full hours in another list
def filter():
    #removes hours when they're full or unable to fill
    for day in DaysOfTheWeek:
        for hr in OpenHours[day]:
            #accounting for hrs already scheduled
            if(hr.length() - len(hr.current) < 3): #if there are less than three mentors 
                for peep in hr.current:
                    peep.unschedule(day, hr.time) #double check this here
                                                #Availablitity is a dict of ints not Hours                 
                OpenHours[day].remove(hr)

                break
            if(hr.full):
                Schedule[day] = hr
                OpenHours[day].remove(hr)
                break
    
    #filtering the mentors
    for peep in mentors:
        if(peep.length() - peep.scheduled < 4):
            raise Exception(peep.name + " is unable to be scheduled")
            
            """This should never happen (hopefully)
            if it does, rerunning may work?
            so the built in sort function is a quick sort, which is seeded for randomness
            normally this doesn't matter but if for cases when we have a tie for for length 
            of availability, rerunning it may switch who get's picked first
            
            However we make two assumptions, 
            that there is a possible schedule (which feels safe)
            and that you don't get unlucky when restarting
            where it keeps the order during the tie the same as the previous run
            """

        if(peep.full):
            mentors.remove(peep)
            MentorsDone.append(peep)
    
def isHoursEmpty():
    for day in DaysOfTheWeek:
        if(len(OpenHours[day]) != 0):
            return False
    #if all of the days are empty return true
    return True

def findHour():
    minHour = [OpenHours[day][0] for day in DaysOfTheWeek] # a list 
    return minHour.index(min(minHour)) #finds the index of the lest value
"""

before we get into recursion some quick notes
You should add classes through the google form as a class with LESS THAN 4 HOURS OF AVAILABILITY
IF THE Makerspace is going to be closed more than 4 hours because of a class, add another response

--- 

PART TWO
"""

def Scheduler():
    #Pre-logic functions
    filter()
    sortHours()
    sortMentors(mentors)
    #next chceck if either array is empty
    if(len(mentors) == 0 or isHoursEmpty()):
        if(len(mentors) == 0 and isHoursEmpty()):
            return True #each of 
        else:
            raise Exception("One list emptied before the other")
            # I really really hope this doesn't happen. But it definitely is
            #and idk how to deal with this, yet. Scheduling more hours than 4?
            #removing hours that don't fill up before the mentors do? discuss I will
            # I wrote how I think I should go from here on the whiteboard in the lab
    #LOGIC TIME
    VariableName = findHour()
    BigDay = DaysOfTheWeek[VariableName]
    #sorting the mentors inside the hour object
    sortMentors(OpenHours[BigDay][0].possibleMentors)
    #picking the mentor to schedule
    mtor = OpenHours[BigDay][0].possibleMentors[0]
    #scheduling the hour and the mentor
    mtor.schedule(BigDay, OpenHours[BigDay][0].time)
    OpenHours[BigDay][0].schedule(mtor)

    #recursion :(
    return Scheduler()

#going through and filling in each hour with 3 mentors, and each mentor with four hours
#moving this around that fill in the spots left by the scheduler function
def backtrack():
    
    

    #end of function
    if(len(mentors) == 0 and isHoursEmpty()):
        return True #each of 
    else:
        return backtrack()

"""Everyone's favorite part: Backtracking (ugh)"""
#work in progress
try:
    Scheduler()
except:
    #backtrack in here
    print("backtracking here")

    #I saw a cool way to use a function decorator but I wasn't sure how to implement it

    b = multiprocessing.Process(target=backtrack)
    b.join(30) #If the process is still alive after 30s
    if b.is_alive(): #if the backtracking process is still running after 30 seconds
        b.terminate()
        #b.kill() -> target was recursive so this may be better
        b.join() #brings all the processes back into this main function


