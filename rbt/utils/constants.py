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

STARTING_RESOURCES = 200
STARTING_TTL = 3200
SIGNAL_DECAY = 5

TOOL_COST = 5

TOOL_BUTTON_WIDTH = 200
TOOL_BUTTON_HEIGHT = 50

ATTACK_BUTTON_X = 1040
ATTACK_BUTTON_Y = 0

SIGNAL_BUTTON_X = 1040
SIGNAL_BUTTON_Y = 50

GATHER_BUTTON_X = 1220
GATHER_BUTTON_Y = 0

BUILD_BUTTON_X = 1220
BUILD_BUTTON_Y = 50

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
    11: "blank", #connects none
    12: "northend",
    13: "southend",
    14: "eastend",
    15: "westend"
}

TILE_PATHS = [
    "rbt/images/tiles/goldEdgeTiles/Vertical_64.png",
    "rbt/images/tiles/goldEdgeTiles/Horizontal_64.png",
    "rbt/images/tiles/goldEdgeTiles/L_Turn_64-3.png",
    "rbt/images/tiles/goldEdgeTiles/L_Turn_64-2.png",
    "rbt/images/tiles/goldEdgeTiles/L_Turn_64-1.png",
    "rbt/images/tiles/goldEdgeTiles/L_Turn_64-4.png",
    "rbt/images/tiles/goldEdgeTiles/T_Path_64-2.png",
    "rbt/images/tiles/goldEdgeTiles/T_Path_64-1.png",
    "rbt/images/tiles/goldEdgeTiles/T_Path_64-4.png",
    "rbt/images/tiles/goldEdgeTiles/T_Path_64-3.png",
    "rbt/images/tiles/goldEdgeTiles/4_Way_64.png",
    "rbt/images/tiles/goldEdgeTiles/Blank_64.png",
    "rbt/images/tiles/goldEdgeTiles/Dead_End_64_north.png",
    "rbt/images/tiles/goldEdgeTiles/Dead_End_64_south.png",
    "rbt/images/tiles/goldEdgeTiles/Dead_End_64_east.png",
    "rbt/images/tiles/goldEdgeTiles/Dead_End_64_west.png"
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


TILE_ENTITIES = {
    0: "None",
    1: "Capacitor",
    2: "Resistor",
    3: "Transistor",
    4: "Material",
    5: "Tool",
    6: "Spawn.1",
    7: "Spawn.2"
}
