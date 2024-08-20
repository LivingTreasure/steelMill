import random
from random import choices

class Mill:
    money = 1000
    fuel = 200
    ore = 100
    steel = 0
    workers = 1
    quality = 5
    rail_cap = 10
    pay_rate = 650
    fuel_cost = 10
    ore_cost = 20
    steel_cost = 72.5
    furnace_level = 1
    rail_cap_level = 1
    metallurgy_level = 1
    union_favor = 0
    oreToSteel = 10
    fuelToSteel = 10
    steelProduced = 5
    chemist_level = 1
    union_event = False
    fire_event = False
    derail_event = False
    priceDrop_event = False
    priceSpike_event = False
    priceSpike_percent = 15
    union_percent = 3
    fire_percent = 7
    priceDrop_percent = 10
    noEvent_percent = 60
    derail_percent = 5
    event_weights = {'union': union_percent, 'fire': fire_percent, 'derail': derail_percent, 'priceDrop': priceDrop_percent, 'priceSpike': priceSpike_percent, 'none': noEvent_percent}
    floor_manager = None

class Manager:
    first_name = ['James', 'Thomas', 'Harold', 'Henry', 'Arnold', 'Andrew', 'Lewis', 'Gareth', 'Winston', 'Leo', 'William', 'Richard', 'Faftmoza', 'Doet', 'Cacul', 'Krug', 'Frederick']
    last_name = ['Stewart', 'Fitzgerald', 'Frick', 'Smith', 'Yoder', 'La Rusu', 'Henderson', 'Joe', 'Stevens', 'Williams', 'Caculson', 'Standley']
    full_name = None
    title = None
    trait = None
    salary = None
    title_list = ['Steel Worker', 'Chemist', 'Metalurgist', 'Trucker', 'Union Buster', 'Miner', 'Salesman', 'Monopolizer']
    trait_list = ['Lazy', 'over achiver', 'clumsy', 'union sympathizer', 'organized', 'perfectionist', 'efficient']

def create_mill():
    mill = Mill()
    floor_manager = Manager()
    generateManager(floor_manager)
    week_counter = 7
    weeks_passed = 0
    labor_cost = 0
    resource_cost = 0
    income = 0
    profit = 0
    day_over = False

    print("Welcome to your Mill")
    print("Money: " + str(mill.money) + " Fuel: " + str(mill.fuel) + " Ore: " + str(mill.ore) + " Steel: " + str(mill.steel) + "\n")

    while mill.money >= 0:
        day_over = False
        print("1: Buy " + str(mill.rail_cap) + " tons Fuel for $" + str(mill.rail_cap * mill.fuel_cost))
        print("2: Buy " + str(mill.rail_cap) + "  tons ore for $" + str(mill.rail_cap * mill.ore_cost))
        print("3: Sell " + str(mill.rail_cap) + "  tons Steel for $" + str(mill.rail_cap * mill.steel_cost))
        print("4: Forge " + str(mill.steelProduced * mill.workers) + " tons of steel with " + str(mill.oreToSteel * mill.workers) + " tons ore " + str(mill.fuelToSteel * mill.workers) + " tons fuel")
        print("5: Improve Mill")
        print("6: manage work force")

        while True:
            s = input("Choose your action...")
            try:
                action = int(s)
                break
            except ValueError:
                print("invalid input, must be a numeric option!")
                continue

        if action == 1:
            if mill.money >= mill.rail_cap * mill.fuel_cost:
                buyFuel(mill)
                resource_cost = resource_cost + (mill.rail_cap * mill.fuel_cost)
                day_over = True
            else:
                prCyan("\nInsufficient Funds\n")

        elif action == 2:
            if mill.money >= mill.rail_cap * mill.ore_cost:
                buyOre(mill)
                resource_cost = resource_cost + (mill.rail_cap * mill.ore_cost)
                day_over = True
            else:
                prCyan("\nInsufficient Funds\n")

        elif action == 3:
            if mill.steel >= mill.rail_cap:
                sellSteel(mill)
                income = income + (mill.rail_cap * mill.steel_cost)
                day_over = True
            else:
                prCyan("\nInsufficient amount of Steel\n")

        elif action == 4:
            if mill.fuel >= (mill.fuelToSteel * mill.workers) and mill.ore >= (mill.oreToSteel * mill.workers):
                createSteel(mill)
                day_over = True
            else:
                prCyan("\nInsufficient Resources\n")

        elif action == 5:
            improveMill(mill)
        elif action == 6:
            manageWorkForce(mill, floor_manager)
        else:
            prCyan("\ninvalid action\n")

        if day_over:
            if week_counter > 0:
                week_counter  = week_counter - 1
                if week_counter == 0:
                    prEvent("The week is almost over, your labor will cost: " + str(mill.workers * mill.pay_rate))
            else:
                if mill.priceDrop_event == True:
                    mill.ore_cost = mill.ore_cost + 11.5
                generateManager(floor_manager)
                mill.steel_cost = random.randint(68, 92)
                week_counter = 7
                weeks_passed = weeks_passed + 1
                labor_cost = mill.workers * mill.pay_rate
                profit = income - (labor_cost + resource_cost)
                mill.money = mill.money - (labor_cost)
                prCyan("\nthe week is over, Labor costs: " + str(labor_cost) + "\nResource cost:" + str(resource_cost) + "\nincome total:" + str(income) + "\nprofit total:" + str(profit))
                income = 0
                resource_cost = 0
                labor_cost = 0
                mill.priceDrop_event = False
                mill.priceSpike_event = False
                eventGenerator(mill)
                eventHandler(mill)

            prCyan("\nMoney: " + str(mill.money) + " Fuel: " + str(mill.fuel) + " Ore: " + str(mill.ore) + " Steel: " + str(mill.steel))
            prCyan("Days left in the week: " + str(week_counter) + " weeks passed: " + str(weeks_passed) + "\n")
    print("Your mill ran out of money")

