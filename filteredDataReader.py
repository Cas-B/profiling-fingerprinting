from tqdm import tqdm

class dataReaderFiltered:

	def __init__(self, filePath):
		self.data = []

		with open(filePath, 'r') as flowData:
			count = 0
			for line in tqdm(flowData):
				if count == 0:
					count += 1
					continue

				splittedLine =  line.split("\t")

				if len(splittedLine) == 12:
					flow_type = splittedLine[11].replace("\n", "")
					if flow_type != "Background":
						self.data.append([splittedLine[0], splittedLine[1], splittedLine[2], splittedLine[3],splittedLine[5],splittedLine[6],splittedLine[7],splittedLine[8],splittedLine[9],splittedLine[10], flow_type])
				elif len(splittedLine) == 13 and len(splittedLine[4]) == 0:
					flow_type = splittedLine[12].replace("\n", "")
					if flow_type != "Background":
						self.data.append([splittedLine[0], splittedLine[1], splittedLine[2], splittedLine[3],splittedLine[6],splittedLine[7],splittedLine[8],splittedLine[9],splittedLine[10],splittedLine[11], flow_type])
				elif len(splittedLine) == 13 and len(splittedLine[7]) == 0:
					flow_type = splittedLine[12].replace("\n", "")
					if flow_type != "Background":
						self.data.append([splittedLine[0], splittedLine[1], splittedLine[2], splittedLine[3],splittedLine[4],splittedLine[6],splittedLine[8],splittedLine[9],splittedLine[10],splittedLine[11], flow_type])
				elif len(splittedLine) == 14 and len(splittedLine[4]) == 0:
					flow_type = splittedLine[13].replace("\n", "")
					if flow_type != "Background":
						self.data.append([splittedLine[0], splittedLine[1], splittedLine[2], splittedLine[3],splittedLine[6],splittedLine[8],splittedLine[9],splittedLine[10],splittedLine[11], splittedLine[12], flow_type])



	def get_data(self):
		return self.data

	def get_data_from(self, ip):
		ip_data = []
		for i in tqdm(range(len(self.data))):
			if self.data[i][3].split(":")[0] == str(ip) or self.data[i][4].split(":")[0] == str(ip):
				ip_data.append(self.data[i])
		return ip_data

	def write_to_file(self, filePath):
		try:
			filet = open(filePath, "w") 
			for i in tqdm(range(len(self.data))):
				if self.data[i][10] == "":
					print ("a")
					print(str(self.data[i]))
				filet.write(str(self.data[i]))
				filet.write("\n")
			filet.close() 
		except:
			print("Your pc sucks!")

reader = dataReaderFiltered("capture51.labeled")
reader.write_to_file("filtered51.labeled")

