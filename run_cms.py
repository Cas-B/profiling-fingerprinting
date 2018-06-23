from cms import count_min_sketch
from datahandler import dataHandler
from tqdm import tqdm

#Setup
data_handler = dataHandler()
data_handler.read_data("capture43.labeled")
data = data_handler.get_original_data()
cms = count_min_sketch(15, 50)
cms.generate_hashkeys()

#Create count-min-sketch
listOfIPs = dict()

for i in tqdm(range(len(data))):
	source_ip = data[i][3].split(":")[0]
	destination_ip = data[i][4].split(":")[0]
	cms.add(source_ip)
	cms.add(destination_ip)
	if listOfIPs.get(source_ip) is None and source_ip != "147.32.84.165":
		listOfIPs[source_ip] = 1
	if listOfIPs.get(destination_ip) is None and destination_ip != "147.32.84.165":
		listOfIPs[destination_ip] = 1
listOfIPs = list(listOfIPs.keys())

#Create frequencies
for i in tqdm(range(len(listOfIPs))):
	listOfIPs[i] = (listOfIPs[i], cms.query(listOfIPs[i]))

#Getting the top 10 most frequent values, taking into account the removal of the host the detection took place on.
listOfIPs.sort(key=lambda x: x[1], reverse=True)
listOfIPs = [listOfIPs[i] for i in range(10)]

for i in range(10):
	frequency = listOfIPs[i][1]/(2*len(data)) * 100
	print (listOfIPs[i][0] + " " + str(frequency))
	print (listOfIPs[i][1])
