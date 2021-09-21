import csv
from os import read
f = open('GPS.csv','r')
reader = csv.reader(f)
people = {}

class Tracker:
    def __init__(self,username,Date):
        self.username = username
        self.Date = Date
    
    def find(self):
        for row in reader:
            people[row[0]] = {'Latitude':row[1],'Longitude':row[2],'Date':row[3],'Time':row[4],}
        
            if row[0] == self.username and row[3] == self.Date:
                print('Name: '+row[0], 'Latitude: '+row[1] ,"Longitude: "+row[2],"Time: "+row[4])

            

    @classmethod
    def get_user_input(self):
        print("""
        *****Welcome To Our Tracking Application!*****  
        """)
        while True:
            try:
                username = input("Enter Username:")
                Date = input("Enter Date:")
                return self(username,Date)

            
            except:
                 print('Invalid input!')
                 continue

                
    

User = Tracker.get_user_input()
User.find()

    









