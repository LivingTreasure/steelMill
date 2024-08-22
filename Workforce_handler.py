from utility import prCyan
from utility import prEvent
from Manager_handler import Manager

def manageWorkForce(mill, new_manager):
    print("\nSelect how you want to manage your workforce: ")
    if mill.floor_manager is not None:
        print("Your Manager: " + mill.floor_manager.full_name + " Title: " + mill.floor_manager.title + " Trait: " + mill.floor_manager.trait)
    print("1: adjust total workforce")
    print("2: Hire Manager")
    if mill.union_event == True:
        prEvent("\n10: break up the union $" + str(mill.union_event_cost))
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
        prCyan(new_manager.full_name + " Title: " + new_manager.title + " Trait: " + new_manager.trait + " salary: " + str(new_manager.salary) + "\n")
        s = input("Hire Him? 1: yes 2: no...")
        action = int(s)
        if action == 1:
            if mill.floor_manager is not None:
                mill.old_manager = mill.floor_manager
            current_manager = Manager()
            current_manager.full_name = new_manager.full_name
            current_manager.salary = new_manager.salary
            current_manager.title = new_manager.title
            current_manager.trait = new_manager.trait
            mill.floor_manager = current_manager
            mill.new_manager_flag = True

    elif action == 10:
        if mill.money > mill.union_event_cost:
            mill.money = mill.money - mill.union_event_cost
            mill.payRate = mill.payRate - 500
            mill.union_event = False
        else:
            prCyan("Not enough money\n")
    prCyan("\nMoney: " + str(mill.money) + " Fuel: " + str(mill.fuel) + " Ore: " + str(mill.ore) + " Steel: " + str(mill.steel) + "\n")
