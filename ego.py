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

    def __init__(self, vxvRef, axvRef, vyvRef, ayvRef, psiDtOpt):
        self.vxvRef = vxvRef
        self.axvRef = axvRef
        self.vyvRef = vyvRef
        self.ayvRef = ayvRef
        self.psiDtOpt = psiDtOpt