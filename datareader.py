from tqdm import tqdm

class dataReader:

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
					self.data.append([splittedLine[0], splittedLine[1], splittedLine[2], splittedLine[3],splittedLine[5],splittedLine[6],splittedLine[7],splittedLine[8],splittedLine[9],splittedLine[10], flow_type])
				elif len(splittedLine) == 13 and len(splittedLine[4]) == 0:
					flow_type = splittedLine[12].replace("\n", "")
					self.data.append([splittedLine[0], splittedLine[1], splittedLine[2], splittedLine[3],splittedLine[6],splittedLine[7],splittedLine[8],splittedLine[9],splittedLine[10],splittedLine[11], flow_type])
				elif len(splittedLine) == 13 and len(splittedLine[7]) == 0:
					flow_type = splittedLine[12].replace("\n", "")
					self.data.append([splittedLine[0], splittedLine[1], splittedLine[2], splittedLine[3],splittedLine[4],splittedLine[6],splittedLine[8],splittedLine[9],splittedLine[10],splittedLine[11], flow_type])
				elif len(splittedLine) == 14 and len(splittedLine[4]) == 0:
					flow_type = splittedLine[13].replace("\n", "")
					self.data.append([splittedLine[0], splittedLine[1], splittedLine[2], splittedLine[3],splittedLine[6],splittedLine[8],splittedLine[9],splittedLine[10],splittedLine[11], splittedLine[12], flow_type])



	def get_data(self):
		return self.data

