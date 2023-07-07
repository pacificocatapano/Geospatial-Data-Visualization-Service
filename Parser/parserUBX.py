import pyubx2
import pandas as pd

class UBXParser():
    def __init__(self, stream_path):
        self.stream_path = stream_path
    
    def parse_all(self):
        LLH = []
        ECEF = []
        STATUS = []

        with open(self.stream_path, 'rb') as stream:
            ubr = pyubx2.UBXReader(stream)
            
            for _, parsed in ubr:
                if parsed != None:
                    if parsed.identity == 'NAV-HPPOSLLH':
                        LLH.append([parsed.version,
                                    parsed.reserved0,
                                    parsed._get_dict()['flags'],
                                    parsed.invalidLlh,
                                    parsed.iTOW,
                                    parsed.lon,
                                    parsed.lat,
                                    parsed.height,
                                    parsed.hMSL,
                                    parsed._lonHp,
                                    parsed._latHp,
                                    parsed._heightHp,
                                    parsed._hMSLHp,
                                    parsed.hAcc,
                                    parsed.vAcc])
                    if parsed.identity == 'NAV-STATUS':
                        
                        STATUS.append([parsed.iTOW,
                                       parsed.gpsFix,
                                       parsed._get_dict()['flags'],
                                       parsed.gpsFixOk,
                                       parsed.diffSoln,
                                       parsed.wknSet,
                                       parsed.towSet,
                                       parsed._get_dict()['fixStat'],
                                       parsed.diffCorr,
                                       parsed.carrSolnValid,
                                       parsed.mapMatching])
                        
                    if parsed.identity == 'NAV-HPPOSECEF':
                        ECEF.append([parsed.version,
                                     parsed.reserved0,
                                     parsed.iTOW,
                                     parsed.ecefX,
                                     parsed.ecefY,
                                     parsed.ecefZ,
                                     parsed.ecefXHp,
                                     parsed.ecefYHp,
                                     parsed.ecefZHp,
                                     parsed._get_dict()['flags'],
                                     parsed.invalidEcef,
                                     parsed.pAcc])

        schema_llh = ['version',
                      'reserved0',
                      'flags',
                      'invalidLlh',
                      'iTOW',
                      'lon',
                      'lat',
                      'height',
                      'hMSL',
                      'lonHp',
                      'latHp',
                      'heightHp',
                      'hMSLHp',
                      'hAcc',
                      'vAcc']
        
        schema_ecef = ['version',
                       'reserved0',
                       'iTOW',
                       'ecefX',
                       'ecefY',
                       'ecefZ',
                       'ecefXHp',
                       'ecefYHp',
                       'ecefZHp',
                       'flags'
                       'invalidEcef',
                       'pAcc']

        schema_status = ['iTOW',
                         'gpsFix',
                         'flags',
                         'gpsFixOk',
                         'diffSoln',
                         'wknSet',
                         'towSet',
                         'fixStat',
                         'diffCorr',
                         'carrSolnValid',
                         'mapMatching']
        
        LLH = pd.DataFrame(LLH, columns=schema_llh)
        STATUS = pd.DataFrame(STATUS, columns=schema_status)
        ECEF = pd.DataFrame(ECEF, columns=schema_ecef)

        return LLH, ECEF, STATUS

parser = UBXParser(stream_path='./COM10___115200_221206_130405.ubx')
LLH, ECEF, STATUS = parser.parse_all()

LLH.to_csv('./provaUBXllh.csv', index=False, sep=';')
ECEF.to_csv('./provaUBXecef.csv', index=False, sep=';')
STATUS.to_csv('./provaUBXstatus.csv', index=False, sep=';')