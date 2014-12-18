import matplotlib.pyplot as plt


def save_img(destination_filename):
	plt.savefig(destination_filename)


def plot(xlist, ylist, marker_style='circle', def_color="r", def_alpha=0.5):
	if marker_style == "circle":
		plt.plot(xlist, ylist, def_color+'o', alpha=def_alpha)
	elif marker_style == "pixel":
		plt.plot(xlist, ylist, def_color+',', alpha=def_alpha)
	elif marker_style == "point":
		plt.plot(xlist, ylist, def_color+'.', alpha=def_alpha)
	elif marker_style == "x":
		plt.plot(xlist, ylist, def_color+'x', alpha=def_alpha)
	elif marker_style == "line":
		plt.plot(xlist, ylist, def_color+'-', alpha=def_alpha)
	elif marker_style == "triangle":
		plt.plot(xlist, ylist, def_color+'^', alpha=def_alpha)
	else:
		plt.plot(xlist, ylist, def_color+'o', alpha=def_alpha)


def set_label(axis_name, label):
	if axis_name == "x":
		plt.xlabel(label)
	elif axis_name == "y":
		plt.ylabel(label)
	else:
		print("[ERR] Unknown label", label)


def set_title(title):
	plt.title(title)


def set_text(x, y, text):
	plt.text(x, y, text)


def set_axis_limit(limit_x, limit_y):
	plt.axis([0, limit_x, 0, limit_y])


def set_note(x,y, text_x, text_y, text):
	"""
	x,y - pointed end
	text_x, text_y - location of the text
	"""
	plt.annotate(text, xy=(x, y),
	             xytext=(text_x, text_y),
	             arrowprops=dict(facecolor='black',
	                             shrink=0.08,
	                             width=1.0,
	                             headwidth=5.0,
	                             alpha=0.3),)


def clear_plot():
	plt.clf()


def main():
	out_image = "D:\\out.png"
	#plt.plot([1,2,3,4], [1,4,9,16], 'ro')
	set_axis_limit(10,10)
	plot([1,4,9,16], [1,2,3,4], "line", "b", 0.4)

	#plot([8,4,9,16], [11,14,3,4], 'y^', ms=8.0, alpha=0.4)



	plt.show()
	pass

if __name__ == "__main__":
	main()