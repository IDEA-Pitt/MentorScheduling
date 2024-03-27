from Mentor import Mentor
from Hour import Hour #two objects to mixmatch
from Data import getData #funciton


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
        



print(len(mentors))
