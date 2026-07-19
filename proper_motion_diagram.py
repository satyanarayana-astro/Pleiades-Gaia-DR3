"""
proper_motion_diagram.py

Plots the proper motion diagram of the detected Pleiades cluster.
"""

import matplotlib.pyplot as plt
from read_data import load_data
from clean_data import clean_data
from cluster_detection import identify_cluster, apply_manual_filter

table = load_data()
cleaned = clean_data(table)
filtered = apply_manual_filter(cleaned)
cluster = identify_cluster(cleaned)

plt.figure(figsize=(8,6))
plt.scatter(filtered["pmra"],filtered["pmdec"],s=8,color="lightgray",label="Filtered Stars")
plt.scatter(cluster["pmra"],cluster["pmdec"],s=15,color="blue",label="Pleiades Members")

plt.xlabel("Proper Motion RA (mas/yr)")
plt.ylabel("Proper Motion Dec (mas/yr)")
plt.title("Proper Motion Diagram of the Pleiades")
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig("pleiades_proper_motion.png", dpi=300)

plt.show()
