# ArcPro Service Area Analysis Layer and Solver
Build a service analysis layer using ArcPy functions and a executing with a Python 3 script

* Prerequisites and Insights
  * Installed and running Anaconda (version 2 OR 3)
  * Access Anaconda in cmd prompt using __conda__ cmd
  * ArcPro Version 2.3.2 runs Python 3.6.6
  * Text editor (i.e. NotePad++) or IDE Code editor (i.e. Visual Studio Code)


## 1.) Create/Establish Virtual Environment 
Establish ArcPro virtual environment to run arcpy with the specific Python version compatible for ArcPro.
### 1.1) Copy ArcPro Python env folder to Anaconda version Python env
* Navigate to: __C:\Program Files\ArcGIS\Pro\bin\Python\envs__
* Copy folder __arcgispro-py3__ to __C:\Users\User_Name\AppData\Local\Continuum\anaconda2\envs__
* Rename __arcgispro-py3__ to __arcpro_py3__
### 1.2) Test whether the arcpro_py3 environment can be activated
* Open cmd prompt
* Type: 
```conda activate arcpro_py3```
* User should now see __(arcpro_py3) C:\WINDOWS\System32__ or some instantiation with the prefix __(arcpro_py3)__

## 2.) Test ArcPy library
* Open cmd and activate virual environment arcpro_py3
* Type: ```python``` and python version 3.6.6 console should appear in cmd window
* Type: ```>>> import arcpy``` and arcpy should successully be imported
* If interested in package contents of ArcPy then in the python console type ```>>> help(arcpy)```

## 3.) Update and Run ArcPro_ODCost_Matrix_Calc.py Script
* Change file paths in script to accomodate your specific environment setup
* ```(arcpro_py3) C:\Path\to\PythonScript> python ArcPro_ODCost_Matrix_Calc.py```
