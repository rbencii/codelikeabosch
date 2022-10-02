class Predict:
    def __init__(self):
        self.predictions = []

    def createPred(self, ego, objects, time=0.1):
        self.predictions = []
        closeObjecs = []
        for obj in objects:
            if obj["x"] < 10 and obj["x"] > -10 and obj["y"] < 10 and obj["y"] > -10:
                closeObjecs.append(obj)
        for obj in closeObjecs:
            self.predictions.append({"x":obj["x"] + time*obj["vx"],"y":obj["y"] + time*obj["vy"],"vx":obj["vx"],"vy":obj["vy"],"type":obj["type"]})

    def filterPred(self, objects):
        
