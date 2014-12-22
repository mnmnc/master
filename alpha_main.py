# -*- coding: utf-8 -*-
from ftools import csv_list as c2l
from ftools import pcap_csv as p2c
from plotter import plotter
from arrtools import arrtools as arr
import random
import os



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


def testing():
	# TESTING
	# INPUT
	input_directory = "/home/x/projects/poligon/input/"
	input_file = "smaller_00000_20120316133000.pcap"

	# OUTPUT
	output_directory = "/home/x/projects/poligon/output/"
	output_file = "test1.csv"
	image_output_name = "plotted"
	image_output_format = ".png"

	# OTHER VARIABLES
	tshark_path = "tshark"
	if True == False:
		protocols = ["frame", "ip", "tcp", "udp", "dns", "icmp"]
		for protocol in protocols:
			print("[TST] Testing protocol", protocol)
			headers, data = process_protocol(protocol, tshark_path, input_directory + input_file4, output_directory + output_file, False)
			print(headers)


def work_main():

	# INPUT
	input_directory = "D:\\Poligon\\input\\"
	input_file = "smaller_00000_20120316133000.pcap"

	# OUTPUT
	output_directory = "D:\\Poligon\\output\\"
	output_file = "test.csv"
	image_output_name = "plotted"
	image_output_format = ".png"

	# OTHER VARIABLES
	tshark_path = "D:\\Apps\\Wireshark\\tshark.exe"

	# EXECUTION
	headers, data = process_protocol("tcp", tshark_path, input_directory + input_file, output_directory + output_file, False)

	# BUILDING [ number of packets per (source port) x (destination port) ]
	#xs, ys, sizes = build_2d_with_number_of_packets_per_pair(data, "sport", "deport")

	# plotter.set_title("Porty przeznaczenia i liczba pakietów jako wielkość markera")
	# plotter.plot(xs, ys, "circle", "r", 0.4)
	# plotter.plot_with_sizes(xs, ys, sizes, "circle", "r", 0.4)
	# plotter.save_img_csize(output_directory + image_output_name + image_output_format, 10, 5, 200)


def linux_main():

	# INPUT
	input_directory = "/home/x/projects/poligon/input/"
	input_file = "smaller_00000_20120316133000.pcap"

	# OUTPUT
	output_directory = "/home/x/projects/poligon/output/"
	output_file = "test1.csv"
	image_output_name = "plotted"
	image_output_format = ".png"

	# OTHER VARIABLES
	tshark_path = "tshark"

	# EXECUTION
	headers, data = process_protocol("tcp", tshark_path, input_directory + input_file, output_directory + output_file, False)

	# BUILDING [ number of packets per (source port) x (destination port) ]
	#xs, ys, sizes = build_2d_with_number_of_packets_per_pair(data, "sport", "deport")

	# plotter.set_title("Porty przeznaczenia i liczba pakietów jako wielkość markera")
	# plotter.plot(xs, ys, "circle", "r", 0.4)
	# plotter.plot_with_sizes(xs, ys, sizes, "circle", "r", 0.4)
	# plotter.save_img_csize(output_directory + image_output_name + image_output_format, 10, 5, 200)

def main():
	# INIT
	random.seed()

	# OS CONDITIONAL EXECUTION / PART OF THE DEVELOPMENT PROCESS.
	# WILL BE REMOVED FOR FINAL VERSION
	if os.name == "nt":
		work_main()
	elif os.name == "posix":
		linux_main()
	else:
		print("[ERR] OS not supported. \n\tI give up...")
		return


if __name__ == "__main__":
	main()