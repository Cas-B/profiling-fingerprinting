import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from filteredDataReader import dataReaderFiltered

reader = dataReaderFiltered("capture.labeled")
netflows = np.array(reader.get_data())[:1000]
infected_data = reader.get_data_from("147.32.84.165")[:1000]

column_infected = []
for i in range(np.shape(infected_data)[0]):
	column_infected.append(infected_data[i][6])
#6,7,8,9
column= []
for i in range(np.shape(netflows)[0]):
	column.append(netflows[i][6])

plt.plot(column_infected, color="blue")
plt.plot(column, color="red")
plt.show()

column_infected = []
for i in range(np.shape(infected_data)[0]):
	column_infected.append(infected_data[i][7])
#6,7,8,9
column= []
for i in range(np.shape(netflows)[0]):
	column.append(netflows[i][7])

plt.plot(column_infected, color="blue")
plt.plot(column, color="red")
plt.show()

column_infected = []
for i in range(np.shape(infected_data)[0]):
	column_infected.append(infected_data[i][8])
#6,7,8,9
column= []
for i in range(np.shape(netflows)[0]):
	column.append(netflows[i][8])

plt.plot(column_infected, color="blue")
plt.plot(column, color="red")
plt.show()

column_infected = []
for i in range(np.shape(infected_data)[0]):
	column_infected.append(infected_data[i][9])
#6,7,8,9
column= []
for i in range(np.shape(netflows)[0]):
	column.append(netflows[i][9])

plt.plot(column_infected, color="blue")
plt.plot(column, color="red")
plt.show()

