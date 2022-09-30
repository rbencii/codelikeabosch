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
        with open('PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_416.csv', 'rt') as f:
           reader = csv.reader(f)
           self.database = list(reader)
           self.T = {}
           self.vxvRef = {}
           self.axvRef = 1
           self.vyvRef = {}
           self.ayvRef = {}
           self.psiDtOpt = {}
        for i in range(2,len(self.database[0])):
            sor = self.database[0][i].split('.')
            match sor[7]:
                case "m_camData":
                    match sor[-1]:
                        case "_m_dx":
                            self.cameraPersonas[sor[-2]]["xIndex"] = i
                        case "_m_dy":
                            self.cameraPersonas[sor[-2]]["yIndex"] = i
                        case "_m_vx":
                            self.cameraPersonas[sor[-2]]["vxIndex"] = i
                        case "_m_vy":
                            self.cameraPersonas[sor[-2]]["vyIndex"] = i
                        case "_m_ax":
                            self.cameraPersonas[sor[-2]]["axIndex"] = i
                        case "_m_az":
                            self.cameraPersonas[sor[-2]]["azIndex"] = i
                