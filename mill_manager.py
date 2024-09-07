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
from Market import Market
from Market import steel_market
from Workshop import workshop

def create_mill():
    mill = Mill()
    new_manager = Manager()
    market = Market()
    generateManager(new_manager)
    week_counter = 7
    weeks_passed = 0
    labor_cost = 0
    income = 0
    profit = 0

    prCyan("Welcome to your Mill")
    prCyan("Money: " + str(mill.money) + " Fuel: " + str(mill.fuel) + " Ore: " + str(mill.ore) + " Steel: " + str(mill.billets) + "\n")

    while mill.money >= 0:
        if mill.new_manager_flag:
            print("here")
            setManagerStats(mill.floor_manager, mill, market)

        print("1: Enter Market")
        print("2: Enter Workshop")
        print("3: Improve Mill")
        print("4: manage work force")
        print("100: Skip day")

        while True:
            s = input("Choose your action...")
            try:
                action = int(s)
                break
            except ValueError:
                print("invalid input, must be a numeric option!")
                continue

        if action == 1:
            mill.day_over = steel_market(mill, market) + mill.day_over
        elif action == 2:
            mill.day_over = workshop(mill) + mill.day_over
        elif action == 3:
            improveMill(mill)
        elif action == 4:
            manageWorkForce(mill, new_manager)
        elif action == 100:
            prCyan("\nThe day Passes\n")
            mill.day_over = mill.day_over + 2
        else:
            prCyan("\ninvalid action\n")

        print(mill.day_over)
        if mill.day_over >= 2:
                mill.day_over = 0
                if week_counter > 0:
                    week_counter  = week_counter - 1
                    if week_counter == 0:
                        if mill.floor_manager is not None:
                            prEvent("The week is almost over, your labor will cost: " + str((mill.workers * mill.pay_rate) + mill.floor_manager.salary))
                        else:
                            prEvent("The week is almost over, your labor will cost: " + str(mill.workers * mill.pay_rate))
                else:
                    if mill.priceDrop_event == True:
                        market.ore_cost = market.ore_cost + 11.5
                    generateManager(new_manager)
                    market.billet_cost = random.randint(68, 92)
                    market.bloom_cost = random.randint(68, 92)
                    market.slab_cost = random.randint(68, 92)
                    market.ore_cost = random.randint(17, 23)
                    market.fuel_cost = random.randint(8, 12)

                    if mill.floor_manager is not None:
                        labor_cost = (mill.workers * mill.pay_rate) + mill.floor_manager.salary
                    else:
                        labor_cost = mill.workers * mill.pay_rate

                    profit = income - (labor_cost + market.resource_cost)
                    mill.money = mill.money - (labor_cost)
                    prCyan("\nthe week is over, Labor costs: " + str(labor_cost) + "\nResource cost:" + str(market.resource_cost) + "\nincome total:" + str(income) + "\nprofit total:" + str(profit))
                    
                    week_counter = 7
                    weeks_passed = weeks_passed + 1
                    income = 0
                    market.resource_cost = 0
                    labor_cost = 0
                    mill.priceDrop_event = False
                    mill.priceSpike_event = False
                    eventGenerator(mill)
                    eventHandler(mill, market)

                prCyan("\nMarket update: billet: " + str(market.billet_cost) + " bloom: " + str(market.bloom_cost) + " slab: " + str(market.slab_cost))
                prCyan("\nMoney: " + str(mill.money) + " Fuel: " + str(mill.fuel) + " Ore: " + str(mill.ore) + " Steel billets: " + str(mill.billets) + " Steel blooms: " + str(mill.blooms) + " Steel slabs: " + str(mill.slabs))
                prCyan("Days left in the week: " + str(week_counter) + " weeks passed: " + str(weeks_passed) + "\n")
        else:
            prEvent("\nThe day is half over")
            prCyan("\nMoney: " + str(mill.money) + " Fuel: " + str(mill.fuel) + " Ore: " + str(mill.ore) + " Steel billets: " + str(mill.billets) + " Steel blooms: " + str(mill.blooms) + " Steel slabs: " + str(mill.slabs))
            
    print("Your mill ran out of money")

if __name__ == '__main__':
    create_mill()

