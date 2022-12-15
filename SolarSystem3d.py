import numpy as np
import math
import matplotlib.pyplot as plt
from NumericalIntegrationMethods import Methods, verlet_method_update, euler_method_update, euler_cromer_method_update,\
    euler_richardson_method_update


class SolarSystem:
    def __init__(self, size):
        self.size = size
        self.bodies = []

        self.fig, self.ax = plt.subplots(
            1,
            1,
            subplot_kw={"projection": "3d"},
            figsize=(self.size / 50, self.size / 50)
        )
        self.fig.tight_layout()

    def add_body(self, body):
        self.bodies.append(body)

    def update_all(self, dt, method):
        for body in self.bodies:
            # Create temporary copy of particle list, remove the
            # particle we are going to update properties for
            temp_bodies = self.bodies.copy()
            temp_bodies.remove(body)
            # Loop over temp particle list
            for particle_j in temp_bodies:
                # Update particle_i using temporary particle
                body.update(particle_j, dt, method)
            body.draw()

    def draw_all(self):
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))
        plt.pause(0.001)
        self.ax.clear()


class SolarSystemBody:
    G = 6.67408E-11
    min_display_size = 1.0
    display_log_base = 1.3

    def __init__(
            self,
            solar_system=SolarSystem(400),
            position=np.array([0, 0, 0], dtype=float),
            velocity=np.array([0, 0, 0], dtype=float),
            acceleration=np.array([0, 0, 0], dtype=float),
            name='Unknown Particle',
            mass=1.0
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

    def initialize_velocity(self, body, distance):
        # from centrifugal force = gravitational force
        velocity = np.sqrt(self.G * body.mass / distance)
        self.velocity = np.array([0, velocity, 0])

    def update(self, body, dt, method):
        acceleration = self.calculate_gravitational_acceleration(body, self.position)
        np.add(self.acceleration, acceleration, out=self.acceleration)

        if method == Methods.EULER_METHOD:
            euler_method_update(dt, self)
        elif method == Methods.EULER_CROMER_METHOD:
            euler_cromer_method_update(dt, self)
        elif method == Methods.EULER_RICHARDSON_METHOD:
            euler_richardson_method_update(dt, self)
        elif method == Methods.VERLET_METHOD:
            verlet_method_update(dt, self, body)

    def calculate_gravitational_acceleration(self, body, position):
        distance_vector = np.subtract(position, body.position.astype(float))
        distance = np.linalg.norm(distance_vector)
        distance_unit_vector = np.divide(distance_vector, distance)
        gravity_scalar = -(self.G * body.mass) / distance ** 2
        return np.multiply(gravity_scalar, distance_unit_vector)

    def calculate_kinetic_energy(self):
        v_norm = np.linalg.norm(self.velocity)
        ke = 1 / 2 * self.mass * v_norm ** 2
        return ke
