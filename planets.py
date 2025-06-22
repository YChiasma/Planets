from skyfield.api import load
import matplotlib.pyplot as plt
import numpy as np

# Load planetary data and timescale
planets = load('de421.bsp')
ts = load.timescale()
t = ts.now()

# Define planets of interest
planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_names_2 = [name.upper() + " BARYCENTER" for name in planet_names]
planet_objects = [planets[name] for name in planet_names_2]

# Get positions of planets from the Sun
sun = planets['sun']
positions = [planet.at(t).observe(sun).ecliptic_position().au for planet in planet_objects]

# Unpack coordinates
x = [pos[0] for pos in positions]
y = [pos[1] for pos in positions]

# Define colors and scale
colors = ['gray', 'orange', 'blue', 'red', 'brown', 'gold', 'lightblue', 'darkblue']
sizes = [5, 8, 10, 7, 20, 18, 14, 13]  # Arbitrary for visualization

# Plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(0, 0, color='yellow', s=200, label='Sun')  # Sun at origin
for i, name in enumerate(planet_names):
    ax.scatter(x[i], y[i], color=colors[i], s=sizes[i]**2, label=name)
    ax.plot([0, x[i]], [0, y[i]], color='lightgray', linestyle='--', linewidth=0.5)

# Orbital lines (circles to approximate)
for i in range(len(x)):
    r = np.sqrt(x[i]**2 + y[i]**2)
    orbit = plt.Circle((0, 0), r, color='lightgray', fill=False, linestyle=':', linewidth=0.5)
    ax.add_artist(orbit)

ax.set_aspect('equal')
ax.set_title('Current Positions of Planets (Ecliptic Plane, to scale)')
ax.legend(loc='lower left')
plt.xlabel('AU (Astronomical Units)')
plt.ylabel('AU')
plt.grid(True)
plt.show()
