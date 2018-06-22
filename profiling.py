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
	total_ngrams_found = 0

	for i in range(len(discretised_feature_data)):
		## Check whether we are not going out of bounds
		if (i + size) >= len(discretised_feature_data):
			continue

		ngram = ""
		for j in range(size):
			ngram += discretised_feature_data[i + j]

		# Store the frequencies of the ngrams
		updateDictItemOccurence(ngrams, ngram)

		total_ngrams_found += 1

	# Compute the probabilities of the ngrams
	for key in ngrams:
		freq = ngrams[key]
		ngrams[key] = float(freq) / float(total_ngrams_found)

	return ngrams


######### Create sliding windows of length n ###########################################
def createSlidingWindows(discretised_feature_data, size):
	windows = []
	for i in range(len(discretised_feature_data)):
		if (i + size) >= len(discretised_feature_data):
			continue

		window = ""
		for j in range(size):
			window += discretised_feature_data[i + j]

		windows.append(window)

	return windows


### Find suspicious behaviour in the test data ###########
def findSuspiciousBehaviour(sliding_windows_test_data,  ngrams_training_data):
    suspicious_behaviour = []
    legitimate_behaviour = []
    for i in tqdm(range(len(sliding_windows_test_data))):
        if sliding_windows_test_data[i] in ngrams_training_data:
            value = ngrams_training_data[sliding_windows_test_data[i]]
            if value >= min(ngrams_training_data.values()):
                suspicious_behaviour.append([i, sliding_windows_test_data[i], value])
        else:
            legitimate_behaviour.append([i, sliding_windows_test_data[i], 0])

    return (legitimate_behaviour, suspicious_behaviour)

##### Calculate the performance of the model #####
def calculatePerformance(legitimate_behaviour, suspicious_behaviour, test_data, window_size):
    tps = 0
    fps = 0
    tns = 0
    fns = 0
    for i in range(len(suspicious_behaviour)):
        for j in range(window_size):
            if i + j >= len(suspicious_behaviour):
                continue
            if test_data[suspicious_behaviour[i + j][0]][10] == "Botnet":
                tps += 1
            else:
                fps += 1

    for i in range(len(legitimate_behaviour)):
        for j in range(window_size):
            if i + j >= len(legitimate_behaviour):
                continue
            if test_data[legitimate_behaviour[i + j][0]][10] == "LEGITIMATE":
                tns += 1
            else:
                fns += 1

    print("The performance of the trained model:")
    print("TP: " + str(tps))
    print("FP: " + str(fps))
    print("TN: " + str(tns))
    print("FN: " + str(fns))

### Create test data for the model ######################
def createTestData(data, other_hosts, data_handler):
    test_data = []
    for host in other_hosts:
        for row in data_handler.get_ip_specific_data(host, data):
            test_data.append(row)

    return test_data


############## Read the data ###########################################################
print("Reading in the data")
data_handler = dataHandler()
print("Processing the data")
data = data_handler.read_processed_data("discretised_data.labeled")
training_data = data_handler.get_ip_specific_data("147.32.84.165", data)
other_hosts = ["147.32.84.191", "147.32.84.192", "147.32.84.193", "147.32.84.204",
                "147.32.84.205", "147.32.84.206", "147.32.84.207", "147.32.84.208",
                "147.32.84.209", "147.32.84.170", "147.32.84.134, 147.32.84.164",
                "147.32.87.36", "147.32.80.9", "147.32.87.11"]

print("Creating test data")
test_data = createTestData(data, other_hosts, data_handler)
discretised_training_data = [training_data[i][len(training_data[i]) - 1] for i in range(len(training_data))]
discretised_test_data = [test_data[i][len(test_data[i]) - 1] for i in range(len(test_data))]

print("Creating ngrams for training data")
window_size = 2
ngrams_training_data = createNGrams(discretised_training_data, window_size)

print("Create sliding windows for test data")

sliding_windows_test_data = createSlidingWindows(discretised_test_data, window_size)

print("Running trained model on test data")
(legitimate_behaviour, suspicious_behaviour) = findSuspiciousBehaviour(sliding_windows_test_data, ngrams_training_data)

print("Calculating the performance of the trained model")
calculatePerformance(legitimate_behaviour, suspicious_behaviour, test_data, window_size)
