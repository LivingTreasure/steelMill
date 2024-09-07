from utility import prCyan
from utility import prEvent

def workshop(mill):
    day_over = True

    print("\n1: Forge " + str(mill.steelProduced * mill.workers) + " tons of steel billets with " + str(mill.oreToSteel * mill.workers) + " tons ore " + str(mill.fuelToSteel * mill.workers) + " tons fuel")
    print("2: Forge " + str(mill.steelProduced * mill.workers) + " tons of steel blooms with " + str(mill.oreToSteel * mill.workers) + " tons ore " + str(mill.fuelToSteel * mill.workers) + " tons fuel")    
    print("3: Forge " + str(mill.steelProduced * mill.workers) + " tons of steel slabs with " + str(mill.oreToSteel * mill.workers) + " tons ore " + str(mill.fuelToSteel * mill.workers) + " tons fuel")

    s = input("Choose your action...")
    action = int(s)
    if action == 1:
                if mill.fuel >= (mill.fuelToSteel * mill.workers) and mill.ore >= (mill.oreToSteel * mill.workers):
                    forge_billets(mill)
                else:
                    day_over = False
                    prCyan("\nInsufficient Resources\n")

    elif action == 2:
            if mill.fuel >= (mill.fuelToSteel * mill.workers) and mill.ore >= (mill.oreToSteel * mill.workers):
                forge_blooms(mill)
            else:
                day_over = False
                prCyan("\nInsufficient Resources\n")

    elif action == 3:
        if mill.fuel >= (mill.fuelToSteel * mill.workers) and mill.ore >= (mill.oreToSteel * mill.workers):
            forge_slabs(mill)
        else:
            day_over = False
            prCyan("\nInsufficient Resources\n")
    else:
        prCyan("\ninvalid action\n")
    return day_over

def forge_billets(mill):
    mill.ore = mill.ore - (mill.oreToSteel * mill.workers)
    mill.fuel = mill.fuel - (mill.fuelToSteel * mill.workers)
    mill.billets = mill.billets + (mill.steelProduced * mill.workers)

def forge_blooms(mill):
    mill.ore = mill.ore - (mill.oreToSteel * mill.workers)
    mill.fuel = mill.fuel - (mill.fuelToSteel * mill.workers)
    mill.blooms = mill.blooms + (mill.steelProduced * mill.workers)

def forge_slabs(mill):
    mill.ore = mill.ore - (mill.oreToSteel * mill.workers)
    mill.fuel = mill.fuel - (mill.fuelToSteel * mill.workers)
    mill.slabs = mill.slabs + (mill.steelProduced * mill.workers)

