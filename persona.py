from re import X


class Persona:
    def __init__(self,id,xIndex,x,yIndex,y,tipusIndex,tipus,vyIndex,vy,vxIndex,vx):
        self.name = id;
        self.xIndex = xIndex;
        self.x = x; 
        self.yIndex = yIndex;
        self.y = y;
        self.vxIndex= vxIndex;
        self.vx = vx;
        self.vyIndex= vyIndex;
        self.vy = vy;
        self.tipusIndex = tipusIndex;
        self.tipus = tipus;
        pass

    def __update__(self,x,y,tipus,vy,vx):
        self.x = x; 
        self.y = y;
        self.vx = vx;
        self.vy = vy;
        self.tipus = tipus
        pass