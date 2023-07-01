import pyubx2
import pandas as pd

file_path = 'COM10___115200_221206_130405.ubx'
stream = open(file_path, 'rb')
ubr = pyubx2.UBXReader(stream)

LLH = []
STATUS = []

for _, parsed in ubr:
    if parsed != None:
        if parsed.identity == 'NAV-HPPOSLLH':
            LLH.append([parsed.iTOW, parsed.lon, parsed.lat, parsed.height])
        if parsed.identity == 'NAV-STATUS':
            pass

LLH = pd.DataFrame(LLH,
                   columns = ['Timestamp', 'Longitude', 'Latitude', 'Height'])

print(LLH)