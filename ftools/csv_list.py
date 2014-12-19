import csv

def make_packet(packet_data, field_names):
	"""CREATING PACKET DICTIONARY FROM ROW LIST"""
	result = {}
	if len(field_names) == 0:
		for i in range(len(packet_data)):
			field_names.append(i)

	for i in range(len(field_names)):
		result.update({field_names[i]:packet_data[i]})

	return result


def parse_file(local_file, field_names):
	"""	CREATES A LIST FOR HEADER
		CREATES A LIST FOR DATA
		PARSES CSV FILE AND ADDS DATA TO LISTS
	"""

	data = []
	headers = []
	with open(local_file) as input_file:
		# READ CSV
		csv_file = csv.reader(input_file)
		headers = field_names

		for row in csv_file:
			data.append(make_packet(row, field_names))

	return headers, data


def print_list_of_lists(list_of_lists):
	for inner_list in list_of_lists:
		print(inner_list)


def main():
	data = []
	filter = [' frame.number ', ' frame.time_epoch ', ' frame.len ']

	input = "D:\\Poligon\\output\\testt.csv"
	headers, data = parse_file(input, filter)

	print(headers)
	print_list_of_lists(data)

if __name__ == "__main__":
	main()