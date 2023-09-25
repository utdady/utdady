import random

def calculateWinner(home, away):

    HomeGoals = 0
    AwayGoals = 0

    def testShots(shots):

        Goals = 0

        for shot in shots:
            if random.random() <= shot:
                Goals += 1

        return Goals

    HomeGoals = testShots(home)
    AwayGoals = testShots(away)

    if HomeGoals > AwayGoals:
        return "home"
    elif AwayGoals > HomeGoals:
        return "away"
    else:
        return "draw"

def calculateChance(team1, team2):

    home = 0
    away = 0
    draw = 0

    for i in range(0,10000):
        matchWinner = calculateWinner(team1, team2)
        if matchWinner == "home":
            home += 1
        elif matchWinner == "away":
            away += 1
        else:
            draw += 1

    home = home / 100
    away = away / 100
    draw = draw / 100

    print(f"Home has {home}% chances of winning, Away has {away}% and there is {draw}% chances of a draw")

def main():

    HomexG = [0.21,0.66,0.1,0.14,0.01]
    AwayxG = [0.04,0.06,0.01,0.04,0.06,0.12,0.01,0.06]

    calculateChance(HomexG, AwayxG)

main()
