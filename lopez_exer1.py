
from anytree import Node, RenderTree

# init_state_string=input("Enter initial state\n(binary string with length 25):")
#Build Tree Pseudocode
# Initialization:
# 1. Let root = initial state
# 2. Let root.children = state after pressing one button, total of N children

# Loop:
# N = N-1
# For each child:
# 	1. Let root = child
# 	2. Let root.children = state after pressing one button, total of N children
	# if child.state = [0]: solutionFound, return path
	# if N = 0: break inner loop

#Initialize parameters
length = 3
area = length*length
grid=[1 for i in range(area)]
valid_moves = [[0 for i in range(area)] for j in range(area)]
grid_states = {'0': grid}

def getStringPath(root, i):
	return f"{root.name}-{i}"

def addGrids(current_grid, move):
	result = [0 for i in range(area)]
	for i in range (area):
		result[i] = current_grid[i] ^ move[i]
	return result

def generateMovesTree(grid, valid_moves):
	root = Node('0')
	grid_states['0'] = grid 
	for i in range (len(valid_moves)):
		path = getStringPath(root, i+1)
		child = Node(path, parent = root)
		grid_states[path] = addGrids(grid, valid_moves[i])
	return root

def printMovesTree(root):
	for pre, fill, node in RenderTree(root):
		print("%s%s" % (pre, node.name))	

def print2DGrid(grid):
	for i in range(len(grid)):
		print(f"{grid[i]} ", end = "")
		if i % length == length-1:
			print()


def initValidMoves(moves):
	moves_index=0
	for i in range(length):
		for j in range(length):
			adjacents = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
			valid_adjacents=[]
			for candidate in adjacents:
				if candidate[0] < 0 or candidate[0] >= length or candidate[1] < 0 or candidate[1] >= length: continue
				else: valid_adjacents.append(candidate)

			for k in range (len(valid_adjacents)):
				num = valid_adjacents[k][0] * length + valid_adjacents[k][1]
				# print(num)
				moves[moves_index][num] = 1
			moves[moves_index][moves_index]=1
			moves_index+=1

	# temp=[]
	# grid_state=[]
	# row=[]
	# for i in range(len(moves)):
	# 	for j in range(len(moves[i])):
	# 			if (j % length == length-1):
	# 				row.append(moves[i][j])
	# 				grid_state.append(row)
	# 				row = []
	# 			else: row.append(moves[i][j])
	# 	temp.append(grid_state)
	# 	grid_state=[]

	# moves = temp

initValidMoves(valid_moves)

# for i in valid_moves:
# 	print(i)
root = generateMovesTree(grid, valid_moves)
printMovesTree(root)
print(grid_states)

