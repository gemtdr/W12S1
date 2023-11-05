class Time:

    def __init__(self, seconds = 0):
        
        self.hours = 0
        self.minutes = 0
        self.seconds = seconds

    def addTimes(self,rhs):
        
        addedTime = Time()
        addedTime.hours = self.hours + rhs.hours
        addedTime.minutes = self.minutes + rhs.minutes
        addedTime.seconds = self.seconds + rhs.seconds

        return addedTime

    def subtractTimes(self,rhs):

        subtractedTime = Time()
        subtractedTime.hours = self.hours - rhs.hours
        subtractedTime.minutes = self.minutes - rhs.minutes
        subtractedTime.seconds = self.seconds - rhs.seconds

    def clearTime(self):

        self.hours = 0
        self.minutes = 0
        self.seconds = 0


    def printTime(self):

        print(f'Hours: {self.hours}, Minutes: {self.minutes}, Seconds: {self.seconds}')






if __name__ == "__main__":

    time1 = Time()
    time1.hours = 7
    time1.minutes = 15

    time2 = Time(3)
    time2.hours = 5
    time2.minutes = 2

    

    

    
