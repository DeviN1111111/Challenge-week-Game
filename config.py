import random

time_sleep = [0,0]

weapons = [
    {"name": "Fist", "damage": 20},
    {"name": "Dagger", "damage": 20},
    {"name": "Bow", "damage": 40}
]

player_stats = {
    "name": "no_name_entered",
    "health": 100,
    "weapon": "Fist",
}

enemy_stats = {
    "Zombie": {"damage": 5, "health": 50},
    "Skeleton": {"damage": 7, "health": 40},
    "Vampire": {"damage": 10, "health": 60}
}