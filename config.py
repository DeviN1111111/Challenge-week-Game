import random

time_sleep = [0.0001, 0.0002]

weapons = [
    {"name": "Fist", "damage": 10},
    {"name": "Dagger", "damage": 20},
    {"name": "Shortsword", "damage": 30}
]

player_stats = {
    "name": "no_name_entered",
    "health": 100,
    "weapon": "Fist",
}

enemy_stats = {
    "Zombie": {"damage": 5, "health": 50},
    "Skeleton": {"damage": 12, "health": 60},
    "Vampire": {"damage": 10, "health": 90},
    "Crystal Golem": {"damage": 15,"health": 100}
}

player_inventory = [
    {"name": "Healing potion", "amount": 1, "value": 50},
    {"name": "Damage potion", "amount": 1, "value": 25}
]

player_logbook = {
    "Logbook": {"description": "no description"}
}