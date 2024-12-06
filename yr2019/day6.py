# from functools import cache
from util import tokenedlines

day = 6

data = tokenedlines(day, sep=")")

orbiter_to_orbitee = {row[1]: row[0] for row in data}

def get_orbit_count(orbiter):
    if orbiter == 'COM':
        return 0
    return 1 + get_orbit_count(orbiter_to_orbitee[orbiter])

print(sum(get_orbit_count(orbiter) for orbiter in orbiter_to_orbitee.keys()))

def get_ancestors(map, loc, sofar):
    if loc == None:
        return sofar
    return get_ancestors(map, orbiter_to_orbitee.get(loc), [loc] + sofar)

you_ancestors = get_ancestors(orbiter_to_orbitee, "YOU", [])
san_ancestors = get_ancestors(orbiter_to_orbitee, "SAN", [])

idx = 0
while you_ancestors[idx] == san_ancestors[idx]:
    idx += 1
print(len(you_ancestors) + len(san_ancestors) - 2 * (idx + 1))