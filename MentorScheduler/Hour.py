from Mentor import Mentor
class Hour:
    def __init__(self, time, possible=[], final=[]):
        self.time = time
        self.possibleMentors = possible
        self.current = final #3 mentors per hour
    
    def length(self):
        return self.possibleMentors.length() #sees which hours need to be scheduled first
    
    def add(self, mentor):
        self.possibleMentors.append(mentor)
    
    def schedule(self, mentor):
        self.possibleMentors.remove(mentor)
        self.current.append(mentor)
    
    def full(self):
        return self.current == 3