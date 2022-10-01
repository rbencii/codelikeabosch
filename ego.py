import csv
import math
from normalize import normalize

class Ego:
    ANGLE_AZIMUTH_CORNER_RADAR_LEFT_FRONT = 42
    ANGLE_AZIMUTH_CORNER_RADAR_LEFT_REAR = 135
    ANGLE_AZIMUTH_CORNER_RADAR_RIGHT_FRONT = -42
    ANGLE_AZIMUTH_CORNER_RADAR_RIGHT_REAR = -135
    ANGLE_ELEVATION_CORNER_RADAR_LEFT_FRONT = 0
    ANGLE_ELEVATION_CORNER_RADAR_LEFT_REAR = 0.48
    ANGLE_ELEVATION_CORNER_RADAR_RIGHT_FRONT = 0
    ANGLE_ELEVATION_CORNER_RADAR_RIGHT_REAR = 0.48
    X_POSITION_CORNER_RADAR_LEFT_FRONT = 3473.8
    X_POSITION_CORNER_RADAR_LEFT_REAR = -766.4
    X_POSITION_CORNER_RADAR_RIGHT_FRONT = 3473.8 
    X_POSITION_CORNER_RADAR_RIGHT_REAR = -766.4
    Y_POSITION_CORNER_RADAR_LEFT_FRONT = 628.6
    Y_POSITION_CORNER_RADAR_LEFT_REAR = 738
    Y_POSITION_CORNER_RADAR_RIGHT_FRONT = -628.6
    Y_POSITION_CORNER_RADAR_RIGHT_REAR = -738
    Z_POSITION_CORNER_RADAR_LEFT_FRONT = 515.6
    Z_POSITION_CORNER_RADAR_LEFT_REAR = 735.9
    Z_POSITION_CORNER_RADAR_RIGHT_FRONT = 515.6
    Z_POSITION_CORNER_RADAR_RIGHT_REAR = 735.9

    """ def __init__(self, vxvRef, axvRef, vyvRef, ayvRef, psiDtOpt):
        self.vxvRef = vxvRef
        self.axvRef = axvRef
        self.vyvRef = vyvRef
        self.ayvRef = ayvRef
        self.psiDtOpt = psiDtOpt """
    
    def __init__(self, filePath = 'data/PSA_ADAS_W3_FC_2022-09-01_15-12_0059.MF4/Group_416.csv'):
        with open(filePath, 'rt') as f:
           self.iterator = 1
           reader = csv.reader(f)
           self.database = list(reader)
           self.EndOfList = len(self.database)<=self.iterator
           self.__update__()

    
    def __update__(self,limitMargin = 0.2):
        if(self.EndOfList):
            return
        self.EndOfList = len(self.database)<=self.iterator
        if(self.EndOfList):
            return
        row = self.database[self.iterator]
        self.T = row[0]

        limit=math.floor(float(self.T))+limitMargin
        found = False
        while math.floor(float(self.T))<limit and not found:
            self.iterator+=1
            self.EndOfList = len(self.database)<=self.iterator
            if(self.EndOfList):
                self.T = self.database[self.iterator-1][0]
            self.T = self.database[self.iterator][0]
            if(math.floor(float(self.T))>=limit):
                found = True
                if(limit - float(self.database[self.iterator-1][0]) < float(self.database[self.iterator][0]) - limit):
                    self.iterator-=1
                    self.T = self.database[self.iterator][0]
        row = self.database[self.iterator]
        self.axvRef = normalize("acceleration", row[1])
        self.ayvRef = normalize("acceleration", row[2])
        self.psiDtOpt = normalize("yaw", row[3])
        self.tAbsRefTime = row[4]
        self.vxvRef = normalize("velocity", row[5])
        self.vyvRef = normalize("velocity", row[6])

    def printCurrent(self):
        print("iterator: " + str(self.iterator))
        print("T: " + self.T)
        print("axvRef: " + str(self.axvRef))
        print("ayvRef: " + str(self.ayvRef))
        print("psiDtOpt: " + str(self.psiDtOpt))
        print("tAbsRefTime: " + str(self.tAbsRefTime))
        print("vxvRef: " + str(self.vxvRef))
        print("vyvRef: " + str(self.vyvRef))
        
                
#"""
#sample

"""x = Ego()
x.printCurrent()
x.__update__()
print()
x.printCurrent() """

#"""
