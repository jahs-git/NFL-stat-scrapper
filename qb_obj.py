class QB_Player: 

    def __init__(self, name, position, games_played, completions, attempts, yards, touchdowns, interceptions, rushing_attempt=0, rush_yards=0, rush_td=0):
        self.name = name
        self.position = position
        self.games_played = games_played
        self.completions = completions
        self.attempts = attempts
        self.yards = yards
        self.touchdowns = touchdowns
        self.interceptions = interceptions
        self.rushing_attempt = rushing_attempt
        self.rush_yards = rush_yards
        self.rush_td = rush_td
      
    def print_stats(self):
            print(f"{self.position}: {self.name}")
            print(f"games played: {self.games_played}")
            print(f"completions: {self.completions}")
            print(f"attempts: {self.attempts}")
            print(f"touchdowns: {self.touchdowns}")
            print(f"interceptions: {self.interceptions}")
            print(f"rushing attempts: {self.rushing_attempt}")
            print(f"rushing yards: {self.rush_yards}")
            print(f"rushing touchdowns: {self.rush_td}")
            print()
