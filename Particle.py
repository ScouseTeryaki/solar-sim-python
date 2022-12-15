import numpy as np
from ParticleSprite import ParticleSprite

EULER_METHOD = 1
EULER_CROMER_METHOD = 2
EULER_RICHARDSON_METHOD = 3
VERLET_METHOD = 4


class Particle:
    G = 6.67408E-11

    def __init__(
            self,
            position=np.array([0, 0, 0], dtype=float),
            velocity=np.array([0, 0, 0], dtype=float),
            acceleration=np.array([0, 0, 0], dtype=float),
            name='Unknown Particle',
            mass=1.0,
            sprite=ParticleSprite(25, (0, 255, 0))
            ):
        self.name = name
        self.mass = mass
        self.position = position.copy().astype(float)
        self.velocity = velocity.copy().astype(float)
        self.acceleration = acceleration.copy().astype(float)
        self.sprite = sprite

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def update(self, body, dt, method):
        acceleration = self.calculate_gravitational_acceleration(body, self.position)
        np.add(self.acceleration, acceleration, out=self.acceleration)

        if method == EULER_METHOD:
            self.euler_method_update(dt)
        elif method == EULER_CROMER_METHOD:
            self.euler_cromer_method_update(dt)
        elif method == EULER_RICHARDSON_METHOD:
            self.euler_richardson_method_update(dt)
        elif method == VERLET_METHOD:
            self.verlet_method_update(dt, body)

    def euler_method_update(self, dt):
        # https://en.wikipedia.org/wiki/Euler_method
        np.add(self.position, self.velocity * dt, out=self.position)
        np.add(self.velocity, self.acceleration * dt, out=self.velocity)

    def euler_cromer_method_update(self, dt):
        # https://en.wikipedia.org/wiki/Semi-implicit_Euler_method
        np.add(self.velocity, self.acceleration * dt, out=self.velocity)
        np.add(self.position, self.velocity * dt, out=self.velocity)

    def euler_richardson_method_update(self, dt):
        # https://www.physics.udel.edu/~bnikolic/teaching/phys660/numerical_ode/node4.html
        np.add(self.velocity, 1/2 * self.acceleration * dt, out=self.velocity)
        np.add(self.position, 1/2 * self.velocity * dt, out=self.velocity)

    def verlet_method_update(self, dt, body):
        # Euler Richardson Method to get a_n+1
        velocity_nplus1 = np.add(self.velocity, 1 / 2 * self.acceleration * dt)
        position_nplus1 = np.add(self.position, 1 / 2 * velocity_nplus1 * dt)

        acceleration_nplus1 = self.calculate_gravitational_acceleration(body, position_nplus1)

        # https://en.wikipedia.org/wiki/Verlet_integration
        np.add(self.position, (self.velocity * dt) + (1/2 * self.acceleration * dt**2), out=self.position)
        np.add(self.velocity, 1/2 * (self.acceleration + acceleration_nplus1) * dt, out=self.velocity)

    def calculate_gravitational_acceleration(self, body, position):
        distance_vector = np.subtract(position, body.position.astype(float))
        distance = np.linalg.norm(distance_vector)
        distance_unit_vector = np.divide(distance_vector, distance)
        gravity_scalar = -(self.G * body.mass)/distance**2
        return np.multiply(gravity_scalar, distance_unit_vector)

    def calculate_kinetic_energy(self):
        v_norm = np.linalg.norm(self.velocity)
        ke = 1/2 * self.mass * v_norm**2
        return ke
