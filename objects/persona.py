from re import X


class Persona:
    def __init__(self,id,x,y,tipus,vy,vx):
        self.name = id;
        self.x = x; 
        self.y = y;
        self.vx = vx;
        self.vy = vy;
        self.tipus = tipus
        pass
    def __update__(self,id,x,y,tipus,vy,vx):
        self.name = id;
        self.x = x; 
        self.y = y;
        self.vx = vx;
        self.vy = vy;
        self.tipus = tipus
        pass