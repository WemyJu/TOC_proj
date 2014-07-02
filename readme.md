#Real price predictor

#USAGE
There are two main parts in this project, regression generator and real price estimator.

##Regression Generator
```python
python3 regression_generator.py [dataID]
```
You can generate regression information and find the result in folder regression_resutlt.  

The argument dataID is optional. Its default value is 5365dee31bc6e9d9463a0057.  
If you want to use your own data, you have to enter the ID that DataGarage generate.  
Note that your data must have the same format as default data's.  

##Real price estimator
```python
python3 real_price_estimator.py
```
Enter the value as interactive shell ask, and you'll get the predicted price.  
If the regression functions have not been genterate, it will automatically generate through default data.

#PREREQEUISITES
python3
libraries : numpy, statsmodels  
You sholud install some other packages before install statsmodels.  
All the instructions are below.

##Dependency Problem
###For mac user
```shell
brew install gfortran
pip3 install -r requirements.txt
```
###For Ubuntu user
```shell
sudo apt-get install libatlas-base-dev gfortran
sudo pip3 install -r requirements.txt
```
* note that openpyxl whose version is not in between 1.6.1 and 2.0.0 would be incompatible to some of the other libraries. (This is handled through requirements.txt)

##Get the lastest statsmodels
```shell
cd tmp
git clone https://github.com/statsmodels/statsmodels.git 
cd statsmodels
python3 setup.py build
sudo python3 setup.py install
```

#AUTHORS
[WemyJu] (https://github.com/WemyJu)  
[Lee-W] (https://github.com/Lee-W/)

#LICENSE
MIT
