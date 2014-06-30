#Real price predictor

#USAGE

#REQUIREMENT
python3 and the libraries specified in requirements.txt  

There are some dependency problem.  
You should install gfortran and libatlas-base-dev first, then you can install libraries through
```shell
pip3 install -r requirements.txt
```
* note that openpyxl whose version is not in between 1.6.1 and 2.0.0 would be incompatible to some of the other libraries.
  
If statsmodels still cannot be installed, try 
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
