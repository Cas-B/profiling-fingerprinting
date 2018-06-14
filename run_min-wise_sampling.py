from datareader import  dataReader
from minwisesampling import minWiseSampling
import operator
from tqdm import tqdm
import math

## Update the frequency of an element in the dictionary ##
def updateDictElementFreq(freqDict, element):
    if element in freqDict:
        freqDict[element] += 1
    else:
        freqDict[element] = 1

## Calculate the frequency of the other IP addresses ##
def findIPFreqFromData(data):
    freqDict = dict()
    for row in tqdm(data):
        updateDictElementFreq(freqDict, row[3])
        updateDictElementFreq(freqDict, row[4])

    return freqDict

print("Reading in the data")
data = dataReader("test.labeled").get_data()

print("Calculating the actual frequencies of other IP addresses")
# Find the actual frequency of the other IP addresses.
freq = findIPFreqFromData(data)

frequent_ips = sorted(freq.items(), key=operator.itemgetter(1), reverse=True) # sort the dictionary by values (this returns a list of tuples).
print (frequent_ips[0:10])

print ("Sampling data using Min-Wise Sampling")
reservoir_size = math.floor(0.0001 * len(data * 2))
mws = minWiseSampling(int(reservoir_size))
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
