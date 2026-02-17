class CricketPlayer:

    team_name = "India"

    def __init__(self, name, runs):
        self.name = name
        self.runs = runs

p1 = CricketPlayer("Dhoni", 28750)
p2 = CricketPlayer("Kholi", 32470)

print(p1.name, p1.runs)
print(p2.name, p2.runs)

CricketPlayer.team_name = "CSK"

print(p1.name, p1.runs, p1.team_name)
print(p2.name, p2.runs, p2.team_name)
