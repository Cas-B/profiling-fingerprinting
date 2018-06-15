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
	ip = reader[i][3].split(":")[0]
	cms.add(ip)
	if listOfIPs.get(ip) is None and ip is not "147.32.84.165":
		listOfIPs[ip] = 1
listOfIPs = list(listOfIPs.keys())

#Create frequencies
for i in tqdm(range(len(listOfIPs))):
	listOfIPs[i] = (listOfIPs[i], cms.query(listOfIPs[i]))
	
#Getting the top 10 most frequent values, taking into account the removal of the host the detection took place on.
listOfIPs.sort(key=lambda x: x[1], reverse=True)
listOfIPs = [listOfIPs[i] for i in range(10)]

for i in range(10):
	frequency = listOfIPs[i][1]/len(reader) * 100
	print (listOfIPs[i][0] + " " + str(frequency))

