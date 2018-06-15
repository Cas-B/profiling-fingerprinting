from cms import count_min_sketch
from datareader import dataReader
from tqdm import tqdm

#Setup
reader = dataReader("capture.labeled").get_data()
cms = count_min_sketch(15, 50)
cms.generate_hashkeys()

#Create count-min-sketch
listOfIPs = dict()

for i in tqdm(range(len(reader))):
	source_ip = reader[i][3].split(":")[0]
	destination_ip = reader[i][4].split(":")[0]
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
	frequency = listOfIPs[i][1]/(2*len(reader)) * 100
	print (listOfIPs[i][0] + " " + str(frequency))
	print (listOfIPs[i][1])

