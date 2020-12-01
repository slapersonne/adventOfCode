import math
import re


moons = {
    "Io": ((-4, 3, 15), (0, 0, 0)),
    "Europa": ((-11, -10, 13), (0, 0, 0)),
    "Ganymede": ((2, 2, 18), (0, 0, 0)),
    "Callisto": ((7, -1, 0), (0, 0, 0))
}


def get_acceleration(x1, x2):
    if x1 < x2:
        return 1
    elif x1 > x2:
        return -1
    else:
        return 0


def update_velocities():
    for name, (position, velocity) in moons.items():
        other_moons = {key: value for key, value in moons.items() if key != name}
        for other_name, (other_position, _) in other_moons.items():
            x1, y1, z1 = position
            x2, y2, z2 = other_position
            vx, vy, vz = velocity
            velocity = (
                vx + get_acceleration(x1, x2),
                vy + get_acceleration(y1, y2),
                vz + get_acceleration(z1, z2))
        moons[name] = (position, velocity)


def update_positions():
    for name, (position, velocity) in moons.items():
        x, y, z = position
        vx, vy, vz = velocity
        new_position = (x + vx, y + vy, z + vz)
        moons[name] = (new_position, velocity)


def get_potential_energy(position):
    x, y, z = position
    return abs(x) + abs(y) + abs(z)


def get_kinetic_energy(velocity):
    vx, vy, vz = velocity
    return abs(vx) + abs(vy) + abs(vz)


def get_total_energy(moon):
    position, velocity = moon
    potential = get_potential_energy(position)
    kinetic = get_kinetic_energy(velocity)
    total = potential * kinetic
    print(f"{potential} * {kinetic} = {total}")
    return total


def print_current_state():
    for name, (position, velocity) in moons.items():
        print(name, position, velocity)


def run_12a():
    for i in range(0, 1000):
        update_velocities()
        update_positions()
    print_current_state()
    energies = {name: get_total_energy(value) for name, value in moons.items()}
    print(f"Total energy : {sum(energies.values())}")


def get_all_cycles():
    i = 0
    passed_x = {}
    passed_y = {}
    passed_z = {}
    x_cycle = -1
    y_cycle = -1
    z_cycle = -1
    while x_cycle < 0 or y_cycle < 0 or z_cycle < 0:
        if i % 10000 == 0:
            print(f"i = {i}")
        all_x, all_y, all_z = [], [], []
        for index, ((x, y, z), (vx, vy, vz)) in enumerate(moons.values()):
            all_x.append(f"{x}.{vx}")
            all_y.append(f"{y}.{vy}")
            all_z.append(f"{z}.{vz}")
        key_x = "_".join(all_x)
        key_y = "_".join(all_y)
        key_z = "_".join(all_z)
        if x_cycle < 0 and key_x in passed_x:
            print(f"X Cycle found : i = {i}")
            x_cycle = i
        else:
            passed_x[key_x] = i
        if y_cycle < 0 and key_y in passed_y:
            print(f"Y Cycle found : i = {i}")
            y_cycle = i
        else:
            passed_y[key_y] = i
        if z_cycle < 0 and key_z in passed_z:
            print(f"Z Cycle found : i = {i}")
            z_cycle = i
        else:
            passed_z[key_z] = i
        update_velocities()
        update_positions()
        i += 1
    return x_cycle, y_cycle, z_cycle


def get_min_cycle(cycles):
    cycles.sort(reverse=True)
    print(cycles)
    best_cycle = cycles.pop()
    while len(cycles) > 0:
        next_cycle = cycles.pop()
        for i in range(best_cycle, (next_cycle + 1) * best_cycle, best_cycle):
            if i % next_cycle == 0:
                print(f"Cycle found : {i}")
                best_cycle = i
                break
    return best_cycle


def run_12b():
    x_cycle, y_cycle, z_cycle = get_all_cycles()
    best_cycle = get_min_cycle([x_cycle, y_cycle, z_cycle])
    print(f"Best cycle : {best_cycle}")
