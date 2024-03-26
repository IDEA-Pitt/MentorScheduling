class Mentor:
    def __init__(self, nm, availability):
        self.name = nm
        self.hours = {}
        self.availability = availability
        self.scheduled = 0
        """
        { "Monday" : [9, 10, 14, 15, 16], 
          "Tuesday": [12, 13, 18, 19], 
          ...
        }
        """

    def length(self):
        possible = 0
        for day in self.availability:#to see who is most available
            possible += len(self.availability[day])

    def available(self, day, hour):
        if(hour in self.availability[day]):
            return True
        else: 
            return False

    def add(self, day, hour):
        self.hours[day] = hour