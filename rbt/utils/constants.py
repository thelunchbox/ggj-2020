SCREEN_RESOLUTION = (1400, 1050)
MAP_BORDER = 16
MAP_MARGIN = 32
PORT = 3179
MAX_PLAYERS = 1
COLOR = {
    'orange': (255, 128, 0),
    'blue': (0, 0, 255),
    'cyan': (0, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'yellow': (255, 255, 0),
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'magenta': (255, 0, 255)
}

PLAYER_COLORS = {
    1: COLOR['orange'],
    2: COLOR['cyan']
}

STARTING_RESOURCES = 30
SIGNAL_DECAY = 50

CAPACITANCE_DRAIN = 50
RESISTOR_DAMAGE = 50
MAP_WIDTH = 16     # in tiles
MAP_HEIGHT = 16

TILES = [
    [
        11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 0, 11, 11, 11, 11, 11
    ],
    [
        11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 0, 11, 11, 11, 11, 11
    ],
    [
        11, 9, 2, 11, 11, 3, 1, 1, 1, 1, 5, 11, 11, 11, 11, 11
    ],
    [
        11, 0, 0, 11, 3, 5, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11
    ],
    [
        11, 11, 0, 3, 5, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11
    ],
    [
        11, 11, 9, 5, 11, 11, 11, 8, 11, 11, 7, 6, 11, 11, 11, 11
    ],
    [
        11, 11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 10
    ],
    [
        11, 11, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2
    ],
    [
        11, 11, 0, 11, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5
    ],
    [
        11, 11, 0, 11, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2
    ],
    [
        11, 11, 9, 1, 1, 1, 1, 1, 1, 1, 1, 11, 11, 11, 11, 0
    ],
    [
        11, 11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0
    ],
    [
        11, 11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0
    ],
    [
        11, 11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0
    ],
    [
        11, 11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0
    ],
    [
        11, 11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0
    ]
]

#TILE_PATHS = [ "rbt/game_components/T_Path.png","rbt/game_components/L_Turn.png","rbt/game_components/Vertical_Path.png","rbt/game_components/Green_Clear.png" ]

TILE_PATHS = [
    "rbt/images/tiles/Vertical_64.png",
    "rbt/images/tiles/Horizontal_64.png",
    "rbt/images/tiles/L_Turn_64-3.png",
    "rbt/images/tiles/L_Turn_64-2.png",
    "rbt/images/tiles/L_Turn_64-1.png",
    "rbt/images/tiles/L_Turn_64-4.png",
    "rbt/images/tiles/T_Path_64-2.png",
    "rbt/images/tiles/T_Path_64-1.png",
    "rbt/images/tiles/T_Path_64-4.png",
    "rbt/images/tiles/T_Path_64-3.png",
    "rbt/images/tiles/4_Way_64.png",
    "rbt/images/tiles/Blank_64.png"
    ]
