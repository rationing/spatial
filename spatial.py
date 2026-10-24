print("0")

# Download cartographic boundary files with standard libraries

import urllib.request
import zipfile

a = "https://www2.census.gov/geo/tiger/GENZ2025/shp/"
url = a + "cb_2025_us_state_20m.zip"

urlretrieve = urllib.request.urlretrieve(url)
with zipfile.ZipFile(urlretrieve[0]) as zip:
	zip.extractall()

# Load and visualize the shapefile with geopandas and matplotlib

import geopandas
import matplotlib.pyplot

data = geopandas.read_file("cb_2025_us_state_20m.shp")

# Remove Puerto Rico
data = data.drop(index=24)

# Remove Alaska
data = data.drop(index=25)

# Remove Hawaii
data = data.drop(index=29)

data.plot()
matplotlib.pyplot.show()

# Analyze the shapefile with additional data and pygeoda

import pygeoda



print("1")
