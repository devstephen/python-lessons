# Lambda are anonymous functions

metals = [ "gold", "silver", "platinum", "palladium" ]

print(list(filter( lambda el:  len(el) > 5, metals)))

p_metals = list(filter(lambda metal: "p" in metal, metals))
print(p_metals)

count_l = list(map(lambda metal: metal.count("l"), metals))

print(count_l)


print(list(map(lambda val: val.replace("s", "$"), metals)))
