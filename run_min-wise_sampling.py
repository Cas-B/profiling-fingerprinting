from minwisesampling import minWiseSampling
import operator
from tqdm import tqdm
import math
from datahandler import dataHandler

## Update the frequency of an element in the dictionary ##
def updateDictElementFreq(freqDict, element):
    if element in freqDict:
        freqDict[element] += 1
    else:
        freqDict[element] = 1

## Calculate the frequency of the other IP addresses ##
def findIPFreqFromData(data, host_ip):
    freqDict = dict()
    for row in tqdm(data):
        src_ip = row[3].split(":")[0]
        dest_ip = row[4].split(":")[0]

        if src_ip != host_ip:
            updateDictElementFreq(freqDict, row[3].split(":")[0])
        if dest_ip != host_ip:
            updateDictElementFreq(freqDict, row[4].split(":")[0])

    return freqDict

print("Reading in the data")
data_handler = dataHandler()
data_handler.read_data("capture43.labeled")
data = data_handler.get_original_data()
host_ip = "147.32.84.165"

print("Calculating the actual frequencies of other IP addresses")
# Find the actual frequency of the other IP addresses.
freq = findIPFreqFromData(data, host_ip)

print(sorted(freq.items(), key=operator.itemgetter(1), reverse=True)[0:10]) # sort the dictionary by values (this returns a list of tuples).


print ("Sampling data using Min-Wise Sampling")
reservoir_size = math.floor(0.1 * len(data * 2))
mws = minWiseSampling(int(reservoir_size), host_ip)
mws.sample(data)
sampled_elements = mws.get_elements()
sampled_elements_freq = dict()

## Calculate the frequency from sample elements
print("Calculating the frequency of the sampled elements")
for element in tqdm(sampled_elements):
    updateDictElementFreq(sampled_elements_freq, sampled_elements[element])

for element in tqdm(sampled_elements_freq):
    sampled_freq = sampled_elements_freq[element]
    factor = float(sampled_freq / reservoir_size)
    sampled_elements_freq[element] = int(math.floor(len(data) * 2 * factor))

print (sorted(sampled_elements_freq.items(), key=operator.itemgetter(1), reverse=True)[0:10])
