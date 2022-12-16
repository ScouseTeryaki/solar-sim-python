import numpy as np
import math
import itertools
import matplotlib.pyplot as plt
from NumericalIntegrationMethods import Methods, euler_method_update, euler_cromer_method_update,\
    euler_richardson_method_update, verlet_method_update

# Define gravitational constant
G = 6.67408E-11


class SolarSystem:
    def __init__(self, plt_size):
        self.plt_size = plt_size
        self.bodies = []
        self.star = None

        self.fig, self.ax = plt.subplots(
            1,
            1,
            subplot_kw={"projection": "3d"},
            figsize=(self.plt_size / 50, self.plt_size / 50)
        )
        self.fig.tight_layout()

    def add_body(self, body):
        self.bodies.append(body)

    def add_star(self, star):
        self.star = star

    def update_all(self, dt, method):
        self.bodies.sort(key=lambda item: item.position[0])
        for body in self.bodies:
            if method == Methods.VERLET_METHOD:
                body.verlet_update_position(dt=dt, bodies=self.bodies)
            else:
                body.update_position(dt=dt, method=method)
                body.draw()

    def draw_all(self):
        self.ax.set_xlim((-self.plt_size / 2, self.plt_size / 2))
        self.ax.set_ylim((-self.plt_size / 2, self.plt_size / 2))
        self.ax.set_zlim((-self.plt_size / 2, self.plt_size / 2))
        plt.pause(0.001)
        self.ax.clear()

    def calculate_all_gravitational_interactions(self):
        bodies_copy = self.bodies.copy()
        for body in bodies_copy:
            body.acceleration = np.array([0, 0, 0], dtype=float)  # Set acceleration to 0
            removed_body_bodies = bodies_copy.copy()
            removed_body_bodies.remove(body)
            for other_body in removed_body_bodies:
                body.update_gravitational_acceleration_from_other_body(other_body)


class SolarSystemBody:
    min_display_size = 1.0
    display_log_base = 1.3

    def __init__(
            self,
            solar_system,
            position=np.array([0, 0, 0], dtype=float),
            velocity=np.array([0, 0, 0], dtype=float),
            acceleration=np.array([0, 0, 0], dtype=float),
            name='Unknown Particle',
            mass=1
    ):
        self.solar_system = solar_system
        self.name = name
        self.mass = mass
        self.position = position.copy().astype(float)
        self.velocity = velocity.copy().astype(float)
        self.acceleration = acceleration.copy().astype(float)

        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )
        self.color = "black"

        self.solar_system.add_body(self)

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def draw(self):
        self.solar_system.ax.plot(
            *self.position,
            marker="o",
            markersize=self.display_size,
            color=self.color
        )

    def update_position(self, dt, method):
        if method == Methods.EULER_METHOD:
            self.position, self.velocity = euler_method_update(dt, self)
        elif method == Methods.EULER_CROMER_METHOD:
            self.position, self.velocity = euler_cromer_method_update(dt, self)
        elif method == Methods.EULER_RICHARDSON_METHOD:
            self.position, self.velocity = euler_richardson_method_update(dt, self)

    def verlet_update_position(self, dt, bodies):
        self.position, self.velocity = verlet_method_update(dt, self, bodies)

    def update_gravitational_acceleration_from_other_body(self, other):
        gravity = self.calculate_gravitational_acceleration_from_other_body(other)
        self.acceleration = np.add(self.acceleration, gravity)

    def calculate_gravitational_acceleration_from_other_body(self, other):
        distance_vector = np.subtract(other.position.astype(float), self.position)
        distance = np.linalg.norm(distance_vector)
        distance_unit_vector = np.divide(distance_vector, distance)
        gravity_mag = other.mass / distance ** 2
        gravity = np.multiply(gravity_mag, distance_unit_vector)
        return gravity


class Planet(SolarSystemBody):
    colours = itertools.cycle([(1, 0, 0), (0, 1, 0), (0, 0, 1)])

    def __init__(
        self,
        solar_system,
        name,
        mass=10,
        position=np.array([0, 0, 0], dtype=float),
        velocity=np.array([0, 0, 0], dtype=float),
        acceleration=np.array([0, 0, 0], dtype=float),
    ):
        super(Planet, self).__init__(solar_system, position, velocity, acceleration, name, mass)
        self.colour = next(Planet.colours)


class Star(SolarSystemBody):
    def __init__(
            self,
            solar_system,
            name,
            mass=10_000,
            position=np.array([0, 0, 0], dtype=float),
            velocity=np.array([0, 0, 0], dtype=float),
            acceleration=np.array([0, 0, 0], dtype=float),
    ):
        super(Star, self).__init__(solar_system, position, velocity, acceleration, name, mass)
        self.colour = "yellow"

        self.solar_system.add_star(self)
