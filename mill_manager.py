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
    oreToSteel = 10
    fuelToSteel = 10
    steelProduced = 5
    chemist_level = 1
    union_event = False
    fire_event = False
    derail_event = False
    priceDrop_event = False
    priceSpike_event = False

event_weights = {'union': 3, 'fire': 7, 'derail': 5, 'priceDrop': 10, 'priceSpike': 15, 'none': 60}

def create_mill():
    mill = Mill()
    week_counter = 7
    weeks_passed = 0
    labor_cost = 0
    resource_cost = 0
    income = 0
    profit = 0
    day_over = False

    print("Welcome to your Mill")
    print("Money: " + str(mill.money) + " Fuel: " + str(mill.fuel) + " Ore: " + str(mill.ore) + " Steel: " + str(mill.steel) + "\n")

    while mill.money > 0:
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
            if mill.money > mill.rail_cap * mill.fuel_cost:
                buyFuel(mill)
                resource_cost = resource_cost + (mill.rail_cap * mill.fuel_cost)
                day_over = True
            else:
                prCyan("\nInsufficient Funds\n")

        elif action == 2:
            if mill.money > mill.rail_cap * mill.ore_cost:
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
            manageWorkForce(mill)
        else:
            prCyan("\ninvalid action\n")

        if day_over:
            if week_counter > 0:
                week_counter  = week_counter - 1
            else:
                if mill.priceDrop_event == True:
                    mill.ore_cost = mill.ore_cost + 11.5
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
    print("1: Improve furnaces level " + str(mill.furnace_level))
    print("2: Improve rail line capacity level " + str(mill.rail_cap_level))
    print("3: Invest in Metallurgy lab level " + str(mill.metallurgy_level))
    print("4: Invest in Chemist lab level " + str(mill.chemist_level))
    print("5: Return to mill")
    if mill.fire_event == True:
        prEvent("\n10: Put out the fire ")
    if mill.derail_event == True:
        prEvent("\n11: Fix the derailment ")
    
    s = input("Choose your action...")
    action = int(s)
    if action == 1:
        mill.furnace_level = mill.furnace_level + 1
        mill.steelProduced = mill.steelProduced + 2
        mill.money = mill.money - 3000
    elif action == 2:
        mill.rail_cap_level = mill.rail_cap_level + 1
        mill.rail_cap = mill.rail_cap + 5
        mill.money = mill.money - 1000
    elif action == 3:
        mill.metallurgy_level = mill.metallurgy_level + 1
        mill.oreToSteel = mill.oreToSteel - 1.5
        mill.money = mill.money - 1000
    elif action == 4:
        mill.chemist_level = mill.chemist_level + 1
        mill.fuelToSteel = mill.fuelToSteel - 1.5
        mill.money = mill.money - 1000
    elif action == 10:
        mill.money = mill.money - 500
        mill.fire_event = False
    elif action == 11:
        mill.money = mill.money - 1000
        mill.rail_cap = mill.rail_cap + 8.5
        mill.derail_event = False
    else:
        prCyan("\nInvalid Action\n")
    
def manageWorkForce(mill):
    print("\nSelect how you want to manage your workforce: ")
    print("1: adjust total workforce")
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
    if action == 10:
        mill.money = mill.money - 2000
        mill.payRate = mill.payRate - 500
        mill.union_event = False

def percent_return(d):
    val_sum = sum(d.values())
    d_pct = {k: v/val_sum for k, v in d.items()}
    return next(iter(choices(population=list(d_pct), weights=d_pct.values(), k=1)))

def eventGenerator(mill):
    event = percent_return(event_weights)
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
        prEvent("Operating as normal")

def eventHandler(mill):
    if mill.union_event == True:
        prEvent("Your workers are trying to unionize - Labor cost will go up unless you break them up")
        mill.pay_rate = mill.pay_Rate + 500
    elif mill.derail_event == True:
        prEvent("There has been a derailment in the rail yard - You can only use trucks until you fix it")
        mill.rail_cap = mill.rail_cap - 8.5
    elif mill.fire_event == True:
        prEvent("There is a fire on the shop floor - you need to put it out")
    elif mill.priceDrop_event == True:
        prEvent("The Ore market has crashed - take advantage while you can")
        mill.ore_cost = mill.ore_cost - 11.5
    elif mill.priceSpike_event == True:
        prEvent("The market for steel is soaring - take advantage while you can")
        mill.steel_cost = mill.steel_cost + 18.5

def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prEvent(skk): print("\033[46m {}\033[00m" .format(skk))

if __name__ == '__main__':
    create_mill()

