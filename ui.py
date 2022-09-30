import math
import sys
import pygame

from miscelanous import Colors


class UI:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((1280, 720))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        pygame.display.set_caption("Vehicle Radar Help System")
        #game_icon = pygame.image.load('res/logo.png')
        #pygame.display.set_icon(game_icon)
        
    def update(self):
        self.screen.fill(Colors.WHITE)

        self.draw_game_map()

        mouse_pos = pygame.mouse.get_pos()

    def draw_game_map(self):
        rect = pygame.Rect(0, 0, self.width, self.height * 0.5)
        pygame.draw.rect(self.screen, Colors.LIGHTGREY, rect)

    def draw_dashboard(self):
        """Draws the dashboard of the gui"""
        pygame.draw.rect(self.screen, Colors.LIGHTSLATEGREY, self.dashboard_container.rect)
        #self.play_btn.draw()
        #self.exit_btn.draw()
        #self.reset_btn.draw()
        #self.stop_btn.draw()
        #self.data_table.draw()
        #self.draw_obstacle_drag_in()
        #self.size_picker.draw()