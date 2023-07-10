DROP TABLE IF EXISTS Utenti;


CREATE TABLE IF NOT EXISTS 'Utenti' (
	Nome VARCHAR(50),
	Cognome VARCHAR(50),
	Email VARCHAR(50) PRIMARY KEY,
	Password VARCHAR(50),
	UNIQUE(Email)
);

CREATE TABLE IF NOT EXISTS 'HPPOSLLH' (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
	version TEXT,
	reserved0 TEXT,
	invalidLlh BOOLEAN,
	iTOW INT,
	lon REAL(10, 7),
	lat REAL(10, 7),
	height INT,
	hMSL INT,
	lonHp REAL(10, 9),
	latHp REAL(10, 9),
	heightHp INT,
	hMSLHp INT,
	hAcc INT,
	vAcc INT
);

CREATE TABLE IF NOT EXISTS 'HPPOSECEF' (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
	version TEXT,
	reserved0 TEXT,
	iTOW INT,
	ecefX DOUBLE,
	ecefY DOUBLE,
	ecefZ DOUBLE,
	ecefXHp DOUBLE,
	ecefYHp DOUBLE,
	ecefZHp DOUBLE,
	invalidEcef BOOLEAN,
	pAcc INT
);

CREATE TABLE IF NOT EXISTS 'STATUS' (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
	iTOW INT,
	gpsFix TEXT,
	gpsFixOk BOOLEAN,
	diffSoln BOOLEAN,
	wknSet BOOLEAN,
	towSet BOOLEAN,
	diffCorr BOOLEAN,
	carrSolnValid BOOLEAN,
	mapMatching INT,
	psmState INT,
	spoofDetState INT,
	carrSoln INT,
	ttff INT,
	msss INT
);