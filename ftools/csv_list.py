import csv

def make_packet(packet_data):
	"""CREATING PACKET DICTIONARY FROM ROW LIST"""
	return { "id": packet_data[0],
			"time" : packet_data[1],
			"len" : packet_data[2],
			"src" : packet_data[3],
			"dst" : packet_data[4],
			"sport" : packet_data[5],
			"deport" : packet_data[6],
			"ttl" : packet_data[7],
			"flags" : packet_data[8]
	}

def make_packet_new(packet_data, field_names):
	"""CREATING PACKET DICTIONARY FROM ROW LIST"""
	result = {}
	if len(field_names) == 0:
		for i in range(len(packet_data)):
			field_names.append(i)

	for i in range(len(field_names)):
		result.update({(field_names[i]).strip():packet_data[i]})

	return result


def set_header(head):
	"""CREATES A LIST OF HEADERS' NAMES FROM A LIST"""
	result = []
	for i in range(len(head)):
		result.append(head[i])
	return result



def parse_file(local_file, headers=True):
	"""	CREATES A LIST FOR HEADER
		CREATES A LIST FOR DATA
		PARSES CSV FILE AND ADDS DATA TO LISTS
	"""
	data = []
	headers = []
	with open(local_file) as input_file:
		# READ CSV
		csv_file = csv.reader(input_file)

		header_loaded = False
		for row in csv_file:
			if not header_loaded and headers == True:
				# IF THIS IS HEADER
				headers = set_header(row)
				header_loaded = True
			else:
				data.append(make_packet(row))

	return headers, data

def parse_file_new(local_file, field_names):
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
			data.append(make_packet_new(row, field_names))

	return headers, data


def print_list_of_lists(list_of_lists):
	for inner_list in list_of_lists:
		print(inner_list)


def main():
	data = []
	filter = [' frame.number ', ' frame.time_epoch ', ' frame.len ']

	input = "D:\\Poligon\\output\\testt.csv"
	headers, data = parse_file_new(input, filter)

	print(headers)
	print_list_of_lists(data)

if __name__ == "__main__":
	main()