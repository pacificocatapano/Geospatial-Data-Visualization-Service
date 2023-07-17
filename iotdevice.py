import pyubx2
import pandas as pd
import requests
from time import sleep

url = 'http://127.0.0.1:5000/acquisisciDati'
file_path = './file.ubx'

def parse_all(stream_path, url):
    with open(stream_path, 'rb') as stream:
        ubr = pyubx2.UBXReader(stream)
        
        for _, parsed in ubr:
            if parsed != None:
                if parsed.identity == 'NAV-HPPOSLLH':
                    data = {'data_type' : 'LLH',
                           'version' : parsed.version,
                           'reserved0' : parsed.reserved0,
                           'flags' : parsed._get_dict()['flags'],
                           'invalidLlh' : parsed.invalidLlh,
                           'iTOW' : parsed.iTOW,
                           'lon' : parsed.lon,
                           'lat' : parsed.lat,
                           'height' : parsed.height,
                           'hMSL' : parsed.hMSL,
                           'lonHp' : parsed._lonHp,
                           'latHp' : parsed._latHp,
                           'heightHp' : parsed._heightHp,
                           'hMSLHp' : parsed._hMSLHp,
                           'hAcc' : parsed.hAcc,
                           'vAcc' : parsed.vAcc}
                    response = requests.post(url, json=data)
                    print(response)
                    sleep(0.1)
                    
                if parsed.identity == 'NAV-STATUS':
                    data = {'data_type' : 'STATUS',
                            'iTOW' : parsed.iTOW,
                            'gpsFix' : parsed.gpsFix,
                            'flags' : parsed._get_dict()['flags'],
                            'gpsFixOk' : parsed.gpsFixOk,
                            'diffSoln' : parsed.diffSoln,
                            'wknSet' : parsed.wknSet,
                            'towSet' : parsed.towSet,
                            'fixStat' : parsed._get_dict()['fixStat'],
                            'diffCorr' : parsed.diffCorr,
                            'carrSolnValid' : parsed.carrSolnValid,
                            'mapMatching' : parsed.mapMatching,
                            'psmState' : parsed.psmState,
                            'spoofDetState' : parsed.spoofDetState,
                            'carrSoln' : parsed.carrSoln,
                            'ttff' : parsed.ttff,
                            'msss' : parsed.msss}
                    response = requests.post(url, json=data)
                    print(response)
                    sleep(0.1)

                if parsed.identity == 'NAV-HPPOSECEF':
                    data = {'data_type' : 'ECEF',
                            'version' : parsed.version,
                            'reserved0' : parsed.reserved0,
                            'iTOW' : parsed.iTOW,
                            'ecefX' : parsed.ecefX,
                            'ecefY' : parsed.ecefY,
                            'ecefZ' : parsed.ecefZ,
                            'ecefXHp' : parsed.ecefXHp,
                            'ecefYHp' : parsed.ecefYHp,
                            'ecefZHp' : parsed.ecefZHp,
                            'flags' : parsed._get_dict()['flags'],
                            'invalidEcef' : parsed.invalidEcef,
                            'pAcc' : parsed.pAcc}
                    response = requests.post(url, json=data)
                    print(response)
                    sleep(0.1)

parse_all(stream_path=file_path, url=url)