from Mentor import Mentor
class Hour:
    def __init__(self, time, possible=[], final=0):
        self.time = time
        self.possibleMentors = possible
        self.current = final #3 mentors per hour
    
    def length(self):
        return self.possibleMentors.length() #sees which hours need to be scheduled first
    
    def add(self, mentor):
        self.possibleMentors.append(mentor)