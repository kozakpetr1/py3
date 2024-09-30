class Game:
    
    def __init__(self, name, game_type, creator):
        self.name = name
        self.game_type = game_type
        self.creator = creator
    
    def set_name(self, new_name):
        self.name = new_name
        
    def get_name(self):
        return self.name
    
g_1 = Game("CsGo","FPS", "Valve")
g_2 = Game("Fortnite", "FPS", "Epic Games")
print(g_2.get_name())