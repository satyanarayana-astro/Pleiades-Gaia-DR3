# Analysis of the Pleiades Open Cluster Using Gaia DR3 Data

## Overview

This project analyzes the Pleiades (Messier 45) open star cluster using Gaia Data Release 3 (Gaia DR3). The workflow includes data cleaning, cluster identification using the DBSCAN algorithm, statistical analysis, and scientific visualization.

## Features

- Read Gaia DR3 FITS data
- Clean astronomical data
- Detect cluster members using DBSCAN
- Calculate cluster statistics
- Generate a sky map
- Plot proper motion diagram
- Plot color–magnitude diagram (CMD)
- Generate statistical histograms

## Project Structure

```
main.py
read_data.py
clean_data.py
cluster_detection.py
cluster_statistics.py
sky_map.py
proper_motion_diagram.py
color_magnitude_diagram.py
```

## Requirements

- Python 3.10+
- NumPy
- Matplotlib
- Astropy
- Scikit-learn

Install dependencies:

```bash
pip install -r requirements.txt
```

## Results

- Total stars loaded: 50,000
- Cleaned stars: 42,732
- Cluster members detected: 680
- Noise points: 39
- Mean distance: ~135 pc

## Author

**Nunna Satyanarayana**  
BS–MS (Physics)  
Indian Institute of Science Education and Research Tirupati
