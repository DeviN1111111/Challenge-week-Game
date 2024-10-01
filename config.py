import random

time_sleep = [0.02,0.01]

weapons = [
    {"name": "Fist", "damage": 5},
    {"name": "Dagger", "damage": 20},
    {"name": "Bow", "damage": 40}
]

player_stats = {
    "name": "no_name_entered",
    "health": 100,
    "weapon": "Fist",
}

enemy_stats = {
    "Zombie": {"damage": 7, "health": 50},
    "Skeleton": {"damage": 12, "health": 60},
    "Vampire": {"damage": 10, "health": 90}
}

player_inventory = [
    {"name": "Healing potion", "amount": 1, "value": 50},
    {"name": "Damage potion", "amount": 1, "value": 19}
]