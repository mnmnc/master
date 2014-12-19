# -*- coding: utf-8 -*-
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
	field_list = []
	if skip_pcap == False:
		# PREPARING FOR EXECUTION
		tshark_command, field_list = p2c.build_tshark_command(tshark_path, pcap_file, csv_file, p2c.get_tcp_field_set(), "tcp", 0)

		# INVOKING TSHARK
		p2c.execute_tshark(tshark_command)

	# PARSING CSV
	headers, data = c2l.parse_file_new(csv_file, field_list)

	return headers, data


def main():
	# INIT
	random.seed()

	# INPUT
	input_directory = "D:\\Poligon\\input\\"
	input_file = "smaller_00000_20120316133000.pcap"
	input_file2 = "smaller_00001_20120316133058.pcap"
	input_file3 = "smaller_00002_20120316134254.pcap"
	input_file4 = "smaller_00003_20120316134304.pcap"

	# OUTPUT
	output_directory = "D:\\Poligon\\output\\"
	output_file = "test1.csv"
	image_output_name = "plotted"
	image_output_format = ".png"

	# OTHER VARIABLES
	tshark_path = "D:\\Apps\\Wireshark\\tshark.exe"

	# PROCESSING TCP
	headers, data = process_tcp(tshark_path, input_directory + input_file4, output_directory + output_file, False)

	print(headers)


	# BUILDING 2D DATA
	#xs, ys = build_2d(data, "sport", "deport")

	# BUILDING [ number of packets per (source port) x (destination port) ]
	#xs, ys, sizes = build_2d_with_number_of_packets_per_pair(data, "sport", "deport")

	# PLOTTING DATA

	#plotter.set_axis_limit(1000,1000)
	# PLOTTING DATA WITH MARKER SIZES
	#plotter.set_title("Porty przeznaczenia i liczba pakietów jako wielkość markera")
	#plotter.plot(xs, ys, "circle", "r", 0.4)
	#plotter.plot_with_sizes(xs, ys, sizes, "circle", "r", 0.4)

	# with open(output_directory + "l.log", "w") as f:
	# 	for i in range(len(xs)):
	# 		f.write(str(xs[i]) + "-" + str(ys[i]) + " -> " + str(sizes[i]) + "\n")



	# SAVING IMAGE
	#plotter.save_img(output_directory + image_output_name + image_output_format)

if __name__ == "__main__":
	main()