from subprocess import call, check_output

def build_tshark_command(tshark_path, input_file, output_file, fields, header):
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


def get_tcp_field_set():
	""" CREATES COLLECTION OF FIELDS COMMON FOR TCP PROTOCOL """
	fields = ""
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

def execute_tshark(tshark_command, shell=True):
	call(tshark_command, shell)


def main():

	tshark_path = "D:\\Apps\\Wireshark\\tshark.exe"
	input = "D:\\1.pcap"
	output = "D:\\test.csv"

	tshark_command = build_tshark_command(tshark_path, input, output, get_tcp_field_set(), 0)

	print(tshark_command)

	# EXECUTE COMMAND
	execute_tshark(tshark_command, True)

	#out = check_output("type pcap2csv.py", shell=True)
	#print(out.decode(encoding='utf-8'))



	pass
#tshark -T fields -E header=y -E separator=, -E occurrence=a -E quote=d -e ip.proto -e ip.src -e ip.dst

if __name__ == "__main__":
	main()