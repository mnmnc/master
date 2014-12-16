
import csv_to_list as c2l
import pcap_to_csv as p2c

def main():
	tshark_path = "D:\\Apps\\Wireshark\\tshark.exe"
	input = "D:\\1.pcap"
	output = "D:\\test.csv"
	tshark_command = p2c.build_tshark_command(tshark_path, input, output, p2c.get_tcp_field_set(), 0)

	headers, data = c2l.parse_file(output, False)

	#print_list_of_lists(data)

	pass

if __name__ == "__main__":
	main()