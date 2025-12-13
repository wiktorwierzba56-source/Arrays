# Prints popular computer games, numbered and sorted

computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# sort alphabetically
computer_games.sort()

# print using while loop
i = 0
number = 1

while i < len(computer_games):
    print(number, computer_games[i])
    i += 1
    number += 1
