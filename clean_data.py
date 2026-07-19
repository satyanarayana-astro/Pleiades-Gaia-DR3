"""
clean_data.py

Removes invalid Gaia DR3 entries before analysis.
"""

import numpy as np

def clean_data(table):

    original_count = len(table)

    mask = (np.isfinite(table["parallax"]) &
        np.isfinite(table["pmra"]) &
        np.isfinite(table["pmdec"]) &
        np.isfinite(table["phot_g_mean_mag"]) &
        np.isfinite(table["bp_rp"]))

    cleaned_table = table[mask]

    cleaned_count = len(cleaned_table)
    removed = original_count - cleaned_count

    print("=" * 50)
    print("DATA CLEANING")
    print("=" * 50)
    print(f"Original stars : {original_count:,}")
    print(f"Cleaned stars  : {cleaned_count:,}")
    print(f"Removed stars  : {removed:,}")
    print(f"Percentage removed : {removed/original_count*100:.2f}%")
    print("=" * 50)

    return cleaned_table
