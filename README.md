# solar-sim-python
This project investigates the accuracy of different numerical integration methods for
simulating an n-body gravitational simulation.

NumericalIntegrationMethods.py -> This file holds the functions for the different numerical
integration methods I used, and a "Methods" enum that was used to define which method to use.

SimplifiedSimulation.py -> This file holds a simplified 3-body simulation (1 star, 2 planets).
The simulation is then drawn onto a matplotlib 3D figure. To use different numerical methods
change the method in solar_system.update_all.

SolarSystem3d.py -> This file holds the classes for the solar system and solar system bodies.
In each class are the function to calculate forces and update their properties.

SimpleSimulationData.py -> This file generates a npy file containing data for a simple n-body simulation using all
the numerical analysis methods.

Analysis.py -> This file takes the generated npy file and calculates the error in total linear
momentum.