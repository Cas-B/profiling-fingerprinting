import random
import operator
from tqdm import tqdm


# This class represent an object that could be used to do min wise sampling.
class minWiseSampling:

    ############# Constructor ##################
    def __init__(self, reservoir_size, host_ip):
        self.host_ip = host_ip
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
            src_ip = row[3].split(":")[0]
            dest_ip = row[4].split(":")[0]
            if src_ip != self.host_ip:
                temp_dict[tag] = src_ip
            if dest_ip != self.host_ip:
                temp_dict[tag2] = dest_ip

        print("Selecting the k elements with the lowest tag")
        for tag in tqdm(sorted(temp_dict.keys())):
            if len(self.elements_dict) < self.reservoir_size:
                self.elements_dict[tag] = temp_dict[tag]

    # Get the k sample elements.
    def get_elements(self):
        return self.elements_dict
