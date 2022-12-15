import numpy as np
from SolarSystem3d import SolarSystem, SolarSystemBody
from NumericalIntegrationMethods import Methods

# Define delta time constant
dt = 100

solar_system = SolarSystem(400)

sunMass_kg = 1.9885e30  # https://en.wikipedia.org/wiki/Sun
sunRadius_m = 695700 * 1e3  # https://en.wikipedia.org/wiki/Sun

# The sun is at the centre of the simulation
Sun = SolarSystemBody(
    solar_system=solar_system,
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Sun",
    mass=sunMass_kg
)

while True:
    solar_system.update_all(dt=dt, method=Methods.EULER_METHOD)
    solar_system.draw_all()



