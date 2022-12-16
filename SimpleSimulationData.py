from SolarSystem3d import SolarSystem, Star, Planet
from NumericalIntegrationMethods import Methods
from copy import deepcopy
import numpy as np


# Initialize new solar system using these parameters
def init_solar_system():
    system = SolarSystem(800, False)

    sun = Star(system, "Sun")

    planets = (
        Planet(
            system,
            "Planet 1",
            position=np.array([150, 50, 0], dtype=float),
            velocity=np.array([0, 0, 0], dtype=float),
        ),
        Planet(
            system,
            "Planet 2",
            mass=20,
            position=np.array([100, -50, 150], dtype=float),
            velocity=np.array([0, 0, 0], dtype=float)
        )
    )

    return system


dt = 1
for method in Methods:
    Data = []
    solar_system = init_solar_system()
    time = 0
    for x in range(86400):
        time += (x+1) * dt
        solar_system.calculate_all_gravitational_interactions()
        solar_system.update_all(dt=1, method=method)
        item = [time, deepcopy(solar_system)]
        Data.append(item)
    np.save("./Data/"+method.value, Data)
