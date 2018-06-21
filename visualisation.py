import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from datahandler import dataHandler
from datetime import datetime

handler = dataHandler()
handler.read_data("capture51.labeled")
handler.filter_background_data()
netflows = np.array(handler.get_filtered_data())
infected = np.array(handler.get_ip_data("147.32.84.165"))

times = [datetime.strptime(infected[i][0], "%Y-%m-%d %H:%M:%S.%f") for i in range(len(infected))]
protocols = [infected[i][2] for i in range(len(infected))]
bytes = [int(infected[i][7]) for i in range(len(infected))]

print("Show usage of protocols")
plt.plot(times, protocols, color="red")
plt.show()


print("Show the amount of bytes used")
plt.plot(times, bytes)
plt.show()
