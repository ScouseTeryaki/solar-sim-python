from enum import Enum
import numpy as np


class Methods(Enum):
    EULER_METHOD = "EulerMethod"
    EULER_CROMER_METHOD = "CromerMethod"
    EULER_RICHARDSON_METHOD = "RichardsonMethod"
    VERLET_METHOD = "VerletMethod"


def euler_method_update(dt, body):
    # https://en.wikipedia.org/wiki/Euler_method
    new_position = np.add(body.position, body.velocity * dt)
    new_velocity = np.add(body.velocity, body.acceleration * dt)
    return new_position, new_velocity


def euler_cromer_method_update(dt, body):
    # https://en.wikipedia.org/wiki/Semi-implicit_Euler_method
    new_velocity = np.add(body.velocity, body.acceleration * dt)
    new_position = np.add(body.position, body.velocity * dt)
    return new_position, new_velocity


def euler_richardson_method_update(dt, body):
    # https://www.physics.udel.edu/~bnikolic/teaching/phys660/numerical_ode/node4.html
    new_velocity = np.add(body.velocity, 1 / 2 * body.acceleration * dt)
    new_position = np.add(body.position, 1 / 2 * body.velocity * dt)
    return new_position, new_velocity


def verlet_method_update(dt, body, bodies):
    # Euler Richardson Method to get a_n+1
    position_nplus1, velocity_nplus1 = euler_richardson_method_update(dt, body)

    acceleration_nplus1 = 0
    other_bodies = bodies.copy()
    other_bodies.remove(body)
    for other_body in other_bodies:
        acceleration_nplus1 += calculate_gravitational_acceleration_from_other_body(other_body,
                                                                                    position_nplus1)

    # https://en.wikipedia.org/wiki/Verlet_integration
    new_position = np.add(body.position, (body.velocity * dt) + (1 / 2 * body.acceleration * dt ** 2))
    new_velocity = np.add(body.velocity, 1 / 2 * (body.acceleration + acceleration_nplus1) * dt)
    return new_position, new_velocity


def calculate_gravitational_acceleration_from_other_body(other_body, position):
    distance_vector = np.subtract(other_body.position.astype(float), position)
    distance = np.linalg.norm(distance_vector)
    distance_unit_vector = np.divide(distance_vector, distance)
    gravity_mag = other_body.mass / distance ** 2
    gravity = np.multiply(gravity_mag, distance_unit_vector)
    return gravity
