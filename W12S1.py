class Time:

    def __init__(self): #make a default parameter called seconds and set it to 0
        
        self.hours = 0
        self.minutes = 0

    def addTimes(self,rhs): #Update this function to include seconds
        
        addedTime = Time()
        addedTime.hours = self.hours + rhs.hours
        addedTime.minutes = self.minutes + rhs.minutes
     

        return addedTime

    def subtractTimes(self,rhs): #Use the logic from addTimes to complete this function

        pass
    

    def clearTime(self): #Set hours, minutes and seconds to 0

        pass
    


    def printTime(self): #update to include seconds

        print(f'Hours: {self.hours}, Minutes: {self.minutes}')






if __name__ == "__main__": #Play with the instances below to test each of your functions

    time1 = Time()
    time1.hours = 7
    time1.minutes = 15

    time2 = Time()
    time2.hours = 5
    time2.minutes = 2

    

    

    
