from enum import Enum
import numpy as np


class Methods(Enum):
    EULER_METHOD = 1
    EULER_CROMER_METHOD = 2
    EULER_RICHARDSON_METHOD = 3
    VERLET_METHOD = 4


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


def verlet_method_update(dt, body_1, body_2):
    # Euler Richardson Method to get a_n+1
    velocity_nplus1 = np.add(body_1.velocity, 1 / 2 * body_1.acceleration * dt)
    position_nplus1 = np.add(body_1.position, 1 / 2 * velocity_nplus1 * dt)

    # fix later!!!!!!
    acceleration_nplus1 = SolarSystemBody.calculate_gravitational_acceleration(body_2, position_nplus1)

    # https://en.wikipedia.org/wiki/Verlet_integration
    new_position = np.add(body_1.position, (body_1.velocity * dt) + (1 / 2 * body_1.acceleration * dt ** 2))
    new_velocity = np.add(body_1.velocity, 1 / 2 * (body_1.acceleration + acceleration_nplus1) * dt)
    return new_position, new_velocity
