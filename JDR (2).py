import matplotlib.pyplot as plt
import numpy as np
time = np.linspace(0, 5, 100)
initial_velocity = (0)
gravity = 9.8
time_of_flight = (2 * initial_velocity) / gravity
initial_height = gravity * -1/2 * time ** 2
time = np.linspace(0, 5, 100)
height = initial_height + initial_velocity * time - 0.5 * gravity * time ** 2
   
    
plt.plot(time, height)
plt.xlabel("time (s)")
plt.ylabel("height (m)")
plt.title("X vs T GRAPH")
plt.grid(True)
plt.show()
