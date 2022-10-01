import csv

class Ego:
    ANGLE_AZIMUTH_CORNER_RADAR_LEFT_FRONT = 42
    ANGLE_AZIMUTH_CORNER_RADAR_LEFT_REAR = 135
    ANGLE_AZIMUTH_CORNER_RADAR_RIGHT_FRONT = 42
    ANGLE_AZIMUTH_CORNER_RADAR_RIGHT_REAR = -135
    ANGLE_ELEVATION_CORNER_RADAR_LEFT_FRONT = 0
    ANGLE_ELEVATION_CORNER_RADAR_LEFT_REAR = 0,48
    ANGLE_ELEVATION_CORNER_RADAR_RIGHT_FRONT = 0
    ANGLE_ELEVATION_CORNER_RADAR_RIGHT_REAR = 0,48
    X_POSITION_CORNER_RADAR_LEFT_FRONT = 3473,8
    X_POSITION_CORNER_RADAR_LEFT_REAR = -766,4
    X_POSITION_CORNER_RADAR_RIGHT_FRONT = 3473,8 
    X_POSITION_CORNER_RADAR_RIGHT_REAR = -766,4
    Y_POSITION_CORNER_RADAR_LEFT_FRONT = 628,6
    Y_POSITION_CORNER_RADAR_LEFT_REAR = 738
    Y_POSITION_CORNER_RADAR_RIGHT_FRONT = -628,6
    Y_POSITION_CORNER_RADAR_RIGHT_REAR = -738
    Z_POSITION_CORNER_RADAR_LEFT_FRONT = 515,6
    Z_POSITION_CORNER_RADAR_LEFT_REAR = 735,9
    Z_POSITION_CORNER_RADAR_RIGHT_FRONT = 515,6
    Z_POSITION_CORNER_RADAR_RIGHT_REAR = 735,9

    """ def __init__(self, vxvRef, axvRef, vyvRef, ayvRef, psiDtOpt):
        self.vxvRef = vxvRef
        self.axvRef = axvRef
        self.vyvRef = vyvRef
        self.ayvRef = ayvRef
        self.psiDtOpt = psiDtOpt """
    
    def __init__(self, filePath):
        with open('data/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_416.csv', 'rt') as f:
           self.iterator = 0
           reader = csv.reader(f)
           self.database = list(reader)
           self.__update__()

    
    def __update__(self):
        self.iterator += 1;
        row = self.database[self.iterator]
        self.T = row[0]
        self.axvRef = row[1]
        self.ayvRef = row[2]
        self.psiDtOpt = row[3]
        self.tAbsRefTime = row[4]
        self.vxvRef = row[5]
        self.vyvRef = row[6]

    def printCurrent(self):
        print("iterator: " + str(self.iterator))
        print("T: " + self.T)
        print("axvRef: " + self.axvRef)
        print("ayvRef: " + self.ayvRef)
        print("psiDtOpt: " + self.psiDtOpt)
        print("tAbsRefTime: " + self.tAbsRefTime)
        print("vxvRef: " + self.vxvRef)
        print("vyvRef: " + self.vyvRef)
        
                
"""
#sample

x = Ego(None)
x.printCurrent()
x.__update__()
print()
x.printCurrent() 

#"""
