class Predict:

    def __init__(self):
        self.predictions = []

    def createPred(self, objects, time=0.1):  # after render
        RADIUS = 5
        oldPredictions = self.predictions
        self.predictions = []
        closeObjecs = []
        for obj in objects:
            if obj["x"] < RADIUS and obj["x"] > -RADIUS and obj["y"] < RADIUS and obj["y"] > -RADIUS:
                closeObjecs.append(obj)
        for obj in closeObjecs:
            self.predictions.append({"x": obj["x"] + time*obj["vx"], "y": obj["y"] + time*obj["vy"], "vx": obj["vx"], "vy": obj["vy"],
                                    "type": obj["type"] if "type" in obj else 0, "lifeSpan": obj["lifeSpan"]-time if "lifeSpan" in obj else 3.0})

        closeObjecs = []
        for obj in oldPredictions:
            if obj["x"] < RADIUS and obj["x"] > -RADIUS and obj["y"] < RADIUS and obj["y"] > -RADIUS:
                closeObjecs.append(obj)
        for obj in closeObjecs:
            self.predictions.append({"x": obj["x"] + time*obj["vx"], "y": obj["y"] + time*obj["vy"], "vx": obj["vx"],
                                    "vy": obj["vy"], "type": obj["type"] if "type" in obj else 0, "lifeSpan": obj["lifeSpan"]-time})

    def filterPred(self, objects):  # before render
        # print((self.predictions))

        for obj in self.predictions:
            for realObj in objects:
                if obj["x"] < realObj["x"] + 2 and obj["x"] > realObj["x"] - 2 and obj["y"] < realObj["y"] + 2 and obj["y"] > realObj["y"] - 2:
                    if obj in self.predictions:
                        self.predictions.remove(obj)
                if "lifeSpan" in obj and obj["lifeSpan"] < 0:
                    if obj in self.predictions:
                        self.predictions.remove(obj)
