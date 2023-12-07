import matplotlib.pyplot as plt
import numpy as np
g = 9.8 
t = np.linspace(0, 5, 100)
v = -g * t

plt.plot(t, v)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs. Time for Free Falling Object')
plt.grid(True)
plt.show()