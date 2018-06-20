import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from datahandler import dataHandler

handler = dataHandler()
handler.read_data("capture51.labeled")
handler.filter_background_data()
netflows = np.array(handler.get_filtered_data())
infected = np.array(handler.get_ip_data("147.32.84.165"))
protocols = [netflows[i][2] for i in range(len(netflows))]
protocol = [infected[i][2] for i in range(len(infected))]

print("Show relation between protocol use")
plt.plot(protocols, color="red")
plt.plot(protocol,color="blue")
plt.show()
