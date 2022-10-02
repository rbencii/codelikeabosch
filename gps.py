import csv
from turtle import up

class GpsObjects:
    def __init__(self, filePathLat = 'data/PSA_ADAS_W3_FC_2022-09-01_15-12_0059.MF4/Group_442.csv',filePathLong= 'data/PSA_ADAS_W3_FC_2022-09-01_15-12_0059.MF4/Group_443.csv',filePathHunterGPS='data/PSA_ADAS_W3_FC_2022-09-01_15-12_0059.MF4/Group_440.csv'):
        self.iterator = 1
        with open(filePathLat, 'rt') as f:
            reader = csv.reader(f)
            self.Latitude = list(reader)
        with open(filePathLong, 'rt') as f:
            reader = csv.reader(f)
            self.Longitude = list(reader)
        with open(filePathHunterGPS, 'rt') as f:
            reader = csv.reader(f)
            self.HunterGPS = list(reader)
        self.EndOfList = len(self.Latitude)<=self.iterator
        self.update()
    def update(self):
        self.iterator+=1
        self.EndOfList = len(self.HunterGPS)<=self.iterator
        if(self.EndOfList):
            return
        while(self.HunterGPS[self.iterator][1] != 8 or self.HunterGPS[self.iterator][1] != 9):
            self.iterator += 1
            self.EndOfList = len(self.HunterGPS)<=self.iterator
            if(self.EndOfList):
                return
        self.time = float(self.HunterGPS[self.iterator][0])
        self.Y = float(self.Latitude[self.iterator][1])
        self.YV = float(self.Latitude[self.iterator][2])
        self.X = float(self.Longitude[self.iterator][1])
        self.XV = float(self.Longitude[self.iterator][2])

        