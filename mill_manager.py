import random
from Manager_handler import generateManager
from Manager_handler import setManagerStats
from Manager_handler import Manager
from Event_handler import eventGenerator
from Event_handler import eventHandler
from utility import prCyan
from utility import prEvent
from Workforce_handler import manageWorkForce
from Improvement_handler import improveMill
from Mill import Mill

def create_mill():
    mill = Mill()
    new_manager = Manager()
    generateManager(new_manager)
    week_counter = 7
    weeks_passed = 0
    labor_cost = 0
    resource_cost = 0
    income = 0
    profit = 0
    day_over = False

    prCyan("Welcome to your Mill")
    prCyan("Money: " + str(mill.money) + " Fuel: " + str(mill.fuel) + " Ore: " + str(mill.ore) + " Steel: " + str(mill.steel) + "\n")

    while mill.money >= 0:
        if mill.new_manager_flag:
            print("here")
            setManagerStats(mill.floor_manager, mill)

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
            manageWorkForce(mill, new_manager)
        else:
            prCyan("\ninvalid action\n")

        if day_over:
            if week_counter > 0:
                week_counter  = week_counter - 1
                if week_counter == 0:
                    if mill.floor_manager is not None:
                        prEvent("The week is almost over, your labor will cost: " + str((mill.workers * mill.pay_rate) + mill.floor_manager.salary))
                    else:
                        prEvent("The week is almost over, your labor will cost: " + str(mill.workers * mill.pay_rate))
            else:
                if mill.priceDrop_event == True:
                    mill.ore_cost = mill.ore_cost + 11.5
                generateManager(new_manager)
                mill.steel_cost = random.randint(68, 92)
                week_counter = 7
                weeks_passed = weeks_passed + 1

                if mill.floor_manager is not None:
                    labor_cost = (mill.workers * mill.pay_rate) + mill.floor_manager.salary
                else:
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

if __name__ == '__main__':
    create_mill()
