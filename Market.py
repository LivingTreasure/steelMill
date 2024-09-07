from utility import prCyan
from utility import prEvent

class Market:
    fuel_cost = 10
    ore_cost = 20
    billet_cost = 72.5
    bloom_cost = 72.5
    slab_cost = 72.5
    resource_cost = 0
 

def steel_market(mill, market):
    day_over = True
    print("\n1: Sell  " + str(mill.rail_cap) + " tons of Steel Billets - " + str(mill.rail_cap * market.billet_cost))
    print("2: Sell  " + str(mill.rail_cap) + " tons of Steel Blooms - " + str(mill.rail_cap * market.bloom_cost))
    print("3: Sell  " + str(mill.rail_cap) + " tons of Steel Slabs - " + str(mill.rail_cap * market.slab_cost))
    print("4: Buy " + str(mill.rail_cap) + " tons Fuel for $" + str(mill.rail_cap * market.fuel_cost))
    print("5: Buy " + str(mill.rail_cap) + " tons ore for $" + str(mill.rail_cap * market.ore_cost))

    s = input("Choose your action...")
    action = int(s)
    if action == 4:
        if mill.money >= mill.rail_cap * market.fuel_cost:
            buyFuel(mill, market)
            market.resource_cost = market.resource_cost + (mill.rail_cap * market.fuel_cost)
        else:
            prCyan("\nInsufficient Funds\n")
            day_over = False

    elif action == 5:
        if mill.money >= mill.rail_cap * market.ore_cost:
            buyOre(mill, market)
            market.resource_cost = market.resource_cost + (mill.rail_cap * market.ore_cost)
        else:
            prCyan("\nInsufficient Funds\n")
            day_over = False

    elif action == 3:
        if mill.slabs > mill.rail_cap:
            sell_Slab(mill, market)
        else:
            prCyan("\nInsufficient Resources\n")
            day_over = False

    elif action == 2:
        if mill.blooms >= mill.rail_cap:
            sell_Bloom(mill, market)
        else:
            prCyan("\nInsufficient Resources\n")
            day_over = False

    elif action == 1:
        if mill.billets >= mill.rail_cap:
            sell_Billet(mill, market)
        else:
            prCyan("\nInsufficient Resources\n")
            day_over = False
    else:
        prCyan("\ninvalid action\n")

    return day_over

def sell_Billet(mill, market):
    mill.money = mill.money + (mill.rail_cap * market.billet_cost)
    mill.billets = mill.billets - mill.rail_cap

def sell_Bloom(mill, market):
    mill.money = mill.money + (mill.rail_cap * market.bloom_cost)
    mill.blooms = mill.blooms - mill.rail_cap

def sell_Slab(mill, market):
    mill.money = mill.money + (mill.rail_cap * market.slab_cost)
    mill.slabs = mill.slabs - mill.rail_cap

def buyFuel(mill, market):
    mill.money = mill.money - (mill.rail_cap * market.fuel_cost)
    mill.fuel = mill.fuel + mill.rail_cap

def buyOre(mill, market):
    mill.money = mill.money - (mill.rail_cap * market.ore_cost)
    mill.ore = mill.ore + mill.rail_cap

