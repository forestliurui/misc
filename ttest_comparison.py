"""
This is to perform t-test
"""
import numpy as np
import csv
from scipy import stats

def readData(filename):
	with open(filename) as csvfile:
		csvreader = csv.reader(csvfile)
		#method_name = csv_file_name.split('.')[0]
		#method_name = method_name.split('/')[1]
		row_count = 0
		for row in csvreader:
			if row_count == 0:
				dict_method = {}
				dict_method2rowID = {}
				
				dict_method2rowID[row[1]] = 1
				dict_method2rowID[row[2]] = 2
				dict_method2rowID[row[3]] = 3
				dict_method2rowID[row[4]] = 4
				
				dict_method[row[1]] = []
				dict_method[row[2]] = []
				dict_method[row[3]] = []
				dict_method[row[4]] = []

				row_count += 1
			else:
				if '.' not in row[0]:
					for (method_name, colID) in dict_method2rowID.items():
						dict_method[method_name].append(float(row[colID]))
	return dict_method

def pairedTTest(method1, method2,dict_method):
	temp1 = np.array(dict_method[method1])
	temp2 = np.array(dict_method[method2])
	print temp1-temp2
	print np.average(temp1-temp2)
	return stats.ttest_1samp(temp1-temp2,0)
	

if __name__ == "__main__":
	file_name = 'comparison_with_SVM_bag_AUC.csv'

	dict_method = readData(file_name)
	for method_name in dict_method.keys():
		print method_name		
		print pairedTTest('adaboost(500 rounds)',method_name, dict_method)
	import pdb;pdb.set_trace()
