import random
import operator
from tqdm import tqdm


# This class represent an object that could be used to do min wise sampling.
class minWiseSampling:

    ############# Constructor ##################
    def __init__(self, reservoir_size):
        self.elements_dict = dict() # dictionary to store the k elements with the smallest random tags.
        self.reservoir_size = reservoir_size

    ########### Do min wise sampling on the data that is provided to this function ########
    def sample(self, data):
        temp_dict = dict() # temporary dictionary to store the tags of the elements.
        print("Creating tags for the elements")
        for row in tqdm(data):
            # create tags in the interval of [0,1]
            tag = random.uniform(0, 1)
            tag2 = random.uniform(0, 1)
            temp_dict[tag] = row[3]
            temp_dict[tag2] = row[4]

        print("Selecting the k elements with the lowest tag")
        for tag in tqdm(sorted(temp_dict.keys())):
            if len(self.elements_dict) < self.reservoir_size:
                self.elements_dict[tag] = temp_dict[tag]

    def get_elements(self):
        return self.elements_dict
