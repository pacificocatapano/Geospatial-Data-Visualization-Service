import pyubx2
import pandas as pd

class UBXParser():

    def __init__(self,
                 stream_path):
        self.stream_path = stream_path
    
    def parse_all(self):
        LLH = []
        STATUS = []

        with open(self.stream_path, 'rb') as stream:
            ubr = pyubx2.UBXReader(stream)
            
            for _, parsed in ubr:
                if parsed != None:
                    if parsed.identity == 'NAV-HPPOSLLH':
                        LLH.append([parsed.iTOW, parsed.lon, parsed.lat, parsed.height])
                    if parsed.identity == 'NAV-STATUS':
                        pass
        
        LLH = pd.DataFrame(LLH,
                           columns=['Timestamp', 'Longitude', 'Latitude', 'Height'])
        STATUS = pd.DataFrame(STATUS)

        return LLH, STATUS

parser = UBXParser(stream_path='../COM10___115200_221206_130405.ubx')
LLH, STATUS = parser.parse_all()
print(LLH)