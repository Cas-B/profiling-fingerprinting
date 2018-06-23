import numpy as np
from datahandler import dataHandler

from saxpy.znorm import znorm
from saxpy.sax import ts_to_string
from saxpy.alphabet import cuts_for_asize

def discretise(data, number_of_bins):
	return ts_to_string(znorm(data), cuts_for_asize(number_of_bins))

#Read in the data
handler = dataHandler()
handler.read_data('capture51.labeled')
handler.filter_background_data()
data = handler.get_filtered_data() #To discretize the original data, get the original data here
durations = [float(data[i][1]) for i in range(len(data))]
packets = [float(data[i][7]) for i in range(len(data))]
bytes = [float(data[i][8]) for i in range(len(data))]


#Discretize the data
discretised_durations = discretise(durations, 8)
discretised_packets = discretise(durations, 10)
discretised_bytes = discretise(durations, 20)


#Store the discretization results in the original data
for i in range(len(data)):
	item = data[i]
	item[1] = discretised_durations[i]
	item[7] = discretised_packets[i]
	item[8] = discretised_bytes[i]
	item.append(data[i][2] + discretised_bytes[i])
	data[i] = item


#Write the data to a file
ip_specific = handler.get_ip_specific_data("147.32.84.165", data)
handler.write_to_file("discretised_data.labeled", data)
handler.write_to_file("discretised_ip_data.labeled", ip_specific)
