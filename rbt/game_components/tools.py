#This class represents the tools

class Tools():
    #tool ID counter
    idCounter = 0
    
    def __init__(self, tool_type, pos, bot_owned):
        self.tool_id += 1
        self.tool_type = tool_type
        self.pos = pos
        self.bot_owned = bot_owned
        
