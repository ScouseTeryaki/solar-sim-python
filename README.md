# solar-sim-python
This project investigates the accuracy of different numerical integration methods for
simulating an n-body gravitational simulation.

NumericalIntegrationMethods.py -> This file holds the functions for the different numerical
integration methods I used, and a "Methods" enum that was used to define which method to use.

SimplifiedSimulation.py -> This file holds a simplified 3-body simulation (1 star, 2 planets).
The simulation is then drawn onto a matplotlib 3D figure. The data for the simulation is writen
to a file to be used in ConservationTest.py

SolarSystem3d.py -> This file holds the classes for the solar system and solar system bodies.
In each class are the function to calculate forces and update their properties.

ConservationTest.py -> This file tests the conservation of total linear momentum from the file
exported from SimplifiedSimulation.py.