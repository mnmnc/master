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

	return neighbours


def get_knn(neighbours=None, k=3):
	k_distances = {}
	for key in neighbours:
		k_closest = []
		temp_values = []
		for subkey in neighbours[key]:
			temp_values.append(neighbours[key][subkey])


		temp_values.sort()
		#print(temp_values)

		threshold_value = temp_values[k-1]
		print(key,", threashold: ", threshold_value)

		for subkey in neighbours[key]:
			if neighbours[key][subkey] <= threshold_value:
				k_closest.append(subkey)

		selected_dictionary = {}
		for k_closest_neighbour in k_closest:
			for subkey in neighbours[key]:
				if k_closest_neighbour == subkey:
					selected_dictionary.update({subkey:neighbours[key][subkey]})

		k_distances.update({key:selected_dictionary})

	for key in k_distances:
		print("\n",key,"\t:\n")
		for subkey in k_distances[key]:
			print("\t",subkey,"\t:", k_distances[key][subkey])

	return k_distances

def calculate_local_reachability_density(distances):
	lrd_dictionary = {}

	for key in distances:
		list_size = len(distances[key])
		sum = 0
		for subkey in distances[key]:
			bigger = 0



def main():

	xs = [1,2,3,4,5,6,7,8,9]
	ys = [5,4,6,37,2,5,3,4,8]

	points = create_points_list(xs, ys)
	neighbours = create_distance_dictionary(points)
	get_knn(neighbours)

if __name__ == "__main__":
	main()