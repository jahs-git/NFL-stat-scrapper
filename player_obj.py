class Player: 

    def __init__(self, name, position, games_played, rushing_attempt, rush_yards, rush_td, rec_targets, receptions, rec_yards, rec_td):
        self.name = name
        self.position = position
        self.games_played = games_played
        self.rushing_attempt = rushing_attempt
        self.rush_yards = rush_yards
        self.rush_td = rush_td
        self.rec_targets = rec_targets
        self.receptions = receptions
        self.rec_yards = rec_yards
        self.rec_td = rec_td

    def print_stats(self):
        if self.position == "RB":
            print(f"{self.position}: {self.name}")
            print(f"games played: {self.games_played}")
            print(f"rushing attemps: {self.rushing_attempt}")
            print(f"rushing yards: {self.rush_yards}")
            print(f"rushing touchdowns: {self.rush_td}")
            print(f"receiving targets: {self.rec_targets}")
            print(f"receiving receptions: {self.receptions}")
            print(f"receiving yards: {self.rec_yards}")
            print(f"receiving touchdowns: {self.rec_td}")
            print()
        else:
            print(f"{self.position}: {self.name}")
            print(f"games played: {self.games_played}")
            print(f"receiving targets: {self.rec_targets}")
            print(f"receiving receptions: {self.receptions}")
            print(f"receiving yards: {self.rec_yards}")
            print(f"receiving touchdowns: {self.rec_td}")
            if self.rushing_attempt > 10:
                print(f"rushing attempts: {self.rushing_attempt}")
                print(f"rushing yards: {self.rush_yards}")
                print(f"rushing touchdowns: {self.rush_td}")

            print()

