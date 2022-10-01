# win: pip3 install arcade

import functools
from math import floor
import arcade
import arcade.gui
from arcade.experimental.uislider import UISlider
from arcade.gui.events import UIOnChangeEvent, UIOnClickEvent
import os
from ego import Ego
from objectlayer import Objects

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Vehicle Radar Help System"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5


# FILE VALASZTAS
#egoObj = Ego(filedialog.askopenfilename())
egoObj = {}

objectLayer = {}

origox = 0
origoy = 0

CARSIZE = 250
CARWIDTH = CARSIZE/2.4
METERTOPIXEL = CARSIZE/4.65
STREETSIZE = 500
AXLEP = 3.43
FPS = 60.0
STARTT = 0

Files = [{"objektumok": "data/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_349.csv",
         "auto": 'data/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_416.csv'},
         {"objektumok": "data/PSA_ADAS_W3_FC_2022-09-01_15-03_0057.MF4/Group_349.csv",
         "auto": 'data/PSA_ADAS_W3_FC_2022-09-01_15-03_0057.MF4/Group_416.csv'},
         {"objektumok": "data/PSA_ADAS_W3_FC_2022-09-01_15-12_0059.MF4/Group_349.csv",
         "auto": 'data/PSA_ADAS_W3_FC_2022-09-01_15-12_0059.MF4/Group_416.csv'},
         {"objektumok": "data/PSA_ADAS_W3_FC_2022-09-01_15-17_0060.MF4/Group_349.csv",
         "auto": 'data/PSA_ADAS_W3_FC_2022-09-01_15-17_0060.MF4/Group_416.csv'}]
Cars = ["car.png", "car2.png"]
choosen_file = 1
car_type = 1
pause = False

"""class Item(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1
"""
def lerp(A,B,t):
    return A+(B-A)*t

