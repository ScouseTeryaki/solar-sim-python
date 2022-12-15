import numpy as np
from Particle import Particle
from ParticleSprite import ParticleSprite


sunMass_kg = 1.9885e30  # https://en.wikipedia.org/wiki/Sun
sunRadius_m = 695700 * 1e6  # https://en.wikipedia.org/wiki/Sun

# The sun is at the centre of the simulation
Sun = Particle(
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Sun",
    mass=sunMass_kg,
    sprite=ParticleSprite(50, (255, 100, 0))
)

earth_mass_kg = 5.97237e24     # https://en.wikipedia.org/wiki/Earth
earth_radius_m = 63710 * 1e3  # https://en.wikipedia.org/wiki/Earth
earth_aphelion_distance_m = 1521 * 1e8  # https://en.wikipedia.org/wiki/Earth
earth_distance = earth_aphelion_distance_m + sunRadius_m

earth_velocity = np.sqrt(Sun.G * Sun.mass / earth_distance)  # from centrifugal force = gravitational force

Earth = Particle(
    position=np.array([earth_distance, 0, 0]),
    velocity=np.array([0, earth_velocity, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=earth_mass_kg,
    sprite=ParticleSprite(20, (0, 255, 0))
)

sat_mass_kg = 100.
sat_distance_from_earth = earth_radius_m + (35786 * 1e3)
sat_aphelion_distance_m = earth_distance + sat_distance_from_earth
sat_velocity = np.sqrt(Earth.G * Earth.mass / sat_distance_from_earth)  # from centrifugal force = gravitational force

Satellite = Particle(
    position=np.array([sat_aphelion_distance_m, 0, 0]),
    velocity=np.array([0, sat_velocity, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Satellite",
    mass=sat_mass_kg,
    sprite=ParticleSprite(5, (105, 105, 105))
)

Solar_System = [Sun, Earth, Satellite]
