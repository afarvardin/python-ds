import csv
import json
import pandas as pd

# df1 = pd.read_csv(r'C:\Users\AminFarvardin\OneDrive - helkinz.com\data\realtime-fraudDataset\ieee\unzip\test\test_identity.csv')
# df1

# Decide the two file paths according to your computer system
csv_test_path = r'C:\Users\AminFarvardin\OneDrive - helkinz.com\data\realtime-fraudDataset\ieee\unzip\test\test_identity.csv'
csv_transaction_path = r'C:\Users\AminFarvardin\OneDrive - helkinz.com\data\realtime-fraudDataset\ieee\unzip\test\test_transaction.csv'
jsonFilePath = r'C:\Users\AminFarvardin\OneDrive - helkinz.com\data\realtime-fraudDataset\ieee\unzip\test\json\test_transaction.json'

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):

	# create a dictionary
	data = {}

	# Open a csv reader called DictReader
	with open(csv_transaction_path, encoding='utf-8') as csv_transaction:
		csvReader_transaction = csv.DictReader(csv_transaction)
		# csvReader_transaction_list = list(csvReader_transaction)
		# l = len(csvReader_transaction_list)
		# count = 0

		# Convert each row into a dictionary
		# and add it to data
		# jsonf = open(jsonFilePath, 'w', encoding='utf-8')
		# jsonf.write('{\n')
		for rows in csvReader_transaction:
			# count += 1
			# print(count)
			# print(rows)
			# # Assuming a column named 'No' to
			# # be the primary key
			key = rows['TransactionID']
			data[key] = rows
			# jsonf.write(json.dumps({key: rows}, indent=4))
			# jsonf.write(json.dumps(str(key)) + json.dumps(str(rows)))
		# 	if l > count:
		# 		jsonf.write(',' + '\n')

		# jsonf.write('\n}')
		# jsonf.close()
        

	# # Open a json writer, and use the json.dumps()
	# # function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))

# Driver Code

# Call the make_json function
make_json()