def carspacetoscreenspace(screencarcenterX, screencarcenterY, carSpaceX, carSpaceY, METERTOPIXEL):
    return (
        screencarcenterX+(-1*(carSpaceY/1000.0)*METERTOPIXEL),
        screencarcenterY+((carSpaceX/1000.0)*METERTOPIXEL)
    )


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        # Open a window in full screen mode. Remove fullscreen=True if
        # you don't want to start this way.
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=False)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # This will get the size of the window, and set the viewport to match.
        # So if the window is 1000x1000, then so will our viewport. If
        # you want something different, then use those coordinates instead.
        width, height = self.get_size()
        self.set_viewport(0, width, 0, height)
        arcade.set_background_color(arcade.color.GRAY)
        self.street = arcade.load_texture("street.png")
        self.set_update_rate(1/FPS)
        self.timecnt=0.0
        self.debugcnt2=0.0

        self.objt=arcade.Text("", 0, 0, arcade.color.BABY_BLUE, 12, multiline=True, width=300,anchor_y="bottom")
        self.multi_line_breaks = arcade.Text(
            "",
            0,0,
            arcade.color.BLACK,
            22 / 2,
            multiline=True,
            width=300,
        )
        self.innit_Alerts()

        self.setup()

        self.create_buttons()

        global STARTITERATION
        STARTT = egoObj.T

    def setup(self):
        global egoObj
        global objectLayer
        self.car = arcade.load_texture(Cars[car_type])
        self.streetX = -100
        self.streetY = 0
        self.slider = 100
        self.objectit = 1
        egoObj = Ego(Files[choosen_file]["auto"])
        objectLayer = Objects(Files[choosen_file]["objektumok"])

    def on_update(self, delta_time):
        global alert
        self.timecnt+=delta_time
        self.debugcnt2=delta_time
        
        global pause
        if pause:
            if (self.timecnt % 1) > 0.8:
                objectLayer.setState(self.objectit)
            return

        egoObj.__update__(delta_time)
        objectLayer.__update__(delta_time)
        
        # v = s/t
        # egoObj.vxvRef = s meter / 1sec
        # s = egoObj.vxvRef
        # self.streetX-=egoObj.vyvRef
        # self.streetx-=math.cos
        if (egoObj.EndOfList):
            if (egoObj.vxvRef < 1):
                egoObj.vxvRef += 0.1
            elif (egoObj.vxvRef > 1):
                egoObj.vxvRef -= 0.1
            else:
                egoObj.vxvRef = 0
                self.streetY = 0
        self.streetY -= egoObj.vxvRef
        if self.streetY <= -500:
            self.streetY = 0
        # tesztelés
        # if(egoObj.iterator >300):
        #    egoObj.EndOfList = True

        self.create_slider()
       

        #ALERT SYSTEM
        """"for i in objectLayer.realObjects:
            if (i.keys().__contains__("type")):
                if(i["type"]=="5" or i["type"]=="4"):
                    if( Ki megy-e  balra)
                        alert["TLeft"]["status"] = True
                        alert["TLeft"]["time"]= float(egoObj.T) + 5
                    if(" Ki megy-e  jobra")
            if("Közel van valami kocsi elött")
            if("Közel van valami kocsi mögött")"""

    def on_draw(self):
        global pause
        
        
        """
        Render the screen.
        """
        global origox
        global origoy
        self.clear()

        

        # Get viewport dimensions
        left, screen_width, bottom, screen_height = self.get_viewport()
        centerX = screen_width/2.0
        centerY = screen_height/2.0
        # Draw some boxes on the bottom so we can see how they change
        for i in range(4):
            arcade.draw_texture_rectangle(
                centerX+self.streetX, i*STREETSIZE+self.streetY, STREETSIZE, STREETSIZE, self.street, egoObj.psiDtOpt)

        # auto
        arcade.draw_texture_rectangle(
            centerX, centerY, CARSIZE, CARSIZE, self.car)

        cartext=""
        cartext+=("iterator: " + str(egoObj.iterator) + "\n"
        + "T: " + egoObj.T + "\n"
        + "axvRef: " + str(egoObj.axvRef) + "\n"
        + "ayvRef: " + str(egoObj.ayvRef) + "\n"
        + "psiDtOpt: " + str(egoObj.psiDtOpt) + "\n"
        + "tAbsRefTime: " + str(egoObj.tAbsRefTime) + "\n"
        + "vxvRef: " + str(egoObj.vxvRef) + "\n"
        + "vyvRef: " + str(egoObj.vyvRef) + "\n" 
        # draw debugcounters
        # + str(self.debugcnt) + "\n" + str(self.debugcnt2)
        )

        self.multi_line_breaks.text=cartext
        self.multi_line_breaks.x=screen_width-200
        self.multi_line_breaks.y=screen_height-20
        self.multi_line_breaks.draw()
        # Objects

        # koordinatarendszer
        arcade.draw_line(centerX-CARWIDTH/2.0, centerY-CARSIZE/AXLEP, centerX +
                         CARWIDTH/2.0, centerY-CARSIZE/AXLEP, arcade.color.YELLOW, 5)
        arcade.draw_line(centerX, centerY+CARSIZE/2.0, centerX,
                         centerY-CARSIZE/2.0, arcade.color.YELLOW, 5)

        origox = centerX
        origoy = centerY-CARSIZE/AXLEP


        cameraposX,cameraposY=carspacetoscreenspace(origox,origoy,float(objectLayer.cameraPosX),float(objectLayer.cameraPosY),METERTOPIXEL)
        arcade.draw_point(cameraposX,cameraposY,arcade.color.LIME_GREEN,20)
        arcade.draw_text("Camera",cameraposX,cameraposY,anchor_x="center",anchor_y="center")


        # radarjobbelso
        radarcarx, radarcary = carspacetoscreenspace(origox, origoy,
                                                     egoObj.X_POSITION_CORNER_RADAR_RIGHT_FRONT,
                                                     egoObj.Y_POSITION_CORNER_RADAR_RIGHT_FRONT, METERTOPIXEL)
        arcade.draw_point(radarcarx, radarcary, arcade.color.AMARANTH_PINK, 10)

        radarAngle = 90+egoObj.ANGLE_AZIMUTH_CORNER_RADAR_RIGHT_FRONT
        tmpList = [radarAngle-62, 92]
        tmpList.sort()
        startAngle,endAngle=tuple(tmpList)
        arcade.draw_arc_filled(radarcarx,radarcary,500,500,(15, 145, 242, 70),startAngle,endAngle)
        arcade.draw_text("RFCorner Radar",radarcarx,radarcary,anchor_x="left",anchor_y="bottom",multiline=True,width=50)

        # radarbalelso
        radarcarx, radarcary = carspacetoscreenspace(origox, origoy,
                                                     egoObj.X_POSITION_CORNER_RADAR_LEFT_FRONT,
                                                     egoObj.Y_POSITION_CORNER_RADAR_LEFT_FRONT, METERTOPIXEL)
        arcade.draw_point(radarcarx, radarcary, arcade.color.AMARANTH_PINK, 10)

        radarAngle = 90+egoObj.ANGLE_AZIMUTH_CORNER_RADAR_LEFT_FRONT
        tmpList = [radarAngle+62, 92]
        tmpList.sort()
        startAngle,endAngle=tuple(tmpList)
        arcade.draw_arc_filled(radarcarx,radarcary,500,500,(15, 145, 242, 70),startAngle,endAngle)
        arcade.draw_text("LFCorner Radar",radarcarx,radarcary,anchor_x="right",anchor_y="bottom",multiline=True,width=50)

        # radarbalhatso
        radarcarx, radarcary = carspacetoscreenspace(origox, origoy,
                                                     egoObj.X_POSITION_CORNER_RADAR_LEFT_REAR,
                                                     egoObj.Y_POSITION_CORNER_RADAR_LEFT_REAR, METERTOPIXEL)
        arcade.draw_point(radarcarx, radarcary, arcade.color.AMARANTH_PINK, 10)

        radarAngle = 90+egoObj.ANGLE_AZIMUTH_CORNER_RADAR_LEFT_REAR
        tmpList = [radarAngle-42, 272]
        tmpList.sort()
        startAngle,endAngle=tuple(tmpList)
        arcade.draw_arc_filled(radarcarx,radarcary,500,500,(15, 145, 242, 70),startAngle,endAngle)
        arcade.draw_text("LRCorner Radar",radarcarx,radarcary,anchor_x="right",anchor_y="top",multiline=True,width=50)

        # radarjobbhatso
        radarcarx, radarcary = carspacetoscreenspace(origox, origoy,
                                                     egoObj.X_POSITION_CORNER_RADAR_RIGHT_REAR,
                                                     egoObj.Y_POSITION_CORNER_RADAR_RIGHT_REAR, METERTOPIXEL)
        arcade.draw_point(radarcarx, radarcary, arcade.color.AMARANTH_PINK, 10)

        radarAngle = 180-(egoObj.ANGLE_AZIMUTH_CORNER_RADAR_RIGHT_REAR)
        tmpList = [radarAngle+42, 272]
        tmpList.sort()
        startAngle,endAngle=tuple(tmpList)
        arcade.draw_arc_filled(radarcarx,radarcary,500,500,(15, 145, 242, 70),startAngle,endAngle)
        arcade.draw_text("RRCorner Radar",radarcarx,radarcary,anchor_x="left",anchor_y="top",multiline=True,width=50)

        # holtter
        point_list = tuple(map(lambda t:
                               (carspacetoscreenspace(origox, origoy, t[0], t[1], METERTOPIXEL)[0],
                                carspacetoscreenspace(origox, origoy, t[0], t[1], METERTOPIXEL)[1]), ((-300, 800),
                                                                                                      (-300,
                                                                                                       2300),

                                                                                                      (2000, 800),
                                                                                                      (2000, 2300),

                                                                                                      (-300,
                                                                                                       800),
                                                                                                      (2000, 800),

                                                                                                      (-300,
                                                                                                       2300),
                                                                                                      (2000, 2300)
                                                                                                      )))

        arcade.draw_lines(point_list, arcade.color.RED_DEVIL, 3)

        point_list = tuple(map(lambda t:
                               (carspacetoscreenspace(origox, origoy, t[0], t[1], METERTOPIXEL)[0],
                                carspacetoscreenspace(origox, origoy, t[0], t[1], METERTOPIXEL)[1]), ((-300, -800),
                                                                                                      (-300, -2300),

                                                                                                      (2000, -800),
                                                                                                      (2000, -2300),

                                                                                                      (-300, -800),
                                                                                                      (2000, -800),

                                                                                                      (-300, -2300),
                                                                                                      (2000, -2300)
                                                                                                      )))

        arcade.draw_lines(point_list, arcade.color.RED_DEVIL, 3)

        # draw black debug point
        # arcade.draw_point(100,self.debugcnt,arcade.color.BLACK,30)

        #Objects
        #print(len(objectLayer.realObjects)) 
        objectText=""
        for i in range(len(objectLayer.realObjects)):
            objektumx, objektumy = carspacetoscreenspace(
                origox, origoy, 1000*objectLayer.realObjects[i]["x"], 1000*objectLayer.realObjects[i]["y"], METERTOPIXEL)
            #print(str(i),end=": ")
            # print(objectLayer.realObjects[i])
            if (objectLayer.realObjects[i]["x"] > -0.5 and objectLayer.realObjects[i]["x"] < 2):
                continue
            # Object texture
            if (objectLayer.realObjects[i].keys().__contains__("type")):
                if (objectLayer.realObjects[i]["type"] == "0"):
                    arcade.draw_point(objektumx, objektumy,
                                      arcade.color.ROSE_RED, 20)
                elif (objectLayer.realObjects[i]["type"] == "1"):
                    arcade.draw_point(objektumx, objektumy,
                                      arcade.color.DARK_BLUE, 35)
                elif (objectLayer.realObjects[i]["type"] == "2"):
                    arcade.draw_point(objektumx, objektumy,
                                      arcade.color.FERN_GREEN, 29)
                elif (objectLayer.realObjects[i]["type"] == "3"):
                    arcade.draw_point(objektumx, objektumy,
                                      arcade.color.AMARANTH_PURPLE, 22)
                elif (objectLayer.realObjects[i]["type"] == "4"):
                    arcade.draw_point(objektumx, objektumy,
                                      arcade.color.ANDROID_GREEN, 22)
                elif (objectLayer.realObjects[i]["type"] == "5"):
                    arcade.draw_point(objektumx, objektumy,
                                      arcade.color.BABY_PINK, 16)
                elif (objectLayer.realObjects[i]["type"] == "6"):
                    arcade.draw_point(objektumx, objektumy,
                                      arcade.color.STAR_COMMAND_BLUE, 32)
            else:
                arcade.draw_point(objektumx, objektumy,
                                  arcade.color.ROSE_RED, 25)
            # Object text
            objectText += ("Object id: " + str(i)+" ")
            if (objectLayer.realObjects[i].keys().__contains__("type")):
                if (objectLayer.realObjects[i]["type"] == "0"):
                    objectText += (
                        "Type: unknown")
                elif (objectLayer.realObjects[i]["type"] == "1"):
                    objectText += ("Type: truck")
                elif (objectLayer.realObjects[i]["type"] == "2"):
                    objectText += ("Type: car")
                elif (objectLayer.realObjects[i]["type"] == "3"):
                    objectText += (
                        "Type: motorbike")
                elif (objectLayer.realObjects[i]["type"] == "4"):
                    objectText += (
                        "Type: cyclist")
                elif (objectLayer.realObjects[i]["type"] == "5"):
                    objectText += (
                        "Type: pedestrian")
                elif (objectLayer.realObjects[i]["type"] == "6"):
                    objectText += (
                        "Type: truck/car")
            else:
                objectText += ("Type: unknown")
            objectText += (
                " vx: " + str(objectLayer.realObjects[i]["vx"]) + "\n")
            objectText += (
                "X: " + str(objectLayer.realObjects[i]["x"]) + " ")
            objectText += (
                "Y: " + str(objectLayer.realObjects[i]["y"]) + " ")
            objectText += (
                "vy: " + str(objectLayer.realObjects[i]["vy"]) + "\n")

        
        self.objt.x=screen_width-300
        self.objt.text=objectText
        self.objt.draw()
        if pause:
            arcade.draw_text("Pause", 10, 20, arcade.color.BLACK, 14)
        # draw manager for buttons
        self.button_manager.draw()
        self.slider_manager.draw()

        self.alert_Driver_draw()

        
    #  legacy fullscreen stuff
    """def on_key_press(self, key, modifiers):
        #Called whenever a key is pressed.
        if key == arcade.key.F:
            # User hits f. Flip between full and not full screen.
            self.set_fullscreen(not self.fullscreen)

            # Get the window coordinates. Match viewport to window coordinates
            # so there is a one-to-one mapping.
            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)
        if key == arcade.key.UP:
            self.slider += 1"""

    # style for buttons
    button_style = {
        "font_name": ("calibri", "arial"),
        "font_size": 15,
        "font_color": arcade.color.WHITE,
        "bg_color": arcade.color.BLUE,
        "bg_color_pressed": arcade.color.DARK_GRAY,
        "border_color_pressed": arcade.color.DARK_GRAY,
        "font_color_pressed": arcade.color.WHITE,
    }

    selected_button_style = {
        "font_name": ("calibri", "arial"),
        "font_size": 15,
        "font_color": arcade.color.WHITE,
        "bg_color": arcade.color.RED,
        "bg_color_pressed": arcade.color.DARK_GRAY,
        "border_color_pressed": arcade.color.DARK_GRAY,
        "font_color_pressed": arcade.color.WHITE,
    }

    def pause_resume(self, event):
        global pause
        if pause:
            pause = False
            objectLayer.setState(self.objectit)
        else:
            pause = True
        self.create_buttons()


    def select_file(self, event, index):
        global choosen_file 
        choosen_file = index
        self.create_buttons()
        self.setup()

    def select_car(self, event, index):
        global car_type 
        car_type = index
        self.create_buttons()
        self.car = arcade.load_texture(Cars[car_type])
    def innit_Alerts(self):
        global alert
        left, screen_width, bottom, screen_height = self.get_viewport()
        alert = {
            "Stop":{"status": False,"time": 0},
            "TLeft": {"status": False,"time": 0},
            "TRight": {"status": False,"time": 0},
            "TooCloseFront": {"status": False,"time": 0},
            "TooCloseRear": {"status": False,"time": 0},
        }
        global StopSign, DangerOnRight, DangerOnLeft, DangerOnFront, DangerOnRear, TurnRight, TurnLeft, StopText, SlowText, CarefulOnRear
        point_list = (
                    (240, screen_height-300),
                    (340, screen_height-300),
                    (340, screen_height-250),
                    (400, screen_height-350),
                    (340, screen_height-450),
                    (340, screen_height-400),
                    (240, screen_height-400))
        TurnRight = arcade.create_polygon(point_list, arcade.color.YELLOW)
        point_list = (
                    (230, screen_height-350),
                    (290, screen_height-250),
                    (290, screen_height-300),
                    (390, screen_height-300),
                    (390, screen_height-400),
                    (290, screen_height-400),
                    (290, screen_height-450))
        TurnLeft = arcade.create_polygon(point_list, arcade.color.YELLOW)
        point_list = (
                    (230, screen_height-400),
                    (230, screen_height-300),
                    (300, screen_height-238),
                    (382, screen_height-238),
                    (454, screen_height-300),
                    (454, screen_height-400),
                    (382, screen_height-462),
                    (300, screen_height-462))
        StopSign = arcade.create_polygon(point_list, arcade.color.RUBY_RED)
        StopText = arcade.Text("STOP!!",screen_width/2.0-20,screen_height-70,arcade.color.RED, 50,bold=True)
        point_list = ((screen_width-330, 20),
                    (screen_width-340, 30),
                    (screen_width-350, 300),
                    (screen_width-350, screen_height-300),
                    (screen_width-340, screen_height-30),
                    (screen_width-330, screen_height-20))
        DangerOnRight = arcade.create_polygon(point_list, arcade.color.SPANISH_RED)
        point_list = ((160, 20),
                    (170, 30),
                    (180, 300),
                    (180, screen_height-300),
                    (170, screen_height-30),
                    (160, screen_height-20))
        DangerOnLeft = arcade.create_polygon(point_list, arcade.color.SPANISH_RED)
        point_list = ((170, screen_height-10),
                    (180, screen_height-22),
                    (screen_width/2.0-170, screen_height-30),
                    (screen_width/2.0+70, screen_height-30),
                    (screen_width-340, screen_height-22),
                    (screen_width-330, screen_height-10))
        DangerOnFront = arcade.create_polygon(point_list, arcade.color.SPANISH_RED)
        SlowText = arcade.Text("Slow Down!!",screen_width/2.0-70,screen_height-70,arcade.color.RED, 50,bold=True)
        point_list = ((170, 10),
                    (180, 22),
                    (screen_width/2.0-170, 30),
                    (screen_width/2.0+70, 30),
                    (screen_width-340, 22),
                    (screen_width-330, 10))
        DangerOnRear = arcade.create_polygon(point_list, arcade.color.SPANISH_RED)
        CarefulOnRear = arcade.Text("An object is close behind you!!",screen_width/2.0-70,screen_height-70,arcade.color.RED, 40,bold=True)
    def alert_Driver_draw(self):
        global alert
        global StopSign, DangerOnRight, DangerOnLeft, DangerOnFront, DangerOnRear, TurnRight, TurnLeft, StopText, SlowText, CarefulOnRear
        for i in alert:
            if alert[i]['status'] == True:
                diff = floor(float(egoObj.T)) - alert[i]['time']
                if diff % 2 == 0:
                    if i == 'Stop':
                        StopSign.color = arcade.color.SPANISH_RED
                        StopSign.draw()
                        
                    elif i == 'TLeft':
                        TurnLeft.color = arcade.color.YELLOW_ORANGE
                        TurnLeft.draw()
                    elif i == 'TRight':
                        TurnRight.color = arcade.color.YELLOW_ORANGE
                        TurnRight.draw()
                    elif i == 'TooCloseFront':
                        SlowText.draw()
                        DangerOnFront.color = arcade.color.RUBY_RED
                        DangerOnFront.draw()
                    elif i == 'TooCloseRear':
                        CarefulOnRear.draw()
                        DangerOnRear.color = arcade.color.RUBY_RED
                        DangerOnRear.draw()
                    elif i == 'TooCloseLeft':
                        DangerOnLeft.color = arcade.color.RUBY_RED
                        DangerOnLeft.draw()
                    elif i == 'TooCloseRight':
                        DangerOnRight.color = arcade.color.RUBY_RED
                        DangerOnRight.draw()
                else:
                    if i == 'Stop':
                        StopSign.color = arcade.color.RUBY_RED
                        StopSign.draw()
                    elif i == 'TLeft':
                        TurnLeft.color = arcade.color.YELLOW
                        TurnLeft.draw()
                    elif i == 'TRight':
                        TurnRight.color = arcade.color.YELLOW
                        TurnRight.draw()
                    elif i == 'TooCloseFront':
                        SlowText.draw()
                        DangerOnFront.color = arcade.color.SPANISH_RED
                        DangerOnFront.draw()
                    elif i == 'TooCloseRear':
                        CarefulOnRear.draw()
                        DangerOnRear.color = arcade.color.SPANISH_RED
                        DangerOnRear.draw()
                    elif i == 'TooCloseLeft':
                        DangerOnLeft.color = arcade.color.SPANISH_RED
                        DangerOnLeft.draw()
                    elif i == 'TooCloseRight':
                        DangerOnRight.color = arcade.color.SPANISH_RED
                        DangerOnRight.draw()         
                if diff <= 0:
                    alert[i]['status'] = False
                    alert[i]['time'] = 0
        
    def create_buttons(self):
        global pause
        BUTTON_WIDTH = 100
        PADDING = 10

        self.button_manager = arcade.gui.UIManager()
        self.button_manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(
            text="Start" if pause else "Pause", width=BUTTON_WIDTH, style=self.button_style)
        start_button.on_click = self.pause_resume
        self.v_box.add(start_button.with_space_around(
            top=PADDING, left=PADDING))

        for i in range(len(Files)):
            if(i == choosen_file):
                button = arcade.gui.UIFlatButton(
                    text="Test_" + str(i), width=BUTTON_WIDTH, style=self.selected_button_style)
            else:
                button = arcade.gui.UIFlatButton(
                    text="Test_" + str(i), width=BUTTON_WIDTH, style=self.button_style)
            button.on_click = functools.partial(self.select_file, index=i)
            self.v_box.add(button.with_space_around(top=PADDING, left=PADDING))

        for i in range(len(Cars)):
            if(i == car_type):
                button = arcade.gui.UIFlatButton(
                    text="Car_" + str(i + 1), width=BUTTON_WIDTH, style=self.selected_button_style)
            else:
                button = arcade.gui.UIFlatButton(
                    text="Car_" + str(i + 1), width=BUTTON_WIDTH, style=self.button_style)
            button.on_click = functools.partial(self.select_car, index=i)
            self.v_box.add(button.with_space_around(top=PADDING, left=PADDING))
            
        self.create_slider()

            

        self.button_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="top",
                child=self.v_box)
        )

    def create_slider(self):
        self.slider_manager = arcade.gui.UIManager()
        self.slider_manager.enable()
        STEPS = 100
        ui_slider = UISlider(value=float(egoObj.iterator)/float(egoObj.highestit)*100, width=400, height=50)
        label = arcade.gui.UILabel(text=f"Iteration: {egoObj.iterator:02.0f}")

        @ui_slider.event()
        def on_change(event: UIOnChangeEvent):  
            egoObj.setState(int(lerp(1, egoObj.highestit, ui_slider.value/100)))
            self.objectit = int(lerp(1, objectLayer.highestit, ui_slider.value/100))
            label.text = f"Iteration: {egoObj.iterator:02.0f}"
            label.fit_content()

        

        self.slider_manager.add(arcade.gui.UIAnchorWidget(child=ui_slider, anchor_x="left", anchor_y="bottom"))
        self.slider_manager.add(arcade.gui.UIAnchorWidget(child=label, anchor_x="left", anchor_y="bottom"))
        
        
def ui_run():
    MyGame()
    arcade.run()
