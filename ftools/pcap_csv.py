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
# get_frame_field_set()             # FRAME NUMBER + FRAME LENGTH + FRAME TIME
# get_ip_field_set()                # SOURCE IP + DESTINATION IP + TTL
# get_tcp_field_set()               # SOURCE PORT + DESTINATION PORT + FLAGS
# get_udp_field_set()               # SOURCE PORT + DESTINATION PORT
# get_icmp_field_set()              # TYPE + CODE
# get_dns_field_set()               # NAME + TYPE + RESPONSE + DOMAIN
# get_full_field_set()              # ALL ABOVE
#
# execute_tshark(
#               [str] tshark_command
# )

def build_tshark_command(tshark_path, input_file, output_file, fields, filter_req):
	""" PREPARES COMMAND FOR TSHARK EXECUTION """
	result = ""

	# ADD PATH
	result += tshark_path

	# ADD INPUT
	result += " -r " + input_file

	# ADD OUTPUT MODIFIERS
	result += " -T fields -E header=n -E separator=, -E occurrence=f -E quote=d -t u "

	# ADD FIELDS
	result += fields
	field_list = fields.split("-e")[1:]

	# GETTING RID OF TRAILING SPACES
	for i in range(len(field_list)):
		field_list[i] = (field_list[i]).strip()

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

	return result, field_list

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
	udp = {
		"src": " -e udp.srcport",
	    "dst": " -e udp.dstport"
	}
	dns = {
		"name": " -e dns.qry.name",
		"type": " -e dns.qry.type",
		"resp": " -e dns.a",
	    "domain": " -e dns.ptr.domain_name"
	}
	icmp = {
		"type": " -e icmp.type",
		"code": " -e icmp.code"
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

	if field_cat == "udp":
		# Available: src, dst
		if field_name == "src":
			fields += udp["src"]
		elif field_name == "dst":
			fields += udp["dst"]
		else:
			print("Error. Adding", field_cat, "field unsuccessful. No such field: ", field_name)

	if field_cat == "dns":
		# Available: name, type, resp, domain
		if field_name == "name":
			fields += dns["name"]
		elif field_name == "type":
			fields += dns["type"]
		elif field_name == "resp":
			fields += dns["resp"]
		elif field_name == "domain":
			fields += dns["domain"]
		else:
			print("Error. Adding", field_cat, "field unsuccessful. No such field: ", field_name)

	if field_cat == "icmp":
		# Available: code, type
		if field_name == "code":
			fields += icmp["code"]
		elif field_name == "type":
			fields += icmp["type"]
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

	fields = get_frame_field_set(fields)
	fields = get_ip_field_set(fields)
	fields = get_tcp_field_set(fields)
	fields = get_udp_field_set(fields)
	fields = get_icmp_field_set(fields)
	fields = get_dns_field_set(fields)
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

def get_udp_field_set(fields=""):
	""" CREATES COLLECTION OF FIELDS COMMON FOR udp PROTOCOL """
	fields = add_field(fields, "udp", "src")
	fields = add_field(fields, "udp", "dst")
	return fields

def get_icmp_field_set(fields=""):
	""" CREATES COLLECTION OF FIELDS COMMON FOR udp PROTOCOL """
	fields = add_field(fields, "icmp", "code")
	fields = add_field(fields, "icmp", "type")
	return fields

def get_dns_field_set(fields=""):
	""" CREATES COLLECTION OF FIELDS COMMON FOR udp PROTOCOL """
	fields = add_field(fields, "dns", "name")
	fields = add_field(fields, "dns", "type")
	fields = add_field(fields, "dns", "resp")
	fields = add_field(fields, "dns", "domain")
	return fields

def execute_tshark(tshark_command):
	""" EXECUTES TSHARK """
	call(tshark_command, shell=True)


def main():

	tshark_path = "D:\\Apps\\Wireshark\\tshark.exe"
	input = "D:\\Poligon\\input\\1.pcap"
	output = "D:\\Poligon\\output\\testt.csv"

	# TEST FRAME
	fields = get_frame_field_set()
	tshark_command, field_list = build_tshark_command(tshark_path, input, output, fields, "frame")
	print(tshark_command)


	# TEST IP
	fields = get_ip_field_set()
	tshark_command, field_list = build_tshark_command(tshark_path, input, output, fields, "ip")
	print(tshark_command)

	# TEST TCP
	fields = get_tcp_field_set()
	tshark_command, field_list = build_tshark_command(tshark_path, input, output, fields, "tcp")
	print(tshark_command)

	# TEST UDP
	fields = get_udp_field_set()
	tshark_command, field_list = build_tshark_command(tshark_path, input, output, fields, "udp")
	print(tshark_command)

	# TEST ICMP
	fields = get_icmp_field_set()
	tshark_command, field_list = build_tshark_command(tshark_path, input, output, fields, "icmp")
	print(tshark_command)


	# TEST DNS
	fields = get_dns_field_set()
	tshark_command, field_list = build_tshark_command(tshark_path, input, output, fields, "dns")
	print(tshark_command)

	# TEST FULL
	fields = get_full_field_set()
	tshark_command, field_list = build_tshark_command(tshark_path, input, output, fields, "")
	print(tshark_command)
	print(field_list)

	# EXECUTE COMMAND
	#execute_tshark(tshark_command)

	#out = check_output("type pcap_csv.py", shell=True)
	#print(out.decode(encoding='utf-8'))


if __name__ == "__main__":
	main()