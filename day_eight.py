def min_fuel(positions: list):
    return min((sum((abs(ending - starting) for starting in positions)) for ending in set(positions)))


crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

print(min_fuel(crabs))
