
from ftools import csv_list as c2l
from ftools import pcap_csv as p2c
from plotter import plotter
import random
import matplotlib


def process_tcp(tshark_path, pcap_file, csv_file, skip_pcap=False):
	"""
	PROCESSING TCP TRAFFIC
	:param tshark_path:
	:param pcap_file:
	:param csv_file:
	:return:
	"""

	if skip_pcap == False:
		# PREPARING FOR EXECUTION
		tshark_command = p2c.build_tshark_command(tshark_path, pcap_file, csv_file, p2c.get_tcp_field_set(), 0)

		# INVOKING TSHARK
		p2c.execute_tshark(tshark_command)

	# PARSING CSV
	headers, data = c2l.parse_file(csv_file, False)

	return headers, data
	# OPTIONAL PRINT
	#c2l.print_list_of_lists(data)


	#create_unique_data(data)

	# INTERESTING PAIRS


def create_unique_data(data):
	unique_data = []
	unique_values = []

	for row in data:
		sport = int(row["sport"])
		dport = int(row["deport"])
		local_id = float(sport + (dport/100000))
		#print("Calculation for", local_id, end="")
		if local_id not in unique_values:
			unique_values.append(local_id)
			unique_data.append([sport, dport, int(row["flags"])])
		else:
			if random.randint(0, 1) == 0:
				not_added = True
				counter = 0
				while not_added:
					local_id = local_id + 0.000005
					counter += 1
					if local_id not in unique_values:
						unique_values.append(local_id)
						unique_data.append([sport, float(dport + (counter*0.5)), int(row["flags"])])
						not_added = False
						#print(" 0 -> Tried", counter, "times. Reached value:", local_id)
			else:
				not_added = True
				counter = 0
				while not_added:
					local_id = local_id + 0.5
					counter += 1
					if local_id not in unique_values:
						unique_values.append(local_id)
						unique_data.append([float(sport + (counter*0.5)), dport, int(row["flags"])])
						not_added = False
						#print(" 1 -> Tried", counter, "times. Reached value:", local_id)

	#print(unique_values)
	xs = []
	ys = []
	for row in unique_data:
		if row[2] == 2 and row[1] < 1025:
			xs.append(row[0])
			ys.append(row[1])

	print(xs)
	print(ys)


def count_packets_per_destination_port():
	pass

def translate_flag(flag):
	# FLAGS VALUES
	# 2048 - RESERVED
	# 1024 - RESERVED
	# 512 - RESERVED
	# 256 - NONCE
	# 128 - CONGESTION WINDOW REDUCED
	# 64 - ECN-ECHO
	# 32 - URG
	# 16 - ACK
	# 8 - PUSH
	# 4 - RST
	# 2 - SYN
	# 1 - FIN
	result = ""
	flag = int(flag)
	if flag >= 2048:
		result += "RSV "
		flag -= 2048
	if flag >= 1024:
		result += "RSV "
		flag -= 1024
	if flag >= 512:
		result += "RSV "
		flag -= 512
	if flag >= 256:
		result += "NCE "
		flag -= 256
	if flag >= 128:
		result += "CWR "
		flag -= 128
	if flag >= 64:
		result += "ECN "
		flag -= 64
	if flag >= 32:
		result += "URG "
		flag -= 32
	if flag >= 16:
		result += "ACK "
		flag -= 16
	if flag >= 8:
		result += "PSH "
		flag -= 8
	if flag >= 4:
		result += "RST "
		flag -= 4
	if flag >= 2:
		result += "SYN "
		flag -= 2
	if flag >= 1:
		result += "FIN "

	return result

def build_2d(data, attribute_1, attribute_2):
	xs = []
	ys = []
	for row in data:
		xs.append(row[attribute_1])
		ys.append(row[attribute_2])

	return xs, ys

def main():
	random.seed()
	input_directory = "D:\\Poligon\\input\\"
	output_directory = "D:\\Poligon\\output\\"
	input_file = "split_00000_20120316133000.pcap"
	output_file = "test1.csv"
	image_output_name = "plotted"
	image_output_format = ".png"
	tshark_path = "D:\\Apps\\Wireshark\\tshark.exe"


	# PROCESSING TCP
	headers, data = process_tcp(tshark_path, input_directory + input_file, output_directory + output_file, False)

	# BUILDING 2D DATA
	xs, ys = build_2d(data, "sport", "deport")

	print(xs)
	# PLOTTING DATA
	#plotter.plot(xs, ys, "circle", "r", 0.4)

	# SAVING IMAGE
	#plotter.save_img(output_directory + image_output_name + image_output_format)

if __name__ == "__main__":
	main()