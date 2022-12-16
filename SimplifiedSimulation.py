from SolarSystem3d import SolarSystem, Star, Planet
from NumericalIntegrationMethods import Methods
import numpy as np

solar_system = SolarSystem(800)

sun = Star(solar_system, "Sun")

planets = (
    Planet(
        solar_system,
        "Planet 1",
        position=np.array([150, 50, 0], dtype=float),
        velocity=np.array([0, 5, 5], dtype=float),
    ),
    Planet(
        solar_system,
        "Planet 2",
        mass=20,
        position=np.array([100, -50, 150], dtype=float),
        velocity=np.array([5, 0, 0], dtype=float)
    )
)

while True:
    solar_system.calculate_all_gravitational_interactions()
    solar_system.update_all(dt=1, method=Methods.EULER_METHOD)
    solar_system.draw_all()
