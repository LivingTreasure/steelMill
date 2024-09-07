from utility import prEvent
from random import choices

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

def eventHandler(mill, market):
    if mill.union_event == True:
        prEvent("Your workers are trying to unionize - Labor cost will go up unless you break them up")
        mill.pay_rate = mill.pay_rate + 500
    if mill.derail_event == True:
        prEvent("There has been a derailment in the rail yard - You can only use trucks until you fix it")
        if mill.rail_cap > 9:
            mill.rail_cap = mill.rail_cap - mill.derail_amount
            mill.rail_cap_arch  = mill.rail_cap
    if mill.fire_event == True:
        prEvent("There is a fire on the shop floor - you need to put it out")
    if mill.priceDrop_event == True:
        prEvent("The Ore market has crashed - take advantage while you can")
        mill.ore_cost = market.ore_cost - 11.5
    if mill.priceSpike_event == True:
        prEvent("The market for steel is soaring - take advantage while you can")
        market.billet_cost = market.billet_cost + 35

