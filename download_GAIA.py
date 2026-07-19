from astroquery.gaia import Gaia
from astropy.table import Table

query = """
SELECT TOP 50000
    source_id,
    ra,
    dec,
    parallax,
    parallax_error,
    pmra,
    pmdec,
    phot_g_mean_mag,
    bp_rp
FROM gaiadr3.gaia_source
WHERE
    CONTAINS(POINT('ICRS', ra, dec) , CIRCLE('ICRS', 56.75, 24.12, 1.5)) = 1
"""

print("Downloading Gaia DR3 data...")

job = Gaia.launch_job(query)
table = job.get_results()

print(f"Downloaded {len(table)} stars")

table.write("pleiades.fits", overwrite=True)

print("Saved as pleiades.fits")
