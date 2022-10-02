class Predict:
    def __init__(self):
        self.predictions = []

    def createPred(self, objects, time=0.1): #after render
        oldPredictions = self.predictions
        self.predictions = []
        closeObjecs = []
        for obj in objects:
            if obj["x"] < 10 and obj["x"] > -10 and obj["y"] < 10 and obj["y"] > -10:
                closeObjecs.append(obj)
        for obj in closeObjecs:
            self.predictions.append({"x":obj["x"] + time*obj["vx"],"y":obj["y"] + time*obj["vy"],"vx":obj["vx"],"vy":obj["vy"],"type":obj["type"] if "type" in obj else 0})
        
        closeObjecs = []
        for obj in oldPredictions:
            if obj["x"] < 10 and obj["x"] > -10 and obj["y"] < 10 and obj["y"] > -10:
                closeObjecs.append(obj)
        for obj in closeObjecs:
            self.predictions.append({"x":obj["x"] + time*obj["vx"],"y":obj["y"] + time*obj["vy"],"vx":obj["vx"],"vy":obj["vy"],"type":obj["type"] if "type" in obj else 0})

    def filterPred(self, objects): #before render
        print(len(self.predictions))
        for obj in self.predictions:
            for realObj in objects:
                if obj["x"] < realObj["x"] + 2 and obj["x"] > realObj["x"] - 2 and obj["y"] < realObj["y"] + 2 and obj["y"] > realObj["y"] - 2:
                    if obj in self.predictions:
                        self.predictions.remove(obj)
