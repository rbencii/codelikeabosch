
import csv


class objects:
    def __init__(self):
        with open('PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_340.csv', 'rt') as f:
           reader = csv.reader(f)
           self.database = list(reader)
        pass
