# win: pip3 install arcade

from glob import glob
import arcade
import arcade.gui
import os
import math
#from tkinter import filedialog
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
egoObj = Ego()

objectLayer = Objects()

origox = 0
origoy = 0

CARSIZE = 250
CARWIDTH = CARSIZE/2.4
METERTOPIXEL = CARSIZE/4.65
STREETSIZE = 500
AXLEP = 3.43

Files = [{"objektumok": "data/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_349.csv",
         "auto": 'data/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_416.csv'},
         {"objektumok": "data/PSA_ADAS_W3_FC_2022-09-01_15-03_0057.MF4/Group_349.csv",
         "auto": 'data/PSA_ADAS_W3_FC_2022-09-01_15-03_0057.MF4/Group_416.csv'},
         {"objektumok": "data/PSA_ADAS_W3_FC_2022-09-01_15-12_0059.MF4/Group_349.csv",
         "auto": 'data/PSA_ADAS_W3_FC_2022-09-01_15-12_0059.MF4/Group_416.csv'},
         {"objektumok": "data/PSA_ADAS_W3_FC_2022-09-01_15-17_0060.MF4/Group_349.csv",
         "auto": 'data/PSA_ADAS_W3_FC_2022-09-01_15-17_0060.MF4/Group_416.csv'}]
