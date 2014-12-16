
from csv2list import csv2list as c2l
from pcap2csv import pcap2csv as p2c
from subprocess import call

def main():
	tshark_path = "D:\\Apps\\Wireshark\\tshark.exe"
	input = "D:\\1.pcap"
	output = "D:\\test.csv"
	tshark_command = p2c.build_tshark_command(tshark_path, input, output, p2c.get_tcp_field_set(), 0)
	print(tshark_command)
	test = "D:\\Apps\Wireshark\\tshark.exe -r D:\\1.pcap > D:\\test.csv"
	#p2c.execute_tshark(test, True)
	#headers, data = c2l.parse_file(output, False)

	#print_list_of_lists(data)

	pass

if __name__ == "__main__":
	main()