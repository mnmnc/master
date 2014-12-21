# -*- coding: utf-8 -*-
from ftools import csv_list as c2l
from ftools import pcap_csv as p2c
from plotter import plotter
from arrtools import arrtools as arr
import random
import matplotlib


def process_protocol(protocol, tshark_path, pcap_file, csv_file, skip_pcap=False):
	"""
	PROCESSING IP TRAFFIC
	:param tshark_path:
	:param pcap_file:
	:param csv_file:
	:return:
	"""
	field_set = []
	field_list = []
	if skip_pcap == False:
		# PREPARING FOR EXECUTION
		if protocol == "ip":
			field_set = p2c.get_ip_field_set()
		elif protocol == "tcp":
			field_set = p2c.get_tcp_field_set()
		elif protocol == "udp":
			field_set = p2c.get_udp_field_set()
		elif protocol == "icmp":
			field_set = p2c.get_icmp_field_set()
		elif protocol == "frame":
			field_set = p2c.get_frame_field_set()
		elif protocol == "dns":
			field_set = p2c.get_dns_field_set()
		else:
			print("[ERR] Unsupported protocol:", protocol)

		tshark_command, field_list = p2c.build_tshark_command(tshark_path, pcap_file,
																csv_file, field_set,
																protocol)

		# INVOKING TSHARK
		p2c.execute_tshark(tshark_command)

	# PARSING CSV
	headers, data = c2l.parse_file(csv_file, field_list)

	return headers, data


def main():
	# INIT
	random.seed()

	# INPUT
	input_directory = "D:\\Poligon\\input\\"
	input_directory = "E:\\SQL_PROJECTS\\Poligon\\input\\"
	input_directory = "/home/x/projects/poligon/input/"

	input_file = "smaller_00000_20120316133000.pcap"
	input_file2 = "smaller_00001_20120316133058.pcap"
	input_file3 = "smaller_00002_20120316134254.pcap"
	input_file4 = "smaller_00003_20120316134407.pcap"
	input_file5 = "1.pcap"

	# OUTPUT
	output_directory = "D:\\Poligon\\output\\"
	output_directory = "E:\\SQL_PROJECTS\\Poligon\\output\\"
	output_directory = "/home/x/projects/poligon/output/"
	output_file = "test1.csv"
	image_output_name = "plotted"
	image_output_format = ".png"

	# OTHER VARIABLES
	tshark_path = "D:\\Apps\\Wireshark\\tshark.exe"
	tshark_path = "C:\\tshark.exe"
	tshark_path = "tshark"


	headers, data = process_protocol("tcp", tshark_path, input_directory + input_file4, output_directory + output_file, False)
	selected_data = arr.select_from_data(data, [headers[0], headers[2]])
	print(selected_data)

	xs = []
	ys = []

	for row in selected_data:
		x = -1
		y = -1
		try:
			x = float(row[0])
			y = float(row[1])
		except:
			pass
		if x is not -1 and y is not -1:
			xs.append(float(row[0]))
			ys.append(float(row[1]))


	# TESTING
	if True == False:
		protocols = ["frame", "ip", "tcp", "udp", "dns", "icmp"]
		for protocol in protocols:
			print("[TST] Testing protocol", protocol)
			headers, data = process_protocol(protocol, tshark_path, input_directory + input_file4, output_directory + output_file, False)
			print(headers)

	print(xs)
	print(ys)

	# BUILDING 2D DATA
	#xs, ys = build_2d(data, "sport", "deport")

	# BUILDING [ number of packets per (source port) x (destination port) ]
	#xs, ys, sizes = build_2d_with_number_of_packets_per_pair(data, "sport", "deport")

	# PLOTTING DATA

	plotter.set_axis_limit(65535,33)
	# PLOTTING DATA WITH MARKER SIZES
	#plotter.set_title("Porty przeznaczenia i liczba pakietów jako wielkość markera")
	plotter.plot(xs, ys, "circle", "r", 0.4)
	#plotter.plot_with_sizes(xs, ys, sizes, "circle", "r", 0.4)

	# with open(output_directory + "l.log", "w") as f:
	# 	for i in range(len(xs)):
	# 		f.write(str(xs[i]) + "-" + str(ys[i]) + " -> " + str(sizes[i]) + "\n")

	with open(output_directory + "log.txt", "w") as f:
		ux = []
		uy = []
		for i in range(len(xs)):
			if xs[i] not in ux:
				ux.append(xs[i])
			if ys[i] not in uy:
				uy.append(ys[i])

		for i in range(len(uy)):
			f.write(str(uy[i]) + "\n")

	# SAVING IMAGE

	#plotter.save_img(output_directory + image_output_name + image_output_format)
	plotter.set_label("x", headers[0])
	plotter.set_label("y", headers[2])
	plotter.set_text(3000, 1, "FIN")
	plotter.set_text(5000, 2, "SYN")
	plotter.set_text(3000, 4, "RST")
	plotter.set_text(3000, 8, "PSH")
	plotter.set_text(3000, 16, "ACK")
	plotter.set_text(3000, 32, "URG")





	plotter.save_img_csize(output_directory + image_output_name + image_output_format, 10, 5, 200)


if __name__ == "__main__":
	main()