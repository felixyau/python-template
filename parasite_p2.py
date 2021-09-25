import sys
from collections import deque
import json
import copy

cases = [
  {
    "room": 1,
    "grid": [
      [0, 3],
      [0, 1]
    ],
    "interestedIndividuals": [
      "0,0"
    ]
  },
  {
    "room": 2,
    "grid": [
      [0, 3, 2],
      [0, 1, 1],
      [1, 0, 0]
    ],
    "interestedIndividuals": [
      "0,2", "2,0", "1,2"
    ]
  }
]

# Below lists detail all four possible movements from a cell
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]


# Function to check if it is possible to go to position (row, col)
# from the current position. The function returns false if row, col
# is not a valid position or has a value 0 or already visited.
def isValid(mat, visited, row, col):
	return (row >= 0) and (row < len(mat)) and (col >= 0) and (col < len(mat[0])) \
		   and mat[row][col] == 1 and not visited[row][col]


# Find the shortest possible route in a matrix `mat` from source `src` to
# destination `dest`
def findShortestPathLength(mat, src, dest):

	# get source cell (i, j)
	i, j = src

	# get destination cell (x, y)
	x, y = dest

	# base case: invalid input
	if not mat or len(mat) == 0 or mat[i][j] == 0 or mat[x][y] == 0:
		return -1

	# `M × N` matrix
	(M, N) = (len(mat), len(mat[0]))

	# construct a matrix to keep track of visited cells
	visited = [[False for x in range(N)] for y in range(M)]

	# create an empty queue
	q = deque()

	# mark the source cell as visited and enqueue the source node
	visited[i][j] = True

	# (i, j, dist) represents matrix cell coordinates, and their
	# minimum distance from the source
	q.append((i, j, 0))

	# stores length of the longest path from source to destination
	min_dist = sys.maxsize

	# loop till queue is empty
	while q:

		# dequeue front node and process it
		(i, j, dist) = q.popleft()

		# (i, j) represents a current cell, and `dist` stores its
		# minimum distance from the source

		# if the destination is found, update `min_dist` and stop
		if i == x and j == y:
			min_dist = dist
			break

		# check for all four possible movements from the current cell
		# and enqueue each valid movement
		for k in range(4):
			# check if it is possible to go to position
			# (i + row[k], j + col[k]) from current position
			if isValid(mat, visited, i + row[k], j + col[k]):
				# mark next cell as visited and enqueue it
				visited[i + row[k]][j + col[k]] = True
				q.append((i + row[k], j + col[k], dist + 1))

	if min_dist != sys.maxsize:
		return min_dist
	else:
		return -1


if __name__ == '__main__':
	out_format = {"room": 0,
					 "p1": { "":  0, "":  0, "":  0},
					 "p2": 0,
					 "p3": 0,
					 "p4": 0}
	output  = []
	

	
	for data in cases:
		temp_out = out_format

		p1 = dict.fromkeys(data["interestedIndividuals"])
		temp_out["room"] = data["room"]

		temp_out["p1"] = p1
		list_dict = list(temp_out["p1"])
		temp_out["p1"]
		pre_map = data["grid"]
		
		for y in range(len(pre_map)):
			for x in range(len(pre_map[y])):
				if pre_map[y][x] == 3 :
					dest = (y,x)
					pre_map[y][x] =1
					
				if (pre_map[y][x] == 0 or pre_map[y][x] ==2 ):
					pre_map[y][x] = 0
		for n in range(int(len(data["interestedIndividuals"]))):


			mat = pre_map
		
			a, b = data["interestedIndividuals"][n].split(",")
			a = int(a)
			b = int(b)
			
			src = (a,b)

		
			min_dist = findShortestPathLength(mat, src, dest)
		
			if min_dist != -1:
				temp_out["p1"][list_dict[n]] = min_dist
			else:

				temp_out["p1"][list_dict[n]] = -1
		output.append(copy.deepcopy(temp_out))
	print(str(output))
			
	counter = 0
	####//////////the task two
	for data in cases:
		
		longest = -100
		temp_out["p1"]
		pre_map = data["grid"]
		p2_list =  []
		for y in range(len(pre_map)):
			for x in range(len(pre_map[y])):
				if pre_map[y][x] == 1:
					p2_list.append([x,y])
				if pre_map[y][x] == 3 :
					dest = (y,x)
					pre_map[y][x] =1
					
				if (pre_map[y][x] == 0 or pre_map[y][x] ==2 ):
					pre_map[y][x] = 0
		
		for n in range(int(len(p2_list))):
			mat = pre_map
		
			src = (p2_list[n][0],p2_list[n][1])

			min_dist = findShortestPathLength(mat, src, dest)
			

			if min_dist != -1:
				if min_dist > longest:
					longest = min_dist
					output[counter]["p2"] = min_dist
			else:
				output[counter]["p2"] = -1
		if counter == (len(cases)-1):
			counter = 0
		else:
			counter += 1
	
	print(str(output))

			

		
		
		
		
		
		
		
		
		
		
	
			