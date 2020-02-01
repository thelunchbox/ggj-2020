class GameState():
    def __init__(self):
        # list of players (max=2 for now)
        self.players = []
        #TODO: Map object
        #TODO: End Game

    #TODO: Add serializing method
    def getState(self):
        playerStates = []
        for p in self.players:
            playerStates.append(p.getState())

        return {
            "players": playerStates
        }
    
    def isOver()
        return False
    
    #TODO: Add set by game state serialization