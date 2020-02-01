class GameState():
    def __init__(self):
        # list of players (max=2 for now)
        self.players = {}
        #TODO: Map object
        #TODO: End Game

    #TODO: Add serializing method
    def getState(self):
        playerStates = {}
        for p in self.players.values():
            playerStates[str(p.id)] = p.getState()

        return {
            "players": playerStates
        }
    
    def isOver(self):
        return False

    def update(self):
        pass
    
    #TODO: Add set by game state serialization

    def render(self, screen):
        for p in self.players.values():
            p.render(screen)