def buyFuel(mill):
    mill.money = mill.money - (mill.rail_cap * mill.fuel_cost)
    mill.fuel = mill.fuel + mill.rail_cap

def buyOre(mill):
    mill.money = mill.money - (mill.rail_cap * mill.ore_cost)
    mill.ore = mill.ore + mill.rail_cap

def sellSteel(mill):
    mill.money = mill.money + (mill.rail_cap * mill.steel_cost)
    mill.steel = mill.steel - mill.rail_cap
def createSteel(mill):
    mill.ore = mill.ore - (mill.oreToSteel * mill.workers)
    mill.fuel = mill.fuel - (mill.fuelToSteel * mill.workers)
    mill.steel = mill.steel + (mill.steelProduced * mill.workers)

def improveMill(mill):
    print("\nSelect a mill improvements: ")
    print("1: Improve furnaces - $"+ str(3000 * mill.furnace_level) +"  level " + str(mill.furnace_level))
    print("2: Improve rail line capacity - $"+ str(1000 * mill.rail_cap_level) +" level " + str(mill.rail_cap_level))
    print("3: Invest in Metallurgy lab - $"+ str(1000 * mill.metallurgy_level) +" level " + str(mill.metallurgy_level))
    print("4: Invest in Chemist lab - $"+ str(700 * mill.chemist_level) +" level " + str(mill.chemist_level))
    print("5: Return to mill")
    if mill.fire_event == True:
        prEvent("\n10: Put out the fire - $500")
    if mill.derail_event == True:
        prEvent("\n11: Fix the derailment - $1000")
    
    s = input("Choose your action...")
    action = int(s)
    if action == 1:
        if mill.money > (3000 * mill.furnace_level):
            mill.money = mill.money - (3000 * mill.furnace_level)
            mill.furnace_level = mill.furnace_level + 1
            mill.steelProduced = mill.steelProduced + 2
        else:
            prCyan("Not enough money\n")
    elif action == 2:
        if mill.money > (1000 * mill.rail_cap_level):
            mill.money = mill.money - (1000 * mill.rail_cap_level)
            mill.rail_cap_level = mill.rail_cap_level + 1
            mill.rail_cap = mill.rail_cap + 5
        else:
            prCyan("Not enough money\n")
    elif action == 3:
        if mill.money > (1000 * mill.metallurgy_level):
            mill.money = mill.money - (1000 * mill.metallurgy_level)
            mill.metallurgy_level = mill.metallurgy_level + 1
            mill.oreToSteel = mill.oreToSteel - 1.5
        else:
            prCyan("Not enough money\n")
    elif action == 4:
        if mill.money > (700 * mill.chemist_level):
            mill.money = mill.money - (700 * mill.chemist_level)
            mill.chemist_level = mill.chemist_level + 1
            mill.fuelToSteel = mill.fuelToSteel - 2
        else:
            prCyan("Not enough money\n")
    elif action == 10:
        if mill.money > 500:
            mill.money = mill.money - 500
            mill.fire_event = False
        else:
            prCyan("Not enough money\n")
    elif action == 11:
        if mill.money > 1000:
            mill.money = mill.money - 1000
            mill.rail_cap = mill.rail_cap + 8.5
            mill.derail_event = False
        else:
            prCyan("Not enough money\n")
    else:
        prCyan("\nInvalid Action\n")
    
    prCyan("\nMoney: " + str(mill.money) + " Fuel: " + str(mill.fuel) + " Ore: " + str(mill.ore) + " Steel: " + str(mill.steel) + "\n")
    
