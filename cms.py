import numpy as np
import mmh3

class count_min_sketch():

	def __init__(self, w, d):
		self.matrix = np.zeros(shape=(w,d))
		self.w = int(w)
		self.d = int(d)

	def generate_hashkeys(self):
		self.hashkeys = []
		for i in range(self.w):
			self.hashkeys.append(int(200 + i))

	def add(self, item):
		for i in range(self.w):
			value = mmh3.hash(item, self.hashkeys[i]) % self.d
			self.matrix[i][int(value)] += 1

	def get_columns(self, item):
		return [mmh3.hash(item, self.hashkeys[i]) % self.d for i in range(self.w)]

	def get_matrix(self):
		return self.matrix

	def query(self, item):
		column_values = [self.matrix[i][int(mmh3.hash(item, self.hashkeys[i])) % self.d] for i in range(self.w)]
		return min(column_values)
			
