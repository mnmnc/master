from subprocess import call, check_output

# FUNCTIONS AVAILABLE
#
# build_tshark_command(             # RETURNS COMMAND STRING
#               [str] tshark_path,
#               [str] input_file,
#               [str] output_file,
#               [str] fields,
#               [str] filter_req    # REQUIRED FILTER
#               [int] header        # WHETHER TO INCLUDE HEADER OR NOT
# )
#
# add_field(
#               [str] fields,
#               [str] field_cat,
#               [str] field_name
# )
#
# get_tcp_field_set()               # SOURCE PORT + DESTINATION PORT + FLAGS
# get_ip_field_set()                # SOURCE IP + DESTINATION IP + TTL
# get_frame_field_set()             # FRAME NUMBER + FRAME LENGTH + FRAME TIME
# get_full_field_set()
# execute_tshark(
#               [str] tshark_command
# )

def build_tshark_command(tshark_path, input_file, output_file, fields, filter_req, header):
	""" PREPARES COMMAND FOR TSHARK EXECUTION """
	result = ""

	# ADD PATH
	result += tshark_path

	# ADD INPUT
	result += " -r " + input_file

	# ADD OUTPUT MODIFIERS
	if header == 1:
		result += " -T fields -E header=y -E separator=, -E occurrence=a -E quote=n -t u "
	else:
		result += " -T fields -E header=n -E separator=, -E occurrence=a -E quote=n -t u "

	# ADD FIELDS
	result += fields

	# ADD FILTER
	filter = ""
	if filter_req == "tcp":
		filter += ' -R "(ip.proto == 6)" -2 '
	elif filter_req == "ip":
		filter += ' -R "(ip.version == 4)" -2 '
	elif filter_req == "icmp":
		filter += ' -R "(ip.proto == 1)" -2 '
	elif filter_req == "udp":
		filter += ' -R "(ip.proto == 17)" -2 '
	elif filter_req == "dns":
		filter += ' -R "(dns)" -2 '
	result += filter

	# ADD OUTPUT
	result += " > " + output_file

	return result


def add_field(fields, field_cat, field_name):
	""" ADDS FIELD BASED ON CATEGORY AND NAME"""
	ip = {
		"src": " -e ip.src",
	    "dst": " -e ip.dst",
	    "ttl": " -e ip.ttl"
	}
	tcp = {
		"src": " -e tcp.srcport",
	    "dst": " -e tcp.dstport",
	    "flags": " -e tcp.flags"
	}
	frame = {
		"time": " -e frame.time_epoch",
		"len": " -e frame.len",
	    "num": "-e frame.number"
	}

	if field_cat == "ip":
		# Available: src, dst, ttl
		if field_name == "src":
			fields += ip["src"]
		elif field_name == "dst":
			fields += ip["dst"]
		elif field_name == "ttl":
			fields += ip["ttl"]
		else:
			print("Error. Adding", field_cat, "field unsuccessful. No such field: ", field_name)

	if field_cat == "tcp":
		# Available: src, dst, flags
		if field_name == "src":
			fields += tcp["src"]
		elif field_name == "dst":
			fields += tcp["dst"]
		elif field_name == "flags":
			fields += tcp["flags"]
		else:
			print("Error. Adding", field_cat, "field unsuccessful. No such field: ", field_name)

	if field_cat == "frame":
		# Available: time, len
		if field_name == "time":
			fields += frame["time"]
		elif field_name == "len":
			fields += frame["len"]
		elif field_name == "num":
			fields += frame["num"]
		else:
			print("Error. Adding", field_cat, "field unsuccessful. No such field: ", field_name)

	return fields


def get_tcp_field_set(fields=""):
	""" CREATES COLLECTION OF FIELDS COMMON FOR TCP PROTOCOL """
	fields = add_field(fields, "tcp", "src")
	fields = add_field(fields, "tcp", "dst")
	fields = add_field(fields, "tcp", "flags")
	return fields

def get_full_field_set(fields=""):
	""" CREATES COLLECTION OF FIELDS COMMON FOR TCP PROTOCOL """
	fields = add_field(fields, "frame", "num")
	fields = add_field(fields, "frame", "time")
	fields = add_field(fields, "frame", "len")
	fields = add_field(fields, "ip", "src")
	fields = add_field(fields, "ip", "dst")
	fields = add_field(fields, "tcp", "src")
	fields = add_field(fields, "tcp", "dst")
	fields = add_field(fields, "ip", "ttl")
	fields = add_field(fields, "tcp", "flags")

	# LIMIT TO TCP ONLY
	fields += ' -R "(ip.proto == 6)" -2 '
	return fields

def get_ip_field_set(fields=""):
	""" CREATES COLLECTION OF FIELDS COMMON FOR TCP PROTOCOL """
	fields = add_field(fields, "ip", "src")
	fields = add_field(fields, "ip", "dst")
	fields = add_field(fields, "ip", "ttl")
	return fields

def get_frame_field_set(fields=""):
	""" CREATES COLLECTION OF FIELDS COMMON FOR TCP PROTOCOL """
	fields = add_field(fields, "frame", "num")
	fields = add_field(fields, "frame", "time")
	fields = add_field(fields, "frame", "len")
	return fields

def execute_tshark(tshark_command):
	""" EXECUTES TSHARK """
	call(tshark_command, shell=True)


def main():

	tshark_path = "D:\\Apps\\Wireshark\\tshark.exe"
	input = "D:\\Poligon\\input\\1.pcap"
	output = "D:\\Poligon\\output\\testt.csv"

	fields = get_frame_field_set()
	fields = get_ip_field_set(fields)

	tshark_command = build_tshark_command(tshark_path, input, output, fields, "ip", 0)

	print(tshark_command)

	# EXECUTE COMMAND
	execute_tshark(tshark_command)

	#out = check_output("type pcap_csv.py", shell=True)
	#print(out.decode(encoding='utf-8'))



	pass
#tshark -T fields -E header=y -E separator=, -E occurrence=a -E quote=d -e ip.proto -e ip.src -e ip.dst

if __name__ == "__main__":
	main()