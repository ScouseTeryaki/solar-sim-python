import numpy as np
import SolarSystemParticles
import Particle
import pygame

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    dt = 10
    solarSystemParticles = SolarSystemParticles.Solar_System

    # Loop over all particles
    for particle_i in solarSystemParticles:
        # Create temporary copy of particle list, remove the
        # particle we are going to update properties for
        tempSolarSystemParticles = solarSystemParticles.copy()
        tempSolarSystemParticles.remove(particle_i)
        # Loop over temp particle list
        for particle_j in tempSolarSystemParticles:
            # Update particle_i using temporary particle
            particle_i.update(particle_j, dt, Particle.EULER_METHOD)

            screen_center = np.array([SCREEN_WIDTH / 2 - particle_i.sprite.radius_offset,
                                      SCREEN_HEIGHT / 2 - particle_i.sprite.radius_offset])

            particle_position_2d = np.array([particle_i.position[0], particle_i.position[2]])
            particle_position_2d = np.multiply(particle_position_2d, 1e-10)

            print(particle_i.name)
            print(particle_i.position[0])
            print(particle_position_2d)

            particle_screen_position = np.add(screen_center, particle_position_2d)

            screen.blit(particle_i.sprite.surface,
                        (particle_screen_position[0],
                         particle_screen_position[1]))

    pygame.display.flip()
