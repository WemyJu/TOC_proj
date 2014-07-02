#Real price predictor

#USAGE

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
