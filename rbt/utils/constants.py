SCREEN_RESOLUTION = (1400, 1050)
MAP_BORDER = 16
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

STARTING_RESOURCES = 60
STARTING_TTL = 3200
SIGNAL_DECAY = 5

TOOL_COST = 5

CAPACITANCE_DRAIN = 50
RESISTOR_DAMAGE = 50
MAP_WIDTH = 16     # in tiles
MAP_HEIGHT = 16

TICK_RATE = 4000000

SPAWN_POINTS = [
    [(0,0), 1],
    [(1,0), 1],
    [(2,0), 1],
    [(3,0), 1],
    [(0,15), 2],
    [(1,15), 2],
    [(2,15), 2],
    [(3,15), 2]
]

TILE_WIDTH  = 64
TILE_HEIGHT = 64

TILES = [
    [ 11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 0, 11, 11, 11, 11, 1 ],
    [ 11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 0, 11, 11, 11, 11, 1 ],
    [ 11, 9, 2, 11, 11, 3, 1, 1, 1, 1, 5, 11, 11, 11, 11, 1 ],
    [ 11, 0, 0, 11, 3, 5, 11, 11, 11, 11, 11, 11, 11, 11, 11, 1 ],
    [ 11, 11, 0, 3, 5, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 1 ],
    [ 11, 11, 9, 5, 11, 11, 11, 8, 11, 11, 7, 6, 11, 11, 11, 1 ],
    [ 11, 11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 1 ],
    [ 11, 11, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2 ],
    [ 11, 11, 0, 11, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5 ],
    [ 11, 11, 0, 11, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2 ],
    [ 11, 11, 9, 1, 1, 1, 1, 1, 1, 1, 1, 11, 11, 11, 11, 0 ],
    [ 11, 11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0 ],
    [ 11, 11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0 ],
    [ 11, 11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0 ],
    [ 11, 11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0 ],
    [ 11, 11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0  ]
]

TILE_MAP = {
    0: "vertical",
    1: "horizontal",
    2: "southwest", # connects south and west
    3: "southeast",
    4: "northeast",
    5: "northwest",
    6: "trinorth", # connects every direction except south
    7: "triwest",
    8: "trisouth",
    9: "trieast",
    10: "clover", # connects all
    11: "blank" #connects none
    12: "northend" #connects none
    13: "southend" #connects none
    14: "eastend" #connects none
    15: "westend" #connects none
}

TILE_PATHS = [
    "rbt/images/tiles/original/Vertical_64.png",
    "rbt/images/tiles/original/Horizontal_64.png",
    "rbt/images/tiles/original/L_Turn_64-3.png",
    "rbt/images/tiles/original/L_Turn_64-2.png",
    "rbt/images/tiles/original/L_Turn_64-1.png",
    "rbt/images/tiles/original/L_Turn_64-4.png",
    "rbt/images/tiles/original/T_Path_64-2.png",
    "rbt/images/tiles/original/T_Path_64-1.png",
    "rbt/images/tiles/original/T_Path_64-4.png",
    "rbt/images/tiles/original/T_Path_64-3.png",
    "rbt/images/tiles/original/4_Way_64.png",
    "rbt/images/tiles/original/Dead_End_64_north.png",
    "rbt/images/tiles/original/Dead_End_64_south.png",
    "rbt/images/tiles/original/Dead_End_64_east.png",
    "rbt/images/tiles/original/Dead_End_64_west.png"
]

TILE_EXITS = [
    ["north", "south"],
    ["east", "west"],
    ["west", "south"],
    ["south", "east"],
    ["north", "east"],
    ["north", "west"],
    ["north", "west", "east"],
    ["west", "north", "south"],
    ["south", "west", "east"],
    ["east", "north", "south"],
    ["east", "north", "south", "west"],
    [],
    ["north"],
    ["south"],
    ["east"],
    ["west"]
]