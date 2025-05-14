import random

# Define a list of 10 fighters with stats
fighters = [
    {"name": "Jake Maverick", "style": "Striker", "striking": 75, "grappling": 68, "stamina": 80, "charisma": 50},
    {"name": "Carlos Gracie", "style": "Grappler", "striking": 60, "grappling": 85, "stamina": 78, "charisma": 45},
    {"name": "Donnie Blaze", "style": "Brawler", "striking": 77, "grappling": 60, "stamina": 72, "charisma": 65},
    {"name": "Leo Fury", "style": "Kickboxer", "striking": 82, "grappling": 70, "stamina": 76, "charisma": 55},
    {"name": "Marco Lin", "style": "Karate", "striking": 80, "grappling": 65, "stamina": 79, "charisma": 60},
    {"name": "Ravi Patel", "style": "Grappler", "striking": 65, "grappling": 82, "stamina": 75, "charisma": 48},
    {"name": "Troy Storm", "style": "Striker", "striking": 78, "grappling": 58, "stamina": 74, "charisma": 52},
    {"name": "Andre King", "style": "Boxer", "striking": 83, "grappling": 55, "stamina": 77, "charisma": 59},
    {"name": "Jin Okada", "style": "Judo", "striking": 66, "grappling": 80, "stamina": 73, "charisma": 47},
    {"name": "Nate Cruz", "style": "Wrestler", "striking": 70, "grappling": 78, "stamina": 76, "charisma": 51}
]

def simulate_fight(f1, f2):
    def score(f):
        return (
            f["striking"] * 0.4 +
            f["grappling"] * 0.4 +
            f["stamina"] * 0.1 +
            f["charisma"] * 0.1 +
            random.uniform(-5, 5)
        )

    score1 = score(f1)
    score2 = score(f2)

    if score1 > score2:
        winner = f1
    else:
        winner = f2

    method = random.choice(["KO", "Submission", "Decision"])
    round_ = random.randint(1, 3)

    print(f"\n📣 Matchup: {f1['name']} ({f1['style']}) vs {f2['name']} ({f2['style']})")
    print(f"🏆 Winner: {winner['name']} by {method} in round {round_}")

# Pick two random fighters and simulate the match
fighter1, fighter2 = random.sample(fighters, 2)
simulate_fight(fighter1, fighter2)

pip install pandas