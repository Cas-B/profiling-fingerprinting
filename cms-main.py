from cms import count_min_sketch
from datareader import dataReader

#Setup
reader = dataReader("traffic_data43_truncated.labeled").get_data()
cms = count_min_sketch(150, 50)
cms.generate_hashkeys()

#Create count-min-sketch
listOfIPs = []

for i in range(len(reader)):
	ip = reader[i][3].split(":")[0]
	cms.add(ip)
	if ip not in listOfIPs:
		listOfIPs.append(ip)

#Create frequencies
for i in range(len(listOfIPs)):
	listOfIPs[i] = (listOfIPs[i], cms.query(listOfIPs[i]))
	
#Getting the top 10 most frequent values, taking into account the removal of the host the detection took place on.
listOfIPs.sort(key=lambda x: x[1], reverse=True)
listOfIPs = [listOfIPs[i] for i in range(11)]
del listOfIPs[0]

for i in range(10):
	frequency = listOfIPs[i][1]/len(reader) * 100
	print listOfIPs[i][0] + " " + str(frequency)

