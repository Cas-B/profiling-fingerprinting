import numpy as np
import mmh3

class count_min_sketch():

	def __init__(self, w, d):
		self.matrix = np.zeros(shape=(w,d))
		self.w = w
		self.d = d

	def generate_hashkeys(self):
		self.hashkeys = []
		for i in range(self.w):
			self.hashkeys.append(200 + i)

	def add(self, item):
		for i in range(self.w):
			value = mmh3.hash(item, self.hashkeys[i]) % self.d
			self.matrix[i][value] += 1
			
