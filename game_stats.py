class GameStats():
    def __init__(self, target_settings):
        self.target_settings = target_settings
        self.reset_stats()
        self.game_active = False

        file = open("highest_score.txt", "r")
        self.high_score = file.readline()
        file.close()
        if len(self.high_score) == 0:
            self.high_score = 0
        else:
            self.high_score = int(self.high_score)

    def reset_stats(self):
        self.chances_left = self.target_settings.chances_allowed
        self.score = 0
        
