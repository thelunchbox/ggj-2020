import pygame

from rbt.game_components.button import Button
from rbt.utils.constants import *


class Hud:
    def __init__(self):
        self.buttons = []

    def generate_attack_tool_button(self):
        btn = Button((204, 0, 0), ATTACK_BUTTON_X, ATTACK_BUTTON_Y, TOOL_BUTTON_WIDTH, TOOL_BUTTON_HEIGHT, str("Attack"))
        self.buttons.append(btn)
    def generate_gather_tool_button(self):
        btn = Button((0, 153, 0), GATHER_BUTTON_X, GATHER_BUTTON_Y, TOOL_BUTTON_WIDTH, TOOL_BUTTON_HEIGHT, str("Gather"))
        self.buttons.append(btn)
    def generate_signal_tool_button(self):
        btn = Button((51, 153, 255), SIGNAL_BUTTON_X, SIGNAL_BUTTON_Y, TOOL_BUTTON_WIDTH-20, TOOL_BUTTON_HEIGHT, str("Signal"))
        self.buttons.append(btn)
    def generate_build_tool_button(self):
        btn = Button((204, 102, 0), BUILD_BUTTON_X, BUILD_BUTTON_Y, TOOL_BUTTON_WIDTH, TOOL_BUTTON_HEIGHT, str("Build"))
        self.buttons.append(btn)

    def generate_bot_button(self, slots):
        btn = Button((0, 255, 255), 800, 500, 100, 30, str("Create " + slots) + " slot bot")
        self.buttons.append(btn)

    def render(self, screen):
        #self.generate_bot_button('four')
        self.generate_attack_tool_button()
        self.generate_gather_tool_button()
        self.generate_build_tool_button()
        self.generate_signal_tool_button()
        for button in self.buttons:
            button.draw(screen, (0,0,0))

