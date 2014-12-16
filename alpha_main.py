
from ftools import csv_list as c2l
from ftools import pcap_csv as p2c


def process_tcp(tshark_path):
	"""
	PROCESSING TCP TRAFFIC
	:param tshark_path:
	:return:
	"""

	input = "D:\\1.pcap"
	output = "D:\\test.csv"

	# PREPARING FOR EXECUTION
	tshark_command = p2c.build_tshark_command(tshark_path, input, output, p2c.get_tcp_field_set(), 0)

	# INVOKING TSHARK
	p2c.execute_tshark(tshark_command)

	# PARSING CSV
	headers, data = c2l.parse_file(output, False)

	# OPTIONAL PRINT
	c2l.print_list_of_lists(data)


def main():
	tshark_path = "D:\\Apps\\Wireshark\\tshark.exe"

	# PROCESSING TCP
	process_tcp(tshark_path)



if __name__ == "__main__":
	main()