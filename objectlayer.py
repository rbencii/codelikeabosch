
import csv

class Objects:
    def __init__(self,filePath = 'data/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_349.csv'):
        with open(filePath, 'rt') as f:
           reader = csv.reader(f)
           self.database = list(reader)

           self.cameraPersonas = {}
           self.leftRearRadarPersonas = {}
           self.leftFrontRadarPersonas = {}
           self.rightRearRadarPersonas = {}
           self.rightFrontRadarPersonas = {}
        self.databaseLinePivot = 1
        self.cameraPosX = self.database[1][-3]
        self.cameraPosY = self.database[1][-2]
        self.cameraPosZ = self.database[1][-1]
        for i in range(2,len(self.database[0])-3,1):
            sor = self.database[0][i].split('.')
            match sor[7]:
                case "m_camData":
                    try:
                        self.cameraPersonas[sor[-2]]
                    except KeyError:
                        self.cameraPersonas[sor[-2]] = {}
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
                case "_m_cornerData":
                    match sor[-5]:
                        case "_0_":
                            try:
                                self.leftFrontRadarPersonas[sor[-2]]
                            except KeyError:
                                self.leftFrontRadarPersonas[sor[-2]] = {}
                            match sor[-1]:
                                case "_m_dx":
                                    self.leftFrontRadarPersonas[sor[-2]]["xIndex"] = i
                                case "_m_dy":
                                    self.leftFrontRadarPersonas[sor[-2]]["yIndex"] = i
                                case "_m_vx":
                                    self.leftFrontRadarPersonas[sor[-2]]["vxIndex"] = i
                                case "_m_vy":
                                    self.leftFrontRadarPersonas[sor[-2]]["vyIndex"] = i
                                case "_m_ax":
                                    self.leftFrontRadarPersonas[sor[-2]]["axIndex"] = i
                                case "_m_az":
                                    self.leftFrontRadarPersonas[sor[-2]]["azIndex"] = i    
                        case "_1_":
                            try:
                                self.leftRearRadarPersonas[sor[-2]]
                            except KeyError:
                                self.leftRearRadarPersonas[sor[-2]] = {}
                            match sor[-1]:
                                case "_m_dx":
                                    self.leftRearRadarPersonas[sor[-2]]["xIndex"] = i
                                case "_m_dy":
                                    self.leftRearRadarPersonas[sor[-2]]["yIndex"] = i
                                case "_m_vx":
                                    self.leftRearRadarPersonas[sor[-2]]["vxIndex"] = i
                                case "_m_vy":
                                    self.leftRearRadarPersonas[sor[-2]]["vyIndex"] = i
                                case "_m_ax":
                                    self.leftRearRadarPersonas[sor[-2]]["axIndex"] = i
                                case "_m_az":
                                    self.leftRearRadarPersonas[sor[-2]]["azIndex"] = i
                        case "_2_":
                            try:
                                self.rightFrontRadarPersonas[sor[-2]]
                            except KeyError:
                                self.rightFrontRadarPersonas[sor[-2]] = {} 
                            match sor[-1]:
                                case "_m_dx":
                                    self.rightFrontRadarPersonas[sor[-2]]["xIndex"] = i
                                case "_m_dy":
                                    self.rightFrontRadarPersonas[sor[-2]]["yIndex"] = i
                                case "_m_vx":
                                    self.rightFrontRadarPersonas[sor[-2]]["vxIndex"] = i
                                case "_m_vy":
                                    self.rightFrontRadarPersonas[sor[-2]]["vyIndex"] = i
                                case "_m_ax":
                                    self.rightFrontRadarPersonas[sor[-2]]["axIndex"] = i
                                case "_m_az":
                                    self.rightFrontRadarPersonas[sor[-2]]["azIndex"] = i
                        case "_3_":
                            try:
                                self.rightRearRadarPersonas[sor[-2]]
                            except KeyError:
                                self.rightRearRadarPersonas[sor[-2]] = {}
                            match sor[-1]:
                                case "_m_dx":
                                    self.rightRearRadarPersonas[sor[-2]]["xIndex"] = i
                                case "_m_dy":
                                    self.rightRearRadarPersonas[sor[-2]]["yIndex"] = i
                                case "_m_vx":
                                    self.rightRearRadarPersonas[sor[-2]]["vxIndex"] = i
                                case "_m_vy":
                                    self.rightRearRadarPersonas[sor[-2]]["vyIndex"] = i
                                case "_m_ax":
                                    self.rightRearRadarPersonas[sor[-2]]["axIndex"] = i
                                case "_m_az":
                                    self.rightRearRadarPersonas[sor[-2]]["azIndex"] = i
        self.__update__()
    def __update__(self):
        self.time = self.database[self.databaseLinePivot][1]
        for i in self.cameraPersonas:
            print(i,end="\n")
        self.databaseLinePivot = self.databaseLinePivot + 1
        pass
