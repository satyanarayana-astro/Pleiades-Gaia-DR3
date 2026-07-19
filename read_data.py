'''
02_read_data.py

Loads Gaia DR3 FITS file into an astropy table
'''

from astropy.table import Table


def load_data(filename="pleiades.fits"):
    
    #Load Gaia DR3 FITS data
    table = Table.read(filename)
    
    print("="*50)
    print("GAIA DR3 DATA LOADED")
    print("="*50)
    print(f"Number of Stars loaded :{len(table):,}")
    print(f"Number of coloums      :{len(table.colnames)}")
    print("="*50)

    return table
