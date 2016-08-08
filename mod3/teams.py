def add_games(*teams):
    """
    Creates an entry for the `team` in `TEAMS` dict if it is isn't there
    or increase a number of games of the `team` by 1.
    """

    for team in teams:
        if TEAMS.get(team):
            TEAMS[team]["games"] += 1
        else:
            TEAMS[team] = {"games": 1, "wins": 0, "draws": 0, "defs": 0}


def add_results(team1, score1, team2, score2):
    """
    Increase a number of wins, defs or draws of the teams
    in the `TEAMS` dict depending on results of the game.
    """

    if int(score1) > int(score2):
        TEAMS[team1]["wins"] += 1
        TEAMS[team2]["defs"] += 1

    elif int(score2) > int(score1):
        TEAMS[team2]["wins"] += 1
        TEAMS[team1]["defs"] += 1

    else:
        TEAMS[team1]["draws"] += 1
        TEAMS[team2]["draws"] += 1

TEAMS = {}

for _ in range(int(input())):
    team1, score1, team2, score2 = input().split(";")
    add_games(team1, team2)
    add_results(team1, score1, team2, score2)

for team in TEAMS:
    print("{}:{} {} {} {} {}".format(
        team, TEAMS[team]["games"], TEAMS[team]["wins"],
        TEAMS[team]["draws"], TEAMS[team]["defs"],
        TEAMS[team]["wins"] * 3 + TEAMS[team]["draws"]
    ))
