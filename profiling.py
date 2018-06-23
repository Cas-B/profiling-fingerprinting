from datahandler import dataHandler
from tqdm import tqdm

###### Update the occurence of item in the specified dictionary ################################
def updateDictItemOccurence(dictionary, item):
	if item not in dictionary:
		dictionary[item] = 1
	else:
		dictionary[item] += 1

################ Create ngrams for the discretised feature data ###########################
def createNGrams(discretised_feature_data, size):
	ngrams = dict()

	for i in range(len(discretised_feature_data)):
		## Check whether we are not going out of bounds
		if (i + size) >= len(discretised_feature_data):
			continue

		ngram = ""
		for j in range(size):
			ngram += discretised_feature_data[i + j]

		# Store the frequencies of the ngrams
		updateDictItemOccurence(ngrams, ngram)

	return ngrams



### Create test data for the model ######################
def createTestData(data, other_hosts, data_handler):
    test_data = dict()
    for host in other_hosts:
        test_data[host] = data_handler.get_ip_specific_data(host, data)

    return test_data

## Evaluate the trained model using the error based method explained in the paper #######
def evaluateModel(n_grams_training_data, n_grams_test_data):
    if len(n_grams_test_data) <= len(n_grams_training_data):
        return computeError(n_grams_test_data, n_grams_training_data)
    else:
        return computeError(n_grams_training_data, n_grams_test_data)

#### Compute the error based on what is explained in the paper. #####################
def computeError(ngrams_dict_count_smaller, ngrams_dict_count_larger):
    error = 0
    for ngram in ngrams_dict_count_smaller:
        if ngram in ngrams_dict_count_larger:
            error += (abs(ngrams_dict_count_smaller[ngram] - ngrams_dict_count_larger[ngram]))


############## Read the data ###########################################################
infected_hosts = ["147.32.84.191", "147.32.84.192", "147.32.84.193", "147.32.84.204", "147.32.84.205", "147.32.84.206", "147.32.84.207", "147.32.84.208", "147.32.84.209"]
normal_hosts = ["147.32.84.170", "147.32.84.134, 147.32.84.164", "147.32.87.36", "147.32.80.9", "147.32.87.11"]

print("Reading in the data")
data_handler = dataHandler()

print("Processing the data")
data = data_handler.read_processed_data("discretised_data.labeled")
training_data = data_handler.get_ip_specific_data("147.32.84.165", data)
discretised_training_data = [training_data[i][len(training_data[i]) - 1] for i in range(len(training_data))]

print("Creating test data")
test_data = createTestData(data, infected_hosts + normal_hosts, data_handler)
discretised_test_data = dict()

print("Selecting the discretised data")
for host in tqdm(test_data):
    host_data = test_data[host]
    discretised_test_data[host] = [host_data[i][len(host_data[i]) - 1] for i in range(len(host_data))]

print("Creating ngrams for training data")
window_size = 2
ngrams_training_data = createNGrams(discretised_training_data, window_size)

print("Create ngrams (sliding windows) for test data")
ngrams_test_data = dict()

for host in tqdm(discretised_test_data):
    ngrams_test_data[host]=createNGrams(discretised_test_data[host], window_size)

print("Running trained model on test data")

correctly_identified_infected_hosts = []
incorrectly_identified_infected_hosts = []
correctly_identified_normal_hosts = []
incorrectly_identified_normal_hosts = []

for host in tqdm(ngrams_test_data):
    evaluateModel(ngrams_training_data, ngrams_test_data[host])
