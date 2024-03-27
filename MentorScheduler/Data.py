from Mentor import Mentor
import csv #i'm just downloading the csv of the response once it's done


def getData(filename='data.csv'):
    Mentors = []
    Hours = ["What hours are you available? [Monday]", "What hours are you available? [Tuesday]", "What hours are you available? [Wednesday]", "What hours are you available? [Thursday]", "What hours are you available? [Friday]"]

    file = open(filename, 'r', newline='')
    reader = csv.DictReader(file)

    for row in reader:
        Available = {key: row[key] for key in Hours}
        DayDict = {}
        #converting this string into useable data
        #i could use a regex here, idk how to make a search key. 
        #wouldn't save too much time I think. Plus this is a bit nicer
        for day in Available:
            daily = []
            space = Available[day].find(" ")
            daily.append(int(Available[day][0:space]))
            while space != -1:
                comma = Available[day].find(",", space + 1)
                space = Available[day].find(" - ", space + 1)
                sbstr = Available[day][comma + 1:space]
                if(len(sbstr) < 4):
                    daily.append(int(sbstr))

            #print(daily)
            DayDict[day[day.find("[")+1:len(day)-1]] = daily
        
        print(DayDict)

        temp = Mentor(row["WHAT IS YOUR NAME?"], DayDict)
        Mentors.append(temp)

    file.close()
    return Mentors

