import random

time_sleep = [0.01, 0.08]

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
    "Crystal Golem": {"damage": 20,"health": 175},
    "Wife": {"damage": 50, "health": 500}
}

player_inventory = [
    {"name": "Healing potion", "amount": 0, "value": 50},
    {"name": "Damage potion", "amount": 0, "value": 25}
]

player_logbook = {
    "Logbook": {"description": "no description"}
}

ingredient_order = []
