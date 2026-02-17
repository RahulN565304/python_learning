class FootballPlayer:

    team_name = "Goats"

    def __init__(self, name, goals):
        self.name = name
        self.goals = goals

    def show_details(self):
        print(f"Player-{self.name}, Goals-{self.goals}, Team-{FootballPlayer.team_name}")    

p1 = FootballPlayer("Cristiano Ronaldo", 962)
p2 = FootballPlayer("Lionel Messi", 870)

p1.show_details()
p2.show_details()

FootballPlayer.team_name = "Legends"

p1 = FootballPlayer("Pele", 850)
p2 = FootballPlayer("Maradona", 560)

p1.show_details()
p2.show_details()

