"""
color_magnitude_diagram.py

Plots the Gaia Color–Magnitude Diagram (CMD) for the detected Pleiades cluster.
"""

import numpy as np
import matplotlib.pyplot as plt
from read_data import load_data
from clean_data import clean_data
from cluster_detection import identify_cluster

table = load_data()
cleaned = clean_data(table)
cluster = identify_cluster(cleaned)

color = cluster["bp_rp"]
distance = 1000 / cluster["parallax"]
absolute_mag = cluster["phot_g_mean_mag"] - 5 * np.log10(distance) + 5

plt.figure(figsize=(8, 6))
plt.scatter(color,absolute_mag,s=15,color="blue")
plt.gca().invert_yaxis()

plt.xlabel("BP − RP Color")
plt.ylabel("Absolute G Magnitude")
plt.title("Color–Magnitude Diagram of the Pleiades")
plt.grid(True)
plt.tight_layout()

plt.savefig("pleiades_CMD.png", dpi=300)

plt.show()
