
def flags_to_flag_list(flags):
	""" CONVERTS DECIMAL FLAG VALUE TO FLAGS DICTIONARY """
	# FLAGS VALUES
	# 2048  - RESERVED
	# 1024  - RESERVED
	# 512   - RESERVED
	# 256   - NONCE
	# 128   - CONGESTION WINDOW REDUCED
	# 64    - ECN-ECHO
	# 32    - URG
	# 16    - ACK
	# 8     - PUSH
	# 4     - RST
	# 2     - SYN
	# 1     - FIN

	if flags > 2**12-1:
		print("[ERR] Flags cannot be bigger than", str(2**12-1))
		print("[ERR] \tOnly 12 bit flags are currently supported.")
		return None

	flag_dict = {
		"fin":0,
	    "syn":0,
	    "rst":0,
	    "psh":0,
	    "ack":0,
	    "urg":0,
	    "ecn":0,
	    "cwr":0,
	    "nce":0,
	    "rsvd1":0,
	    "rsvd2":0,
	    "rsvd3":0,
	}
	if int(flags)&1 == 1:
		flag_dict["fin"] += 1
	if int(flags)&2 == 2:
		flag_dict["syn"] += 1
	if int(flags)&4 == 4:
		flag_dict["rst"] += 1
	if int(flags)&8 == 8:
		flag_dict["psh"] += 1
	if int(flags)&16 == 16:
		flag_dict["ack"] += 1
	if int(flags)&32 == 32:
		flag_dict["urg"] += 1
	if int(flags)&64 == 64:
		flag_dict["ecn"] += 1
	if int(flags)&128 == 128:
		flag_dict["cwr"] += 1
	if int(flags)&256 == 256:
		flag_dict["nce"] += 1
	if int(flags)&512 == 512:
		flag_dict["rsvd1"] += 1
	if int(flags)&1024 == 1024:
		flag_dict["rsvd2"] += 1
	if int(flags)&2048 == 2048:
		flag_dict["rsvd3"] += 1

	return flag_dict


def main():

	print(flags_to_flag_list(2242))
	pass

if __name__ == "__main__":

	main()
