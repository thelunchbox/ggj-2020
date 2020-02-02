import pygame

from rbt.game_components.button import Button


class Hud:
    def __init__(self):
        self.buttons = []

    def generate_attack_tool_button(self):
        btn = Button((204, 0, 0), 1040, 0, 200, 50, str("Attack"))
        self.buttons.append(btn)
    def generate_gather_tool_button(self):
        btn = Button((0, 153, 0), 1220, 0, 200, 50, str("Gather"))
        self.buttons.append(btn)
    def generate_signal_tool_button(self):
        btn = Button((51, 153, 255), 1040, 50, 180, 50, str("Signal"))
        self.buttons.append(btn)
    def generate_build_tool_button(self):
        btn = Button((204, 102, 0), 1220, 50, 200, 50, str("Build"))
        self.buttons.append(btn)

    def generate_bot_button(self, slots):
        btn = Button((0, 255, 255), 800, 500, 100, 30, str("Create " + slots) + " slot bot")
        self.buttons.append(btn)

    def render(self, screen):
        self.generate_bot_button('four')
        self.generate_attack_tool_button()
        self.generate_gather_tool_button()
        self.generate_build_tool_button()
        self.generate_signal_tool_button()
        for button in self.buttons:
            button.draw(screen, (0,0,0))

