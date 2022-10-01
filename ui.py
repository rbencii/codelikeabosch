#win: pip3 install arcade
import arcade
import os
import math
from tkinter import filedialog
from ego import Ego

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Full Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5

#FILE VALASZTAS
#egoObj = Ego(filedialog.askopenfilename())
egoObj = Ego()


CARSIZE = 250
CARWIDTH=CARSIZE/2.4
METERTOPIXEL=CARSIZE/4.65
STREETSIZE = 500
AXLEP=3.43

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
def carspacetoscreenspace(screencarcenterX,screencarcenterY,carSpaceX,carSpaceY,METERTOPIXEL):
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
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True)

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
        arcade.set_background_color(arcade.color.BABY_BLUE)
        #self.set_update_rate(1/6000)
        self.car = arcade.load_texture("car2.png")
        self.street = arcade.load_texture("street.png")
        self.streetX = 0
        self.streetY = 0
        self.slider=100

    def on_update(self, delta_time):
        egoObj.__update__()
        # v = s/t
        # egoObj.vxvRef = s meter / 1sec
        # s = egoObj.vxvRef
        #self.streetX-=egoObj.vyvRef
        #self.streetx-=math.cos
        self.streetY-=egoObj.vxvRef
        if self.streetY<=-500:
            self.streetY=0

    def on_draw(self):
        """
        Render the screen.
        """

        self.clear()

        # Get viewport dimensions
        left, screen_width, bottom, screen_height = self.get_viewport()
        centerX=screen_width/2.0
        centerY=screen_height/2.0
        # Draw some boxes on the bottom so we can see how they change
        for i in range(4):
            arcade.draw_texture_rectangle(centerX+self.streetX, i*STREETSIZE+self.streetY, STREETSIZE, STREETSIZE, self.street,egoObj.psiDtOpt)

        #auto
        arcade.draw_texture_rectangle(centerX, centerY, CARSIZE, CARSIZE, self.car)
        arcade.draw_text("iterator: " + str(egoObj.iterator),300,1000)
        arcade.draw_text("T: " + egoObj.T,300,900)
        arcade.draw_text("axvRef: " + str(egoObj.axvRef),300,800)
        arcade.draw_text("ayvRef: " + str(egoObj.ayvRef),300,700)
        arcade.draw_text("psiDtOpt: " + str(egoObj.psiDtOpt),300,600)
        arcade.draw_text("tAbsRefTime: " + str(egoObj.tAbsRefTime),300,500)
        arcade.draw_text("vxvRef: " + str(egoObj.vxvRef),300,400)
        arcade.draw_text("vyvRef: " + str(egoObj.vyvRef),300,300)

        #koordinatarendszer
        arcade.draw_line(centerX-CARWIDTH/2.0,centerY-CARSIZE/AXLEP,centerX+CARWIDTH/2.0,centerY-CARSIZE/AXLEP,arcade.color.YELLOW,5)
        arcade.draw_line(centerX,centerY+CARSIZE/2.0,centerX,centerY-CARSIZE/2.0,arcade.color.YELLOW,5)

        origox=centerX
        origoy=centerY-CARSIZE/AXLEP
        #radarbalelso
        radarcarx,radarcary=carspacetoscreenspace(origox,origoy,
        egoObj.X_POSITION_CORNER_RADAR_LEFT_FRONT,
        egoObj.Y_POSITION_CORNER_RADAR_LEFT_FRONT,METERTOPIXEL)
        arcade.draw_point(radarcarx,radarcary,arcade.color.AMARANTH_PINK,10)

        #radarjobbelso
        radarcarx,radarcary=carspacetoscreenspace(origox,origoy,
        egoObj.X_POSITION_CORNER_RADAR_RIGHT_FRONT,
        egoObj.Y_POSITION_CORNER_RADAR_RIGHT_FRONT,METERTOPIXEL)
        arcade.draw_point(radarcarx,radarcary,arcade.color.AMARANTH_PINK,10)

        #radarbalhatso
        radarcarx,radarcary=carspacetoscreenspace(origox,origoy,
        egoObj.X_POSITION_CORNER_RADAR_LEFT_REAR,
        egoObj.Y_POSITION_CORNER_RADAR_LEFT_REAR,METERTOPIXEL)
        arcade.draw_point(radarcarx,radarcary,arcade.color.AMARANTH_PINK,10)

        #radarjobbhatso
        radarcarx,radarcary=carspacetoscreenspace(origox,origoy,
        egoObj.X_POSITION_CORNER_RADAR_RIGHT_REAR,
        egoObj.Y_POSITION_CORNER_RADAR_RIGHT_REAR,METERTOPIXEL)
        arcade.draw_point(radarcarx,radarcary,arcade.color.AMARANTH_PINK,10)


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.F:
            # User hits f. Flip between full and not full screen.
            self.set_fullscreen(not self.fullscreen)

            # Get the window coordinates. Match viewport to window coordinates
            # so there is a one-to-one mapping.
            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)
        if key == arcade.key.UP:
            self.slider+=1

def ui_run():
    MyGame()
    arcade.run()
