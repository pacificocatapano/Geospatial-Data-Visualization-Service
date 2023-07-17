from flask import render_template, session, redirect, url_for, request
import pandas as pd
from DB.DB import connectDB

def dati():
    connection = connectDB()

    ECEF =  pd.read_sql("SELECT * FROM HPPOSECEF", connection)  
    LLH =  pd.read_sql("SELECT * FROM HPPOSLLH", connection)
    STATUS = pd.read_sql("SELECT * FROM STATUS", connection)
    connection.close()
   
    if 'loggedin' in session:
         ECEF = ECEF.drop('ID',axis=1)
         LLH = LLH.drop('ID',axis=1)
         STATUS = STATUS.drop('ID',axis=1)
         html_table_ecef = ECEF.to_html(classes='table table-stripped')
         html_table_llh = LLH.to_html(classes='table table-stripped')
         html_table_status = STATUS.to_html(classes='table table-stripped')
            
         return render_template('dati.html' , table_ecef=html_table_ecef, table_llh=html_table_llh, table_status=html_table_status), 200
    return redirect(url_for('login'))

def acquisisciDati():
    data = request.json
    connection = connectDB()
    cursor = connection.cursor()
    if data['data_type'] == 'LLH':
        try:
            cursor.execute("INSERT INTO  HPPOSLLH (version, reserved0, invalidLlh, iTOW, lon, lat, height, hMSL, lonHp, latHp, heightHp, hMSLHp, hAcc, vAcc) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
                            (data['version'], data['reserved0'], data['invalidLlh'], data['iTOW'], data['lon'], data['lat'], data['height'], data['hMSL'], data['lonHp'], data['latHp'], data['heightHp'], data['hMSLHp'], data['hAcc'], data['vAcc']),)
            cursor.close()
            connection.commit()
            connection.close()
        except connection.IntegrityError:
            connection.close()
            return 'Acquisizione fallita LLH'
    elif data['data_type'] == 'STATUS':
        try:
            cursor.execute("INSERT INTO STATUS (iTOW, gpsFix, gpsFixOk, diffSoln, wknSet, towSet, diffCorr, carrSolnValid, mapMatching, psmState, spoofDetState, carrSoln, ttff, msss) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
                            (data['iTOW'], data['gpsFix'], data['gpsFixOk'], data['diffSoln'], data['wknSet'], data['towSet'], data['diffCorr'], data['carrSolnValid'], data['mapMatching'], data['psmState'], data['spoofDetState'], data['carrSoln'], data['ttff'], data['msss']),)
            cursor.close()
            connection.commit()
            connection.close()
        except connection.IntegrityError:
            connection.close()
            return 'Acquisizione fallita STATUS'
    else:
        try:
            cursor.execute("INSERT INTO HPPOSECEF (version, reserved0, iTOW, ecefX, ecefY, ecefZ, ecefXHp, ecefYHp, ecefZHp, invalidEcef, pAcc) values(?,?,?,?,?,?,?,?,?,?,?)", 
                            (data['version'], data['reserved0'], data['iTOW'], data['ecefX'], data['ecefY'], data['ecefZ'], data['ecefXHp'], data['ecefYHp'], data['ecefZHp'], data['invalidEcef'], data['pAcc']),)
            cursor.close()
            connection.commit()
            connection.close()
        except connection.IntegrityError:
            connection.close()
            return 'Acquisizione fallita ECEF'
        
    return 'Acquisizione terminata con successo!'
