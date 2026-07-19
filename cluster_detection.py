"""
cluster_detection.py

Detect the Pleiades cluster using DBSCAN.
"""

import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from read_data import load_data
from clean_data import clean_data

DBSCAN_EPS = 1.8
DBSCAN_MIN_SAMPLES = 8

def apply_manual_filter(table):
   
    mask = ((table["parallax"] > 2) &
        (table["parallax"] < 12) &
        (table["pmra"] > 10) &
        (table["pmra"] < 30) &
        (table["pmdec"] > -55) &
        (table["pmdec"] < -40))

    filtered_table = table[mask]

    return filtered_table


def prepare_features(filtered_table):

    features = np.column_stack((
        filtered_table["pmra"],
        filtered_table["pmdec"],
        filtered_table["parallax"]))

    features = StandardScaler().fit_transform(features)

    return features
   
def run_dbscan(features):

    dbscan = DBSCAN(eps=DBSCAN_EPS,min_samples=DBSCAN_MIN_SAMPLES)

    labels = dbscan.fit_predict(features)

    return labels

def extract_cluster(filtered_table, labels):

    valid = labels != -1

    cluster_ids, counts = np.unique(labels[valid],return_counts=True)

    largest_cluster = cluster_ids[np.argmax(counts)]

    cluster = filtered_table[labels == largest_cluster]

    return cluster

def identify_cluster(table):

    print("=" * 50)
    print("CLUSTER DETECTION")
    print("=" * 50)

    filtered_table = apply_manual_filter(table)

    features = prepare_features(filtered_table)

    labels = run_dbscan(features)

    noise = np.sum(labels == -1)

    cluster = extract_cluster(filtered_table, labels)

    cluster_ids, counts = np.unique(
        labels[labels != -1],
        return_counts=True
    )

    print(f"Stars after manual filter : {len(filtered_table)}")
    print(f"Number of clusters        : {len(cluster_ids)}")
    print(f"Noise stars              : {noise}")
    print(f"Cluster members          : {len(cluster)}")

    print("=" * 50)

    return cluster

table = load_data()
cleaned = clean_data(table)
cluster = identify_cluster(cleaned)
