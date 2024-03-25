class Hour:
    def __init__(self, possible, final):
        self.possibleMentors = possible
        self.current = 0 #3 mentors per hour
    
    def length(self):
        return self.possibleMentors.length() #sees which hours need to be scheduled first
    