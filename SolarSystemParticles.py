import numpy as np
from SolarSystem3d import Particle


sunMass_kg = 1.9885e30  # https://en.wikipedia.org/wiki/Sun
sunRadius_m = 695700 * 1e3  # https://en.wikipedia.org/wiki/Sun

# The sun is at the centre of the simulation
Sun = Particle(
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Sun",
    mass=sunMass_kg
)

earth_mass_kg = 5.97237e24     # https://en.wikipedia.org/wiki/Earth
earth_radius_m = 6371 * 1e3  # https://en.wikipedia.org/wiki/Earth
earth_aphelion_distance_m = 1521 * 1e11  # https://en.wikipedia.org/wiki/Earth
earth_position = earth_aphelion_distance_m + sunRadius_m

Earth = Particle(
    position=np.array([earth_position, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=earth_mass_kg
)

Earth.initialize_velocity(Sun, earth_position)

sat_mass_kg = 100.
sat_distance_from_earth = earth_radius_m + (35786 * 1e3)
sat_position = earth_position + sat_distance_from_earth
sat_velocity = np.sqrt(Earth.G * Earth.mass / sat_distance_from_earth)  # from centrifugal force = gravitational force

# Satellite = Particle(
#     position=np.array([sat_position, 0, 0]),
#     velocity=np.array([0, sat_velocity, 0]),
#     acceleration=np.array([0, 0, 0]),
#     name="Satellite",
#     mass=sat_mass_kg
# )

Solar_System = [Sun, Earth]
