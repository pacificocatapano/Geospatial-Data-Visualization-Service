from flask import render_template, session, redirect, url_for, request
import pyubx2
import pandas as pd
from DB.DB import connectDB
import os

def parse_all(stream_path):
    LLH = []
    ECEF = []
    STATUS = []
    with open(stream_path, 'rb') as stream:
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
                                   parsed.mapMatching,
                                   parsed.psmState,
                                   parsed.spoofDetState,
                                   parsed.carrSoln,
                                   parsed.ttff,
                                   parsed.msss])
                    
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
                     'mapMatching',
                     'psmState',
                     'spoofDetState',
                     'carrSoln',
                     'ttff',
                     'msss']
    
    LLH = pd.DataFrame(LLH, columns=schema_llh)
    STATUS = pd.DataFrame(STATUS, columns=schema_status)
    ECEF = pd.DataFrame(ECEF, columns=schema_ecef)

    return LLH, ECEF, STATUS
def dati():
    # Esempio di dati per le tabelle
    #Query nel database
    connection = connectDB()
    #   QUERY Dataframe into SQL Server:
    ECEF =  pd.read_sql("SELECT * FROM HPPOSECEF", connection)  
    LLH =  pd.read_sql("SELECT * FROM HPPOSLLH", connection)
    STATUS = pd.read_sql("SELECT * FROM STATUS", connection)
    connection.close()
   


    if 'loggedin' in session:
         ECEF = ECEF.drop('ID',axis=1)
         LLH = LLH.drop('ID',axis=1)
         STATUS = STATUS.drop('ID',axis=1)
        # Converte le tabelle in stringhe HTML
         html_table_ecef = ECEF.to_html(classes='table table-stripped')
         html_table_llh = LLH.to_html(classes='table table-stripped')
         html_table_status = STATUS.to_html(classes='table table-stripped')
            
         return render_template('dati.html' , table_ecef=html_table_ecef, table_llh=html_table_llh, table_status=html_table_status)
    return redirect(url_for('login'))



def acquisisciDati():
    file = request.files['file']  # Ottieni il file dalla richiesta
    path = os.path.join('tmp', 'file.ubx')
    file.save(path)    
    LLH, ECEF, STATUS = parse_all(path)
    os.remove(path)
    """
    ECEF
    """
    connection = connectDB()
    cursor = connection.cursor()
    try:
        for index, row in ECEF.iterrows():
             cursor.execute("INSERT INTO HPPOSECEF (version, reserved0, iTOW, ecefX, ecefY, ecefZ, ecefXHp, ecefYHp, ecefZHp, invalidEcef, pAcc) values(?,?,?,?,?,?,?,?,?,?,?)", 
                            (row.version, row.reserved0, row.iTOW, row.ecefX, row.ecefY, row.ecefZ, row.ecefXHp, row.ecefYHp, row.ecefZHp, row.invalidEcef, row.pAcc),)
        cursor.close()
        connection.commit()
        connection.close()
    except connection.IntegrityError:
        connection.close()
        return 'Acquisizione fallita ECEF'
    
    """
    SLLH
    """
    connection = connectDB()
    cursor = connection.cursor()
    try:
        for index, row in LLH.iterrows():
             cursor.execute("INSERT INTO  HPPOSLLH (version, reserved0, invalidLlh, iTOW, lon, lat, height, hMSL, lonHp, latHp, heightHp, hMSLHp, hAcc, vAcc) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
                            (row.version, row.reserved0, row.invalidLlh, row.iTOW, row.lon, row.lat, row.height, row.hMSL, row.lonHp, row.latHp, row.heightHp, row.hMSLHp, row.hAcc, row.vAcc),)
        cursor.close()
        connection.commit()
        connection.close()
    except connection.IntegrityError:
        connection.close()
        return 'Acquisizione fallita LLH'
    
    connection = connectDB()
    cursor = connection.cursor()
    try:
        for index, row in STATUS.iterrows():
             cursor.execute("INSERT INTO STATUS (iTOW, gpsFix, gpsFixOk, diffSoln, wknSet, towSet, diffCorr, carrSolnValid, mapMatching, psmState, spoofDetState, carrSoln, ttff, msss) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
                            (row.iTOW, row.gpsFix, row.gpsFixOk, row.diffSoln, row.wknSet, row.towSet, row.diffCorr, row.carrSolnValid, row.mapMatching, row.psmState, row.spoofDetState, row.carrSoln, row.ttff, row.msss),)
        cursor.close()
        connection.commit()
        connection.close()
    except connection.IntegrityError:
        connection.close()
        return 'Acquisizione fallita STATUS'
    
    return 'Acquisizione terminata correttamente'

