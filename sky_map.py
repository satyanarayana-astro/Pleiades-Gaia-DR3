"""
sky_map.py

Plots the detected Pleiades cluster on the sky.
"""

import matplotlib.pyplot as plt
from read_data import load_data
from clean_data import clean_data
from cluster_detection import identify_cluster, apply_manual_filter

table = load_data()
cleaned = clean_data(table)
filtered = apply_manual_filter(cleaned)
cluster = identify_cluster(cleaned)

plt.figure(figsize=(8, 6))
plt.scatter(filtered["ra"],filtered["dec"],s=8,color="lightgray",alpha=0.4,label="Filtered Stars")
plt.scatter(cluster["ra"],cluster["dec"],s=18,color="blue",label="Pleiades Members")

plt.xlabel("Right Ascension (deg)")
plt.ylabel("Declination (deg)")
plt.title("Detected Pleiades Cluster")
plt.gca().invert_xaxis()

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("pleiades_sky_map.png", dpi=300)

plt.show()
