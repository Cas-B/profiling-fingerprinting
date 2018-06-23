#!/bin/sh

# Install required python libraries.
sudo -i python3 -m pip install --upgrade pip
sudo python3 -m pip install -U pip
sudo python3 -m pip install -U numpy
sudo python3 -m pip install -U saxpy
sudo python3 -m pip install -U matplotlib
sudo python3 -m pip install -U tqdm
sudo python3 -m pip install -U mmh3
sudo apt-get install python3-tk


################################################
#### Run each python files for each task #######
################################################

######### Min-Wise Sampling #####################
python3 run_min-wise_sampling.py

######### Count-min Sketch ######################
python3 run_cms.py

######### Discretisation  ######################
python3 discretise.py
python3 visualisation.py

######### Profiling ######################
python3 profiling.py
