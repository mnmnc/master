import math

def create_points_list(xs, ys):
	points = []

	if len(xs) == len(ys):
		for i in range(len(xs)):
			points.append([xs[i], ys[i]])
	else:
		print("[ERR] COORDINATES LIST LENGTH DOES NOT MATCH.")
	return points

def create_distance_dictionary(points):
	distances = {}

	neighbours = {}

	for i in range(len(points)-1):
		point = (points[i][0],points[i][1])
		point_neighbours = {}
		for j in range(len(points)-1):
			compared_point = (points[j][0], points[j][1])
			if i != j:
				if compared_point not in point_neighbours:
					sum = (point[0] - compared_point[0])*(point[0] - compared_point[0]) + (point[1] - compared_point[1]) * (point[1] - compared_point[1])
					result = math.sqrt(sum)
					point_neighbours.update({compared_point:result})
					if compared_point not in neighbours:
						compared_point_neighbours = {}
						compared_point_neighbours.update({point:result})
						neighbours.update({compared_point:compared_point_neighbours})
					else:
						temp_dict = neighbours.get(compared_point)
						temp_dict.update({point:result})
						neighbours.update({compared_point:temp_dict})
		neighbours.update({point:point_neighbours})



	for key in neighbours:
		print("\n",key,"\t:\n")
		for k in neighbours[key]:
			print("\t",k,"\t:", neighbours[key][k])



def main():

	xs = [1,2,3,4,5,6,7,8,9]
	ys = [5,4,6,37,2,5,3,4,8]

	points = create_points_list(xs, ys)
	create_distance_dictionary(points)


if __name__ == "__main__":
	main()