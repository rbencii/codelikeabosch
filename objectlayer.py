
import csv
import math
from normalize import normalize

class Objects:
    def __init__(self,filePath = 'data/PSA_ADAS_W3_FC_2022-09-01_15-12_0059.MF4/Group_349.csv'):
        with open(filePath, 'rt') as f:
           reader = csv.reader(f)
           self.database = list(reader)
           self.cameraPersonas = {}
           self.leftRearRadarPersonas = {}
           self.leftFrontRadarPersonas = {}
           self.rightRearRadarPersonas = {}
           self.rightFrontRadarPersonas = {}
        self.databaseLinePivot = 1
        self.EndOfList = len(self.database)<=self.databaseLinePivot
        self.cameraPosX = self.database[1][-3]
        self.cameraPosY = self.database[1][-2]
        self.cameraPosZ = self.database[1][-1]
        for i in range(2,len(self.database[0])-3,1):
            sor = self.database[0][i].split('.')
            match sor[7]:
                case "_m_camData":
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
                        case "_m_objType":
                            self.cameraPersonas[sor[-2]]["typeIndex"] = i
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
                                case "_m_ay":
                                    self.leftFrontRadarPersonas[sor[-2]]["ayIndex"] = i 
                                case "_m_dz":
                                    self.leftFrontRadarPersonas[sor[-2]]["zIndex"] = i   
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
                                case "_m_ay":
                                    self.leftRearRadarPersonas[sor[-2]]["ayIndex"] = i
                                case "_m_dz":
                                    self.leftRearRadarPersonas[sor[-2]]["zIndex"] = i
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
                                case "_m_ay":
                                    self.rightFrontRadarPersonas[sor[-2]]["ayIndex"] = i
                                case "_m_dz":
                                    self.rightFrontRadarPersonas[sor[-2]]["zIndex"] = i
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
                                case "_m_dz":
                                    self.rightRearRadarPersonas[sor[-2]]["zIndex"] = i
                                case "_m_vx":
                                    self.rightRearRadarPersonas[sor[-2]]["vxIndex"] = i
                                case "_m_vy":
                                    self.rightRearRadarPersonas[sor[-2]]["vyIndex"] = i
                                case "_m_ax":
                                    self.rightRearRadarPersonas[sor[-2]]["axIndex"] = i
                                case "_m_ay":
                                    self.rightRearRadarPersonas[sor[-2]]["ayIndex"] = i
        self.__update__()

    def __update__(self,limitMargin = 0.2):
        self.EndOfList = len(self.database)<=self.databaseLinePivot

        if(self.EndOfList):
            return

        self.realObjects = []
        self.time = self.database[self.databaseLinePivot][0]

        limit=math.floor(float(self.time)*1000.0)/1000.0+limitMargin
        
        while math.floor(float(self.time)*1000.0)/1000.0<limit and not self.EndOfList:
            self.databaseLinePivot+=1
            self.EndOfList = len(self.database)<=self.databaseLinePivot
            if not self.EndOfList:
                self.time=self.database[self.databaseLinePivot][0]
            else:
                return





            '''self.databaseLinePivot+=1
            self.EndOfList = len(self.database)<=self.databaseLinePivot
            if(self.EndOfList):
                self.time = self.database[self.databaseLinePivot-1][0]
            else:
                self.time = self.database[self.databaseLinePivot][0]
            if(math.floor(float(self.time))>=limit):
                found = True
                if(limit - float(self.database[self.databaseLinePivot-1][0]) < float(self.database[self.databaseLinePivot][0]) - limit):
                    self.databaseLinePivot-=1
                    self.time = self.database[self.databaseLinePivot][0]'''

        for i in self.cameraPersonas:
            self.cameraPersonas[i]["x"] = self.database[self.databaseLinePivot][self.cameraPersonas[i]["xIndex"]]
            self.cameraPersonas[i]["y"] = self.database[self.databaseLinePivot][self.cameraPersonas[i]["yIndex"]]
            self.cameraPersonas[i]["vx"] = self.database[self.databaseLinePivot][self.cameraPersonas[i]["vxIndex"]]
            self.cameraPersonas[i]["vy"] = self.database[self.databaseLinePivot][self.cameraPersonas[i]["vyIndex"]]
            self.cameraPersonas[i]["type"] = self.database[self.databaseLinePivot][self.cameraPersonas[i]["typeIndex"]]
        for i in self.leftFrontRadarPersonas:
            self.leftFrontRadarPersonas[i]["x"] = self.database[self.databaseLinePivot][self.leftFrontRadarPersonas[i]["xIndex"]]
            self.leftFrontRadarPersonas[i]["y"] = self.database[self.databaseLinePivot][self.leftFrontRadarPersonas[i]["yIndex"]]
            self.leftFrontRadarPersonas[i]["z"] = self.database[self.databaseLinePivot][self.leftFrontRadarPersonas[i]["zIndex"]]
            self.leftFrontRadarPersonas[i]["vx"] = self.database[self.databaseLinePivot][self.leftFrontRadarPersonas[i]["vxIndex"]]
            self.leftFrontRadarPersonas[i]["vy"] = self.database[self.databaseLinePivot][self.leftFrontRadarPersonas[i]["vyIndex"]]
            self.leftFrontRadarPersonas[i]["ax"] = self.database[self.databaseLinePivot][self.leftFrontRadarPersonas[i]["axIndex"]]
            self.leftFrontRadarPersonas[i]["ay"] = self.database[self.databaseLinePivot][self.leftFrontRadarPersonas[i]["ayIndex"]]
        for i in self.leftRearRadarPersonas:
            self.leftRearRadarPersonas[i]["x"] = self.database[self.databaseLinePivot][self.leftRearRadarPersonas[i]["xIndex"]]
            self.leftRearRadarPersonas[i]["y"] = self.database[self.databaseLinePivot][self.leftRearRadarPersonas[i]["yIndex"]]
            self.leftRearRadarPersonas[i]["z"] = self.database[self.databaseLinePivot][self.leftRearRadarPersonas[i]["zIndex"]]
            self.leftRearRadarPersonas[i]["vx"] = self.database[self.databaseLinePivot][self.leftRearRadarPersonas[i]["vxIndex"]]
            self.leftRearRadarPersonas[i]["vy"] = self.database[self.databaseLinePivot][self.leftRearRadarPersonas[i]["vyIndex"]]
            self.leftRearRadarPersonas[i]["ax"] = self.database[self.databaseLinePivot][self.leftRearRadarPersonas[i]["axIndex"]]
            self.leftRearRadarPersonas[i]["ay"] = self.database[self.databaseLinePivot][self.leftRearRadarPersonas[i]["ayIndex"]]
        for i in self.rightFrontRadarPersonas:
            self.rightFrontRadarPersonas[i]["x"] = self.database[self.databaseLinePivot][self.rightFrontRadarPersonas[i]["xIndex"]]
            self.rightFrontRadarPersonas[i]["y"] = self.database[self.databaseLinePivot][self.rightFrontRadarPersonas[i]["yIndex"]]
            self.rightFrontRadarPersonas[i]["z"] = self.database[self.databaseLinePivot][self.rightFrontRadarPersonas[i]["zIndex"]]
            self.rightFrontRadarPersonas[i]["vx"] = self.database[self.databaseLinePivot][self.rightFrontRadarPersonas[i]["vxIndex"]]
            self.rightFrontRadarPersonas[i]["vy"] = self.database[self.databaseLinePivot][self.rightFrontRadarPersonas[i]["vyIndex"]]
            self.rightFrontRadarPersonas[i]["ax"] = self.database[self.databaseLinePivot][self.rightFrontRadarPersonas[i]["axIndex"]]
            self.rightFrontRadarPersonas[i]["ay"] = self.database[self.databaseLinePivot][self.rightFrontRadarPersonas[i]["ayIndex"]]
        for i in self.rightRearRadarPersonas:
            self.rightRearRadarPersonas[i]["x"] = self.database[self.databaseLinePivot][self.rightRearRadarPersonas[i]["xIndex"]]
            self.rightRearRadarPersonas[i]["y"] = self.database[self.databaseLinePivot][self.rightRearRadarPersonas[i]["yIndex"]]
            self.rightRearRadarPersonas[i]["z"] = self.database[self.databaseLinePivot][self.rightRearRadarPersonas[i]["zIndex"]]
            self.rightRearRadarPersonas[i]["vx"] = self.database[self.databaseLinePivot][self.rightRearRadarPersonas[i]["vxIndex"]]
            self.rightRearRadarPersonas[i]["vy"] = self.database[self.databaseLinePivot][self.rightRearRadarPersonas[i]["vyIndex"]]
            self.rightRearRadarPersonas[i]["ax"] = self.database[self.databaseLinePivot][self.rightRearRadarPersonas[i]["axIndex"]]
            self.rightRearRadarPersonas[i]["ay"] = self.database[self.databaseLinePivot][self.rightRearRadarPersonas[i]["ayIndex"]]
        
        

        for i in self.cameraPersonas:
            van = True
            for j in self.realObjects:
                if(normalize('d',self.cameraPersonas[i]["x"]) - j["x"] < 0.1 and normalize('d',self.cameraPersonas[i]["x"]) - j["x"] > -0.1 and normalize('d',self.cameraPersonas[i]["y"]) - j["y"] < 0.1 and normalize('d',self.cameraPersonas[i]["y"]) - j["y"] > -0.1):
                    van = False
                    j["x"] = normalize('d',self.cameraPersonas[i]["x"])
                    j["y"] = normalize('d',self.cameraPersonas[i]["y"])
                    j["vx"] = normalize('v',self.cameraPersonas[i]["vx"])
                    j["vy"] = normalize('v',self.cameraPersonas[i]["vy"])
                    j["type"] = self.cameraPersonas[i]["type"]
            if(van and normalize('d',self.cameraPersonas[i]["x"])!=0 and normalize('d',self.cameraPersonas[i]["y"])!=0):
                self.realObjects.append({"x":normalize('d',self.cameraPersonas[i]["x"]),"y":normalize('d',self.cameraPersonas[i]["y"]),"vx":normalize('v',self.cameraPersonas[i]["vx"]),"vy":normalize('v',self.cameraPersonas[i]["vy"]),"type":self.cameraPersonas[i]["type"]})
        for i in self.leftFrontRadarPersonas:
            van = True
            for j in self.realObjects:
                if(normalize('d',self.leftFrontRadarPersonas[i]["x"]) - j["x"] < 0.1 and normalize('d',self.cameraPersonas[i]["x"]) - j["x"] > -0.1 and normalize('d',self.leftFrontRadarPersonas[i]["y"]) - j["y"] < 0.1 and normalize('d',self.leftFrontRadarPersonas[i]["y"]) - j["y"] > -0.1):
                    van = False
                    j["x"] = normalize('d',self.leftFrontRadarPersonas[i]["x"])
                    j["y"] = normalize('d',self.leftFrontRadarPersonas[i]["y"])
                    j["z"] = normalize('d',self.leftFrontRadarPersonas[i]["z"])
                    j["vx"] = normalize('v',self.leftFrontRadarPersonas[i]["vx"])
                    j["vy"] = normalize('v',self.leftFrontRadarPersonas[i]["vy"])
                    j["ax"] = normalize('a',self.leftFrontRadarPersonas[i]["ax"])
                    j["ay"] = normalize('a',self.leftFrontRadarPersonas[i]["ay"])
            if(van and normalize('d',self.leftFrontRadarPersonas[i]["x"]) != 0 and normalize('d',self.leftFrontRadarPersonas[i]["y"])!=0):
                self.realObjects.append({"z":normalize('d',self.leftFrontRadarPersonas[i]["z"]),"x":normalize('d',self.leftFrontRadarPersonas[i]["x"]),"y":normalize('d',self.leftFrontRadarPersonas[i]["y"]),"vx":normalize('v',self.leftFrontRadarPersonas[i]["vx"]),"vy":normalize('v',self.leftFrontRadarPersonas[i]["vy"]),"ax":normalize('a',self.leftFrontRadarPersonas[i]["ax"]),"ay":normalize('a',self.leftFrontRadarPersonas[i]["ay"])})
        for i in self.leftRearRadarPersonas:
            van = True
            for j in self.realObjects:
                if(normalize('d',self.leftRearRadarPersonas[i]["x"]) - j["x"] < 0.1 and normalize('d',self.cameraPersonas[i]["x"]) - j["x"] > -0.1 and normalize('d',self.leftRearRadarPersonas[i]["y"]) - j["y"] < 0.1 and normalize('d',self.leftRearRadarPersonas[i]["y"]) - j["y"] > -0.1):
                    van = False
                    j["x"] = normalize('d',self.leftRearRadarPersonas[i]["x"])
                    j["y"] = normalize('d',self.leftRearRadarPersonas[i]["y"])
                    j["z"] = normalize('d',self.leftRearRadarPersonas[i]["z"])
                    j["vx"] = normalize('v',self.leftRearRadarPersonas[i]["vx"])
                    j["vy"] = normalize('v',self.leftRearRadarPersonas[i]["vy"])
                    j["ax"] = normalize('a',self.leftRearRadarPersonas[i]["ax"])
                    j["ay"] = normalize('a',self.leftRearRadarPersonas[i]["ay"])
            if(van and normalize('d',self.leftRearRadarPersonas[i]["x"])!=0 and normalize('d',self.leftRearRadarPersonas[i]["y"])!=0):
                self.realObjects.append({"z":normalize('d',self.leftRearRadarPersonas[i]["z"]),"x":normalize('d',self.leftRearRadarPersonas[i]["x"]),"y":normalize('d',self.leftRearRadarPersonas[i]["y"]),"vx":normalize('v',self.leftRearRadarPersonas[i]["vx"]),"vy":normalize('v',self.leftRearRadarPersonas[i]["vy"]),"ax":normalize('a',self.leftRearRadarPersonas[i]["ax"]),"ay":normalize('a',self.leftRearRadarPersonas[i]["ay"])})
        for i in self.rightFrontRadarPersonas:
            van = True
            for j in self.realObjects:
                if(normalize('d',self.rightFrontRadarPersonas[i]["x"]) - j["x"] < 0.1 and normalize('d',self.cameraPersonas[i]["x"]) - j["x"] > -0.1 and normalize('d',self.rightFrontRadarPersonas[i]["y"]) - j["y"] < 0.1 and normalize('d',self.rightFrontRadarPersonas[i]["y"]) - j["y"] > -0.1):
                    van = False
                    j["x"] = normalize('d',self.rightFrontRadarPersonas[i]["x"])
                    j["y"] = normalize('d',self.rightFrontRadarPersonas[i]["y"])
                    j["z"] = normalize('d',self.rightFrontRadarPersonas[i]["z"])
                    j["vx"] = normalize('v',self.rightFrontRadarPersonas[i]["vx"])
                    j["vy"] = normalize('v',self.rightFrontRadarPersonas[i]["vy"])
                    j["ax"] = normalize('a',self.rightFrontRadarPersonas[i]["ax"])
                    j["ay"] = normalize('a',self.rightFrontRadarPersonas[i]["ay"])
            if(van and normalize('d',self.rightFrontRadarPersonas[i]["x"])!=0 and normalize('d',self.rightFrontRadarPersonas[i]["y"])!=0):
                self.realObjects.append({"z":normalize('d',self.rightFrontRadarPersonas[i]["z"]),"x":normalize('d',self.rightFrontRadarPersonas[i]["x"]),"y":normalize('d',self.rightFrontRadarPersonas[i]["y"]),"vx":normalize('v',self.rightFrontRadarPersonas[i]["vx"]),"vy":normalize('v',self.rightFrontRadarPersonas[i]["vy"]),"ax":normalize('a',self.rightFrontRadarPersonas[i]["ax"]),"ay":normalize('a',self.rightFrontRadarPersonas[i]["ay"])})
        for i in self.rightRearRadarPersonas:
            van = True
            for j in self.realObjects:
                if(normalize('d',self.rightRearRadarPersonas[i]["x"]) - j["x"] < 0.1 and normalize('d',self.cameraPersonas[i]["x"]) - j["x"] > -0.1 and normalize('d',self.rightRearRadarPersonas[i]["y"]) - j["y"] < 0.1 and normalize('d',self.rightRearRadarPersonas[i]["y"]) - j["y"] > -0.1):
                    van = False
                    j["x"] = normalize('d',self.rightRearRadarPersonas[i]["x"])
                    j["y"] = normalize('d',self.rightRearRadarPersonas[i]["y"])
                    j["z"] = normalize('d',self.rightRearRadarPersonas[i]["z"])
                    j["vx"] = normalize('v',self.rightRearRadarPersonas[i]["vx"])
                    j["vy"] = normalize('v',self.rightRearRadarPersonas[i]["vy"])
                    j["ax"] = normalize('a',self.rightRearRadarPersonas[i]["ax"])
                    j["ay"] = normalize('a',self.rightRearRadarPersonas[i]["ay"])
            if(van and normalize('d',self.rightRearRadarPersonas[i]["x"])!=0 and normalize('d',self.rightRearRadarPersonas[i]["y"])!=0):
                self.realObjects.append({"z":normalize('d',self.rightRearRadarPersonas[i]["z"]),"x":normalize('d',self.rightRearRadarPersonas[i]["x"]),"y":normalize('d',self.rightRearRadarPersonas[i]["y"]),"vx":normalize('v',self.rightRearRadarPersonas[i]["vx"]),"vy":normalize('v',self.rightRearRadarPersonas[i]["vy"]),"ax":normalize('a',self.rightRearRadarPersonas[i]["ax"]),"ay":normalize('a',self.rightRearRadarPersonas[i]["ay"])})
        self.databaseLinePivot = self.databaseLinePivot + 1
        #print(len(self.realObjects))
        pass
