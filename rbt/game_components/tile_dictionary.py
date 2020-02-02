

class Tile_Dictionary():
    def __init__(self):
        self.mapTiles = {
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
    }