import os
import numpy as np


def analyse_conservation_linear_momentum(solar_system_a, solar_system_b):
    # Total momentum = Sum of all the masses*velocity at time a = Sum of all the masses*velocity at time b
    total_momentum_a = 0
    total_momentum_b = 0
    for body in solar_system_a.bodies:
        total_momentum_a += body.mass * body.velocity
    for body in solar_system_b.bodies:
        total_momentum_b += body.mass * body.velocity

    accuracy = np.linalg.norm(total_momentum_a / total_momentum_b)

    print(accuracy)


# assign directory
directory = './Data'

# Load each file
for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    data = np.load(file, allow_pickle=True)

    solar_system_at_start = data[0][1]
    solar_system_at_end = data[-1][1]

    analyse_conservation_linear_momentum(solar_system_at_start, solar_system_at_end)
