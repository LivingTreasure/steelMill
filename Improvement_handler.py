from utility import prCyan
from utility import prEvent

def improveMill(mill):
    print("\nSelect a mill improvements: ")
    print("1: Improve furnaces - $"+ str(mill.furnace_level_cost * mill.furnace_level) +"  level " + str(mill.furnace_level))
    print("2: Improve rail line capacity - $"+ str(mill.rail_cap_level_cost * mill.rail_cap_level) +" level " + str(mill.rail_cap_level))
    print("3: Invest in Metallurgy lab - $"+ str(mill.metallurgy_level_cost * mill.metallurgy_level) +" level " + str(mill.metallurgy_level))
    print("4: Invest in Chemist lab - $"+ str(mill.chemist_level_cost * mill.chemist_level) +" level " + str(mill.chemist_level))
    print("5: Return to mill")
    if mill.fire_event == True:
        prEvent("\n10: Put out the fire - $" + str(mill.fire_cost))
    if mill.derail_event == True:
        prEvent("\n11: Fix the derailment - $" + str(mill.derail_cost))
    
    s = input("Choose your action...")
    action = int(s)
    if action == 1:
        if mill.money > (mill.furnace_level_cost * mill.furnace_level):
            mill.money = mill.money - (mill.furnace_level_cost * mill.furnace_level)
            mill.furnace_level = mill.furnace_level + 1
            mill.steelProduced = mill.steelProduced + 2
        else:
            prCyan("Not enough money\n")
    elif action == 2:
        if mill.money > (mill.rail_cap_level_cost * mill.rail_cap_level):
            mill.money = mill.money - (mill.rail_cap_level_cost * mill.rail_cap_level)
            mill.rail_cap_level = mill.rail_cap_level + 1
            mill.rail_cap = mill.rail_cap + 5
        else:
            prCyan("Not enough money\n")
    elif action == 3:
        if mill.money > (mill.metallurgy_level_cost * mill.metallurgy_level):
            mill.money = mill.money - (mill.metallurgy_level_cost * mill.metallurgy_level)
            mill.metallurgy_level = mill.metallurgy_level + 1
            mill.oreToSteel = mill.oreToSteel - 1.5
        else:
            prCyan("Not enough money\n")
    elif action == 4:
        if mill.money > (mill.chemist_level_cost * mill.chemist_level):
            mill.money = mill.money - (mill.chemist_level_cost * mill.chemist_level)
            mill.chemist_level = mill.chemist_level + 1
            mill.fuelToSteel = mill.fuelToSteel - 2
        else:
            prCyan("Not enough money\n")
    elif action == 10:
        if mill.money > mill.fire_cost:
            mill.money = mill.money - mill.fire_cost
            mill.fire_event = False
        else:
            prCyan("Not enough money\n")
    elif action == 11:
        if mill.money > mill.derail_cost:
            mill.money = mill.money - mill.derail_cost
            mill.rail_cap = mill.rail_cap + mill.derail_amount_arch
            mill.derail_event = False
        else:
            prCyan("Not enough money\n")
    else:
        prCyan("\nInvalid Action\n")
    
    prCyan("\nMoney: " + str(mill.money) + " Fuel: " + str(mill.fuel) + " Ore: " + str(mill.ore) + " Steel billets: " + str(mill.billets) + " Steel blooms: " + str(mill.blooms) + " Steel slabs: " + str(mill.slabs))
    

