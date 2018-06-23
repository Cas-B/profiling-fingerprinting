from tqdm import tqdm
import numpy as np

#Provides general statistical information about the processed, not original, data. The data is provided in the shapes of arrays
def read_statistics(filePath):
	with open(filePath, 'r') as flowData:
		duration = dict()
		port = dict()
		tos = dict()
		packets = dict()
		bytes = dict()
		flows = dict()
		for line in tqdm(flowData):
			splittedLine = line.replace("'", "")
			splittedLine = splittedLine.replace("[", "")
			splittedLine = splittedLine.replace("]", "")
			splittedLine = splittedLine.replace(" ", "")
			splittedLine = splittedLine.split(",")


			duration[splittedLine[1]] = 1
			src_prt = np.array(splittedLine[3].split(":"))
			dst_prt = np.array(splittedLine[4].split(":"))
			

			if(len(src_prt) == 2):
				port[splittedLine[3].split(":")[1]] = 1
			if(len(dst_prt) == 2):
				port[splittedLine[4].split(":")[1]] = 1

			tos[splittedLine[6]] = 1
			packets[splittedLine[7]] = 1
			bytes[splittedLine[8]] = 1
			flows[splittedLine[9]] = 1
		
		print("Statistics")
		print("Unique number of durations: ", len(duration.keys()))
		print("Unique number of ports: ", len(port.keys()))
		print("Unique number of tos: ", len(tos.keys()))
		print("Unique number of packets: ", len(packets.keys()))
		print("Unique number of bytes: ", len(bytes.keys()))
		print("Unique number of flows: ", len(flows.keys()))
		print("\n")
		print("Max duration: ", max(duration.keys()))
		print("Max port: ", max(port.keys()))
		print("Max tos: ", max(tos.keys()))
		print("Max packets: ", max(packets.keys()))
		print("Max bytes: ", max(bytes.keys()))
		print("Max flow: ", max(flows.keys()))
		print("\n")
		print("Min duration: ", min(duration.keys()))
		print("Min port: ", min(port.keys()))
		print("Min tos: ", min(tos.keys()))
		print("Min packets: ", min(packets.keys()))
		print("Min bytes: ", min(bytes.keys()))
		print("Min flow: ", min(flows.keys()))

#Counts the occurrences of a specific protocol
def statistics_count_protocol(filePath, protocol):
	with open(filePath, 'r') as flowData:
		counter = 0

		for line in tqdm(flowData):
			splittedLine = line.replace("'", "")
			splittedLine = splittedLine.replace("[", "")
			splittedLine = splittedLine.replace("]", "")
			splittedLine = splittedLine.replace(" ", "")
			splittedLine = splittedLine.split(",")

			if splittedLine[2] == str(protocol):
				counter += 1

		print("Counted: ",counter)

read_statistics('filtered51.labeled')
#statistics_count_protocol('filtered51.labeled', "ICMP")
#statistics_count_protocol('filtered_ip.labeled', "ICMP")

