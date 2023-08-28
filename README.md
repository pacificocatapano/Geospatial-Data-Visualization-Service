# Geospatial Data Visualization Service &#x1F30D;

The application has been designed to meet the needs of users working with geospatial data, providing them with a dedicated environment for storing and visualizing geospatial data. 

This data comes from global positioning systems with centimeter-level accuracy.
Our system needs to receive coordinates from an external computer, save them in a database, and then display and filter them.

The application is composed from:
* An unique external entity that sends data to our service;
* The service itself (server);
* An User Interface that run on browser (client).

## Installation guide

### Requirements

Before you begin, make sure you have Anaconda installed on your system. If you haven't done it yet, you can download it from [Anaconda download link](https://www.anaconda.com/download).

### Installation

#### 1. Clone the repository

```bash
git clone https://github.com/pacificocatapano/Geospatial-Data-Visualization-Service.git
cd Geospatial-Data-Visualization-Service
```

#### 2. Create a conda environment (optional but recommended)

Creating a conda environment will help you keep the application's dependencies separate from the system-wide packages.

```bash
conda create -n environment_name python=3.x
```

Activate the conda environment:

(Windows)
```bash
conda activate environment_name
```

(Linux/Mac):
```bash
source activate environment_name
```

#### 3. Install dependencies

Make sure your conda environment is activated. Then, install the application's dependencies using conda or pip, depending on your preference.

Using conda:
```bash
conda install --file requirements.txt
```

Using pip (if the package is not available in conda):
```bash
pip install -r requirements.txt
```

This will install all the necessary libraries for the application.

#### 4. Configuration
Suppose we are in project folder.

##### 4.1 Run server
Run the following command:
```bash
cd Codice
python app.py
```
We have set a local ip address as example: 127.0.0.1:5000.

Now we should open our browser and on address bar write: [http://127.0.0.1:5000/]( http://127.0.0.1:5000/)

##### 4.2 Load Data on server
Open another Anaconda Terminal and type:
```bash
cd Geospatial-Data-Visualization-Service

python iotdevice.py
```

Now our data should be send every second, and on our UI, ticking auto-update option we can see it updating in real-time.

### Troubleshooting

If you encounter any issues during the installation or execution of the application, check the following points:

* Ensure you have followed all the installation steps correctly.
* Verify that Anaconda has been installed correctly and the conda environment is activated.
* Refer to the repository's documentation for any known issues or solutions.




