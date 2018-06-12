class dataReader:

	def __init__(self, filePath):
		self.data = []

		with open(filePath, 'r') as flowData:
			count = 0
			for line in flowData:
				if count == 0:
					count += 1
					continue
				
				splittedLine =  line.split("\t")
				
				if len(splittedLine[4]) == 0:
					data.append([splittedLine[0], splittedLine[1], splittedLine[2], splittedLine[3],splittedLine[6],splittedLine[7],splittedLine[8],splittedLine[9],splittedLine[10],splittedLine[11], splittedLine[12][:-1]])
				else:
					data.append([splittedLine[0], splittedLine[1], splittedLine[2], splittedLine[3],splittedLine[5],splittedLine[6],splittedLine[7],splittedLine[8],splittedLine[9],splittedLine[10], splittedLine[11][:-1]])

	def get_data():
		return self.data
