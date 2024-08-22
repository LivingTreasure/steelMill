import random

class Manager:
    first_name = ['James', 'Thomas', 'Harold', 'Henry', 'Arnold', 'Andrew', 'Lewis', 'Gareth', 'Winston', 'Leo', 'William', 'Richard', 'Faftmoza', 'Doet', 'Cacul', 'Krug', 'Frederick']
    last_name = ['Stewart', 'Fitzgerald', 'Frick', 'Smith', 'Yoder', 'La Rusu', 'Henderson', 'Joe', 'Stevens', 'Williams', 'Caculson', 'Standley']
    full_name = None
    title = None
    trait = None
    salary = None
    title_list = ['Steel Worker', 'Chemist', 'Metalurgist', 'Trucker', 'Union Buster', 'Miner', 'Salesman', 'Monopolizer', 'Fire Fighter']
    trait_list = ['Lazy', 'over achiver', 'clumsy', 'union sympathizer', 'organized', 'perfectionist', 'efficient']

def generateManager (floor_manager):
    floor_manager.full_name = random.choice(floor_manager.first_name) + " " + random.choice(floor_manager.last_name)
    floor_manager.title = random.choice(floor_manager.title_list)
    floor_manager.trait = random.choice(floor_manager.trait_list)
    floor_manager.salary = random.randint(40, 200)

def setManagerStats(manager, mill):
    mill.new_manager_flag = False
    print(manager.full_name)
    if manager.title == 'Steel Worker':
        mill.fuel_cost = mill.fuel_cost - 2
        mill.ore_cost = mill.ore_cost - 1
        mill.steel_cost = mill.steel_cost + 3
        mill.furnace_level_cost = mill.furnace_level_cost - 300
    elif manager.title == 'Chemist':
        mill.fuel_cost = mill.fuel_cost - 4
        mill.chemist_level_cost = mill.chemist_level_cost - 300
    elif manager.title == 'Metalurgist':
        mill.ore_cost = mill.ore_cost - 3
        mill.metallurgy_level_cost = mill.metallurgy_level_cost - 300
    elif manager.title == 'Trucker':
        mill.derail_cost = mill.derail_cost - 500
        mill.derail_amount = mill.derail_amount - 5
        mill.derail_percent = mill.derail_percent - 2
        mill.noEvent_percent = mill.noEvent_percent + 2
        mill.rail_cap = mill.rail_cap + 2
    elif manager.title == 'Union Buster':
        mill.union_event_cost = mill.union_event_cost - 1000
        mill.union_percent = mill.union_percent - 1
        mill.noEvent_percent = mill.noEvent_percent + 1
        mill.pay_rate = mill.pay_rate - 150
    elif manager.title == 'Miner':
        mill.priceDrop_percent = mill.priceDrop_percent + 5
        mill.noEvent_percent = mill.noEvent_percent - 5
        mill.fuel_cost = mill.fuel_cost - 2
        mill.ore_cost = mill.ore_cost - 2
    elif manager.title == 'Salesman':
        mill.priceSpike_percent = mill.priceSpike_percent + 7
        mill.noEvent_percent = mill.noEvent_percent - 7
        mill.steel_cost = mill.steel_cost + 3
    elif manager.title == 'Monopolizer':
        mill.steel_cost = mill.steel_cost + 5
    elif manager.title == 'Fire Fighter':
        mill.fire_cost = mill.fire_cost - 300
        mill.fire_percent = mill.fire_percent - 5
        mill.noEvent_percent = mill.noEvent_percent + 5
        mill.fuel_cost = mill.fuel_cost - 1

    if mill.old_manager is not None:
        mill.old_manager.full_name
        if mill.old_manager.title == 'Steel Worker':
            mill.fuel_cost = mill.fuel_cost + 2
            mill.ore_cost = mill.ore_cost + 1
            mill.steel_cost = mill.steel_cost - 3
            mill.furnace_level_cost = mill.furnace_level_cost + 300
        elif mill.old_manager.title == 'Chemist':
            mill.fuel_cost = mill.fuel_cost + 4
            mill.chemist_level_cost = mill.chemist_level_cost + 300
        elif mill.old_manager.title == 'Metalurgist':
            mill.ore_cost = mill.ore_cost + 3
            mill.metallurgy_level_cost = mill.metallurgy_level_cost + 300
        elif mill.old_manager.title == 'Trucker':
            mill.derail_cost = mill.derail_cost + 500
            mill.derail_amount = mill.derail_amount + 5
            mill.derail_percent = mill.derail_percent + 2
            mill.noEvent_percent = mill.noEvent_percent - 2
            mill.rail_cap = mill.rail_cap - 2
        elif mill.old_manager.title == 'Union Buster':
            mill.union_event_cost = mill.union_event_cost + 1000
            mill.union_percent = mill.union_percent + 1
            mill.noEvent_percent = mill.noEvent_percent - 1
            mill.pay_rate = mill.pay_rate + 150
        elif mill.old_manager.title == 'Miner':
            mill.priceDrop_percent = mill.priceDrop_percent - 5
            mill.noEvent_percent = mill.noEvent_percent + 5
            mill.fuel_cost = mill.fuel_cost + 2
            mill.ore_cost = mill.ore_cost + 2
        elif mill.old_manager.title == 'Salesman':
            mill.priceSpike_percent = mill.priceSpike_percent - 7
            mill.noEvent_percent = mill.noEvent_percent + 7
            mill.steel_cost = mill.steel_cost - 3
        elif mill.old_manager.title == 'Monopolizer':
            mill.steel_cost = mill.steel_cost - 5
        elif mill.old_manager.title == 'Fire Fighter':
            mill.fire_cost = mill.fire_cost + 300
            mill.fire_percent = mill.fire_percent + 5
            mill.noEvent_percent = mill.noEvent_percent - 5
            mill.fuel_cost = mill.fuel_cost + 1

    manager.trait
