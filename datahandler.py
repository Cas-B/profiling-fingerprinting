from tqdm import tqdm

class dataHandler:

	def __init__(self):
		self.original_data = []
		self.filtered_data = []

	#Reads the original data from the capture dataset and turns each line into an array consisting the necessary features of the original data
	def read_data(self, filePath):
		with open(filePath, 'r') as flowData:
			count = 0
			for line in tqdm(flowData):
				if count == 0:
					count += 1
					continue

				splittedLine =  line.split("\t")

				if len(splittedLine) == 12:
					flow_type = splittedLine[11].replace("\n", "")
					self.original_data.append([splittedLine[0], splittedLine[1], splittedLine[2], splittedLine[3],splittedLine[5],splittedLine[6],splittedLine[7],splittedLine[8],splittedLine[9],splittedLine[10], flow_type])
				elif len(splittedLine) == 13 and len(splittedLine[4]) == 0:
					flow_type = splittedLine[12].replace("\n", "")
					self.original_data.append([splittedLine[0], splittedLine[1], splittedLine[2], splittedLine[3],splittedLine[6],splittedLine[7],splittedLine[8],splittedLine[9],splittedLine[10],splittedLine[11], flow_type])
				elif len(splittedLine) == 13 and len(splittedLine[7]) == 0:
					flow_type = splittedLine[12].replace("\n", "")
					self.original_data.append([splittedLine[0], splittedLine[1], splittedLine[2], splittedLine[3],splittedLine[4],splittedLine[6],splittedLine[8],splittedLine[9],splittedLine[10],splittedLine[11], flow_type])
				elif len(splittedLine) == 14 and len(splittedLine[4]) == 0:
					flow_type = splittedLine[13].replace("\n", "")
					self.original_data.append([splittedLine[0], splittedLine[1], splittedLine[2], splittedLine[3],splittedLine[6],splittedLine[8],splittedLine[9],splittedLine[10],splittedLine[11], splittedLine[12], flow_type])


	#Filters out all data with a label 'Background'
	def filter_background_data(self):
		for i in tqdm(range(len(self.original_data))):
			if self.original_data[i][10] != "Background":
				self.filtered_data.append(self.original_data[i])

	#Returns all the data which has as source of destionation ip-address the variable `ip` from the filtered data
	def get_ip_data(self, ip):
		ip_data = []
		for i in tqdm(range(len(self.filtered_data))):
			if self.filtered_data[i][3].split(":")[0] == str(ip) or self.filtered_data[i][4].split(":")[0] == str(ip):
				ip_data.append(self.filtered_data[i])
		return ip_data

	#Returns all the data which has as source of destionation ip-address the variable `ip` from the provided data
	def get_ip_data(self, ip, data):
		ip_data = []
		for i in tqdm(range(len(data))):
			if data[i][3].split(":")[0] == str(ip) or data[i][4].split(":")[0] == str(ip):
				ip_data.append(data[i])
		return ip_data

	def get_original_data(self):
		return self.original_data

	def get_filtered_data(self):
		return self.filtered_data

	#Write all the arrays to a file
	def write_original_data_to_file(self, filePath):
		try:
			openedFile = open(filePath, "w") 
			for i in tqdm(range(len(self.original_data))):
				openedFile.write(str(self.original_data[i]))
				openedFile.write("\n")
			openedFile.close() 
		except:
			print("Your pc sucks!")

	#Write the data without background flows to a file
	def write_filtered_data_to_file(self, filePath):
		try:
			openedFile = open(filePath, "w") 
			for i in tqdm(range(len(self.filtered_data))):
				openedFile.write(str(self.filtered_data[i]))
				openedFile.write("\n")
			openedFile.close() 
		except:
			print("Your pc sucks!")

	#Write data to a file
	def write_to_file(self, filePath, data):
		try:
			openedFile = open(filePath, "w") 
			for i in tqdm(range(len(data))):
				openedFile.write(str(data[i]))
				openedFile.write("\n")
			openedFile.close() 
		except:
			print("Your pc sucks!")