def manageWorkForce(mill, floor_manager):
    print("\nSelect how you want to manage your workforce: ")
    if mill.floor_manager is not None:
        print("Your Manager: " + mill.floor_manager.full_name + " Title: " + mill.floor_manager.title + " Trait: " + mill.floor_manager.trait)
    print("1: adjust total workforce")
    print("2: Hire Manager")
    if mill.union_event == True:
        prEvent("\n10: break up the union $2000")
    s = input("Choose your action...")
    action = int(s)

    if action == 1:
        print("\nWhat percentage of the workforce do you want to maintain?")
        s = input("enter pertentage (1 - 100)...")
        if int(s) > 0 and int(s) < 101:
            mill.workers = int(s)/100
        else:
            print("invalid percentage")
    elif action == 2:
        prCyan("\navailable Manager: ")
        prCyan(floor_manager.full_name + " Title: " + floor_manager.title + " Trait: " + floor_manager.trait + " salary: " + str(floor_manager.salary) + "\n")
        s = input("Hire Him? 1: yes 2: no...")
        action = int(s)
        if action == 1:
            mill.floor_manager = floor_manager

    elif action == 10:
        mill.money = mill.money - 2000
        mill.payRate = mill.payRate - 500
        mill.union_event = False
    prCyan("\nMoney: " + str(mill.money) + " Fuel: " + str(mill.fuel) + " Ore: " + str(mill.ore) + " Steel: " + str(mill.steel) + "\n")

def percent_return(d):
    val_sum = sum(d.values())
    d_pct = {k: v/val_sum for k, v in d.items()}
    return next(iter(choices(population=list(d_pct), weights=d_pct.values(), k=1)))

def eventGenerator(mill):
    event = percent_return(mill.event_weights)
    if event == "union":
        mill.union_event = True
        prEvent("Workers are trying to unionize")
    elif event =="derail":
        mill.derail_event = True
        prEvent("Train derailment")
    elif event =="fire":
        mill.fire_event = True
        prEvent("Fire")
    elif event =="priceDrop":
        mill.priceDrop_event = True
        prEvent("Ore price drop")
    elif event =="priceSpike":
        mill.priceSpike_event = True
        prEvent("Steel price spike")
    elif event == "none":
        prEvent("No New Events")

def eventHandler(mill):
    if mill.union_event == True:
        prEvent("Your workers are trying to unionize - Labor cost will go up unless you break them up")
        mill.pay_rate = mill.pay_rate + 500
    if mill.derail_event == True:
        prEvent("There has been a derailment in the rail yard - You can only use trucks until you fix it")
        if mill.rail_cap > 9:
            mill.rail_cap = mill.rail_cap - 8.5
    if mill.fire_event == True:
        prEvent("There is a fire on the shop floor - you need to put it out")
    if mill.priceDrop_event == True:
        prEvent("The Ore market has crashed - take advantage while you can")
        mill.ore_cost = mill.ore_cost - 11.5
    if mill.priceSpike_event == True:
        prEvent("The market for steel is soaring - take advantage while you can")
        mill.steel_cost = mill.steel_cost + 35

def generateManager (floor_manager):
    floor_manager.full_name = random.choice(floor_manager.first_name) + " " + random.choice(floor_manager.last_name)
    floor_manager.title = random.choice(floor_manager.title_list)
    floor_manager.trait = random.choice(floor_manager.trait_list)
    floor_manager.salary = random.randint(40, 200)

def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prEvent(skk): print("\033[46m {}\033[00m" .format(skk))

if __name__ == '__main__':
    create_mill()