Cars = ["car.png", "car2.png"]
ChoosenFile = 1
ChoosenCar = 0

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
        # self.set_update_rate(1/6000)

        self.setup()

        self.create_buttons()

    def setup(self,carType=0):
        global egoObj
        global objectLayer
        self.car = arcade.load_texture(Cars[carType])
        self.streetX = -100
        self.streetY = 0
        self.slider = 100
        egoObj = Ego(Files[ChoosenFile]["auto"])
        objectLayer = Objects(Files[ChoosenFile]["objektumok"])

    def on_update(self, delta_time):
        egoObj.__update__()
        objectLayer.__update__()
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

    def on_draw(self):
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
        arcade.draw_text("iterator: " + str(egoObj.iterator),
                         screen_width-200, screen_height-20)
        arcade.draw_text("T: " + egoObj.T, screen_width-200, screen_height-50)
        arcade.draw_text("axvRef: " + str(egoObj.axvRef),
                         screen_width-200, screen_height-80)
        arcade.draw_text("ayvRef: " + str(egoObj.ayvRef),
                         screen_width-200, screen_height-110)
        arcade.draw_text("psiDtOpt: " + str(egoObj.psiDtOpt),
                         screen_width-200, screen_height-140)
        arcade.draw_text("tAbsRefTime: " + str(egoObj.tAbsRefTime),
                         screen_width-200, screen_height-170)
        arcade.draw_text("vxvRef: " + str(egoObj.vxvRef),
                         screen_width-200, screen_height-200)
        arcade.draw_text("vyvRef: " + str(egoObj.vyvRef),
                         screen_width-200, screen_height-230)
        # Objects

        # koordinatarendszer
        arcade.draw_line(centerX-CARWIDTH/2.0, centerY-CARSIZE/AXLEP, centerX +
                         CARWIDTH/2.0, centerY-CARSIZE/AXLEP, arcade.color.YELLOW, 5)
        arcade.draw_line(centerX, centerY+CARSIZE/2.0, centerX,
                         centerY-CARSIZE/2.0, arcade.color.YELLOW, 5)

        origox = centerX
        origoy = centerY-CARSIZE/AXLEP
        # radarbalelso
        radarcarx, radarcary = carspacetoscreenspace(origox, origoy,
                                                     egoObj.X_POSITION_CORNER_RADAR_LEFT_FRONT,
                                                     egoObj.Y_POSITION_CORNER_RADAR_LEFT_FRONT, METERTOPIXEL)
        arcade.draw_point(radarcarx, radarcary, arcade.color.AMARANTH_PINK, 10)

        origox = centerX
        origoy = centerY-CARSIZE/AXLEP


        cameraposX,cameraposY=carspacetoscreenspace(origox,origoy,float(objectLayer.cameraPosX),float(objectLayer.cameraPosY),METERTOPIXEL)
        arcade.draw_point(cameraposX,cameraposY,arcade.color.LIME_GREEN,20)
        arcade.draw_text("Camera",cameraposX,cameraposY,anchor_x="center",anchor_y="center")

        #Objects
        #print(len(objectLayer.realObjects)) 
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
            arcade.draw_text("Object id: " + str(i), screen_width-310, 33*i+40)
            if (objectLayer.realObjects[i].keys().__contains__("type")):
                if (objectLayer.realObjects[i]["type"] == "0"):
                    arcade.draw_text(
                        "Type: unknown", screen_width-220, 33*i+40, arcade.color.ROSE_RED)
                elif (objectLayer.realObjects[i]["type"] == "1"):
                    arcade.draw_text("Type: truck", screen_width -
                                     220, 33*i+40, arcade.color.DARK_BLUE)
                elif (objectLayer.realObjects[i]["type"] == "2"):
                    arcade.draw_text("Type: car", screen_width -
                                     220, 33*i+40, arcade.color.FERN_GREEN)
                elif (objectLayer.realObjects[i]["type"] == "3"):
                    arcade.draw_text(
                        "Type: motorbike", screen_width-220, 33*i+40, arcade.color.AMARANTH_PURPLE)
                elif (objectLayer.realObjects[i]["type"] == "4"):
                    arcade.draw_text(
                        "Type: cyclist", screen_width-220, 33*i+40, arcade.color.ANDROID_GREEN)
                elif (objectLayer.realObjects[i]["type"] == "5"):
                    arcade.draw_text(
                        "Type: pedestrian", screen_width-220, 33*i+40, arcade.color.BABY_PINK)
                elif (objectLayer.realObjects[i]["type"] == "6"):
                    arcade.draw_text(
                        "Type: truck/car", screen_width-220, 33*i+40, arcade.color.STAR_COMMAND_BLUE)
            else:
                arcade.draw_text("Type: unknown", screen_width -
                                 220, 33*i+40, arcade.color.ROSE_RED)
            arcade.draw_text(
                "vx: " + str(objectLayer.realObjects[i]["vx"]), screen_width-110, 33*i+40)
            arcade.draw_text(
                "X: " + str(objectLayer.realObjects[i]["x"]), screen_width-310, 33*i+22)
            arcade.draw_text(
                "Y: " + str(objectLayer.realObjects[i]["y"]), screen_width-220, 33*i+22)
            arcade.draw_text(
                "vy: " + str(objectLayer.realObjects[i]["vy"]), screen_width-110, 33*i+22)

        # radarjobbelso
        radarcarx, radarcary = carspacetoscreenspace(origox, origoy,
                                                     egoObj.X_POSITION_CORNER_RADAR_RIGHT_FRONT,
                                                     egoObj.Y_POSITION_CORNER_RADAR_RIGHT_FRONT, METERTOPIXEL)
        arcade.draw_point(radarcarx, radarcary, arcade.color.AMARANTH_PINK, 10)

        radarAngle = 90+egoObj.ANGLE_AZIMUTH_CORNER_RADAR_RIGHT_FRONT
        tmpList = [radarAngle, 90]
        tmpList.sort()
        startAngle,endAngle=tuple(tmpList)
        arcade.draw_arc_filled(radarcarx,radarcary,500,500,arcade.color.AMARANTH_PINK,startAngle,endAngle)
        arcade.draw_text("RFCorner Radar",radarcarx,radarcary,anchor_x="left",anchor_y="bottom",multiline=True,width=50)

        # radarbalelso
        radarcarx, radarcary = carspacetoscreenspace(origox, origoy,
                                                     egoObj.X_POSITION_CORNER_RADAR_LEFT_FRONT,
                                                     egoObj.Y_POSITION_CORNER_RADAR_LEFT_FRONT, METERTOPIXEL)
        arcade.draw_point(radarcarx, radarcary, arcade.color.AMARANTH_PINK, 10)

        radarAngle = 90+egoObj.ANGLE_AZIMUTH_CORNER_RADAR_LEFT_FRONT
        tmpList = [radarAngle, 90]
        tmpList.sort()
        startAngle,endAngle=tuple(tmpList)
        arcade.draw_arc_filled(radarcarx,radarcary,500,500,arcade.color.AMARANTH_PINK,startAngle,endAngle)
        arcade.draw_text("LFCorner Radar",radarcarx,radarcary,anchor_x="right",anchor_y="bottom",multiline=True,width=50)

        # radarbalhatso
        radarcarx, radarcary = carspacetoscreenspace(origox, origoy,
                                                     egoObj.X_POSITION_CORNER_RADAR_LEFT_REAR,
                                                     egoObj.Y_POSITION_CORNER_RADAR_LEFT_REAR, METERTOPIXEL)
        arcade.draw_point(radarcarx, radarcary, arcade.color.AMARANTH_PINK, 10)

        radarAngle = 90+egoObj.ANGLE_AZIMUTH_CORNER_RADAR_LEFT_REAR
        tmpList = [radarAngle, 270]
        tmpList.sort()
        startAngle,endAngle=tuple(tmpList)
        arcade.draw_arc_filled(radarcarx,radarcary,500,500,arcade.color.AMARANTH_PINK,startAngle,endAngle)
        arcade.draw_text("LRCorner Radar",radarcarx,radarcary,anchor_x="right",anchor_y="top",multiline=True,width=50)

        # radarjobbhatso
        radarcarx, radarcary = carspacetoscreenspace(origox, origoy,
                                                     egoObj.X_POSITION_CORNER_RADAR_RIGHT_REAR,
                                                     egoObj.Y_POSITION_CORNER_RADAR_RIGHT_REAR, METERTOPIXEL)
        arcade.draw_point(radarcarx, radarcary, arcade.color.AMARANTH_PINK, 10)

        radarAngle = 180-egoObj.ANGLE_AZIMUTH_CORNER_RADAR_RIGHT_REAR
        tmpList = [radarAngle, 270]
        tmpList.sort()
        startAngle,endAngle=tuple(tmpList)
        arcade.draw_arc_filled(radarcarx,radarcary,500,500,arcade.color.AMARANTH_PINK,startAngle,endAngle)
        arcade.draw_text("RRCorner Radar",radarcarx,radarcary,anchor_x="left",anchor_y="top",multiline=True,width=50)

        #turn signal

        signalcarx,signalcary=carspacetoscreenspace(origox,origoy,
        egoObj.X_POSITION_CORNER_RADAR_RIGHT_FRONT,
        egoObj.Y_POSITION_CORNER_RADAR_RIGHT_FRONT,METERTOPIXEL)
        arcade.draw_parabola_filled(signalcarx-17, signalcary-35,signalcarx+24 , 17, arcade.color.YELLOW_ORANGE,-55)

        signalcarx,signalcary=carspacetoscreenspace(origox,origoy,
        egoObj.X_POSITION_CORNER_RADAR_LEFT_FRONT,
        egoObj.Y_POSITION_CORNER_RADAR_LEFT_FRONT,METERTOPIXEL)
        arcade.draw_parabola_filled(signalcarx+17, signalcary-35,signalcarx-24, 17, arcade.color.YELLOW_ORANGE,55)

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

        # draw manager for buttons
        self.button_manager.draw()

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

    def choose_file(self, index):
        ChoosenFile = index
        egoObj = Ego(Files[ChoosenFile]["auto"])
        objectLayer = Objects(Files[ChoosenFile]["objektumok"])

    def choose_car(self, index):
        ChoosenCar = index


    def create_buttons(self):
        BUTTON_WIDTH = 100
        PADDING = 10

        self.button_manager = arcade.gui.UIManager()
        self.button_manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(
            text="Start", width=BUTTON_WIDTH, style=self.button_style)
        self.v_box.add(start_button.with_space_around(
            top=PADDING, left=PADDING))

        ind = 0
        for ind in range(len(Files)):
            button = arcade.gui.UIFlatButton(
                text="File_" + str(ind+1), width=BUTTON_WIDTH, style=self.button_style)
            self.v_box.add(button.with_space_around(
                top=PADDING, left=PADDING))
            button.on_click = self.choose_file(ind)

        for ind in range(len(Cars)):
            button = arcade.gui.UIFlatButton(text=Cars[ind], width=BUTTON_WIDTH, style=self.button_style)
            self.v_box.add(button.with_space_around(
                top=PADDING, left=PADDING))
            button.on_click = self.choose_car(ind)

        self.button_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="top",
                child=self.v_box)
        )
        
def ui_run():
    MyGame()
    arcade.run()
