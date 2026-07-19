"""
cluster_statistics.py

Calculates basic properties of the detected Pleiades cluster.
"""

import numpy as np
import matplotlib.pyplot as plt
from read_data import load_data
from clean_data import clean_data
from cluster_detection import identify_cluster

table = load_data()
cleaned = clean_data(table)

cluster = identify_cluster(cleaned)

def cluster_statistics(cluster):

    print("="*50)
    print("CLUSTER STATISTICS")
    print("="*50)

    print(f"Number of members : {len(cluster)}")
    print()
    print(f"Mean RA        : {np.mean(cluster['ra']):.4f} deg")
    print(f"Std RA        : {np.std(cluster['ra']):.4f}")
    print()
    print(f"Mean Dec       : {np.mean(cluster['dec']):.4f} deg")
    print(f"Std Dec       : {np.std(cluster['dec']):.4f}")
    print()
    print(f"Mean PMRA      : {np.mean(cluster['pmra']):.3f} mas/yr")
    print(f"Std PMRA      : {np.std(cluster['pmra']):.4f}")
    print()
    print(f"Mean PMDEC     : {np.mean(cluster['pmdec']):.3f} mas/yr")
    print(f"Std PMDEC     : {np.std(cluster['pmdec']):.4f}")
    print()

    print(f"Mean Parallax  : {np.mean(cluster['parallax']):.3f} mas")
    print(f"Std Parallax  : {np.std(cluster['parallax']):.4f}")
    print(f"Min Parallax : {cluster['parallax'].min():.3f} mas")
    print(f"Max Parallax : {cluster['parallax'].max():.3f} mas")
    print()

    distance = 1000 / cluster["parallax"]

    mean_distance = np.mean(distance)
    std_distance = np.std(distance)

    print(f"Mean Distance : {mean_distance:.2f} pc")
    print(f"Std Distance  : {std_distance:.2f} pc")
    print(f"Min Distance : {distance.min():.2f} pc")
    print(f"Max Distance : {distance.max():.2f} pc")

    print("="*50)

    fig, ax = plt.subplots(2, 2, figsize=(10, 8))

    ax[0,0].hist(distance, bins=20, edgecolor="black")
    ax[0,0].set_title("Distance Distribution")
    ax[0,0].set_xlabel("Distance (pc)")
    ax[0,0].set_ylabel("Number of Stars")

    ax[0,1].hist(cluster["parallax"], bins=20, edgecolor="black")
    ax[0,1].set_title("Parallax Distribution")
    ax[0,1].set_xlabel("Parallax (mas)")
    ax[0,1].set_ylabel("Number of Stars")

    ax[1,0].hist(cluster["pmra"], bins=20, edgecolor="black")
    ax[1,0].set_title("PMRA Distribution")
    ax[1,0].set_xlabel("PMRA (mas/yr)")
    ax[1,0].set_ylabel("Number of Stars")

    ax[1,1].hist(cluster["pmdec"], bins=20, edgecolor="black")
    ax[1,1].set_title("PMDEC Distribution")
    ax[1,1].set_xlabel("PMDEC (mas/yr)")
    ax[1,1].set_ylabel("Number of Stars")

    fig.suptitle("Pleiades Cluster Statistical Distributions", fontsize=14)

    plt.tight_layout()
    plt.savefig("cluster_histograms.png", dpi=300)
    plt.show()

    return distance

cluster_statistics(cluster)
