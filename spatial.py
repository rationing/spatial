print("0")

# Download cartographic boundary files with standard libraries

import urllib.request
import zipfile

a = "https://www2.census.gov/geo/tiger/GENZ2025/shp/"
url = a + "cb_2025_us_state_20m.zip"

urlretrieve = urllib.request.urlretrieve(url)
with zipfile.ZipFile(urlretrieve[0]) as zip:
	zip.extractall()

# Load the shapefile with pygeoda

import pygeoda

data = pygeoda.open("cb_2025_us_state_20m.shp")
print(data)



print("1")
