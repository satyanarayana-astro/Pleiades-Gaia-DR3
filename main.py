"""
main.py

Runs the complete Pleiades Gaia DR3 analysis.
"""

print("=" * 60)
print("PLEIADES OPEN CLUSTER ANALYSIS")
print("=" * 60)

print("\nGenerating cluster statistics...")
import cluster_statistics

print("\nGenerating sky map...")
import sky_map

print("\nGenerating proper motion diagram...")
import proper_motion_diagram

print("\nGenerating color-magnitude diagram...")
import color_magnitude_diagram

print("\nAnalysis complete!")
print("Files saved:")
print(" - pleiades_sky_map.png")
print(" - pleiades_proper_motion.png")
print(" - pleiades_CMD.png")
