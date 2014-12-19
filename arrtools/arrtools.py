
def select_from_data(data, attributes):
	""" CREATES AN ARRAY FROM DATA DICTIONARY
		BY SELECTING GIVEN ATTRIBUTES
	"""
	results = []
	for row in data:
		results_row = []
		for attribute in attributes:
			results_row.append(row[attribute])
		results.append(results_row)
	return results


def main():
	pass


if __name__ == "__main__":
	main()