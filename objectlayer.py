
import csv
from persona import Persona

class objects:
    def __init__(self):
        with open('PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_340.csv', 'rt') as f:
           reader = csv.reader(f)
           self.database = list(reader)
           self.cameraPersonas = {}
           self.leftRearRadarPersonas = {}
           self.leftFrontRadarPersonas = {}
           self.rightRearRadarPersonas = {}
        for i in range(len(self.database[0])):
            sor = self.database[0][i].split('.')
            match sor[7]:
                case "m_camData":
                    match sor[-1]:
                        case "_m_dx":
                            self.cameraPersonas[sor[-2]] = Persona()
                case "_m_cornerData":
                    match sor[-5]:
                        case "_0_":
                            
                        case "_1_":
                        case "_2_":
                        case "_3_":

    def __update__(self):

        pass
