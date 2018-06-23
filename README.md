# Profiling and Fingerprinting
Group members: Cas Buijs and Clinton Cao

# Datasets
For this assignment we use the CTU-13 dataset number 43 and number 51.

Information link:

https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-43/

https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-51/

Download link:

https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-43/capture20110811.pcap.netflow.labeled

https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-51/capture20110818.pcap.netflow.labeled

# Setup and Running the Python Scripts
We have provided a shell script (run.sh) that should install all required libraries and then execute the corresponding python scripts. We have tested our scripts both on Python 2.7.15 and Python 3.5.2. It is possible to modify the shell script to only a specific python script. To do this, open the shell script with your favourite editor and comment out the python scripts that you don't want to run.

**NOTE:** It is too big to put the datasets on the repository :-( , so you would have to make sure that you have downloaded the files yourself and rename them to the right name (e.g. rename **capture20110811.pcap.netflow.labeled** to **capture43.labeled** or rename **capture20110818.pcap.netflow.labeled** to **capture51.labeled**) before running the scripts.
