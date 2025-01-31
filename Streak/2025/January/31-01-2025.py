class Solution:
	def __init__(self):
		self.directions = [(-1,0),(0,1),(1,0),(0,-1)]

	def largestIsland(self, grid: List[List[int]]) -> int:
		self.grid = grid
		self.rows, self.cols = len(self.grid), len(self.grid[0])
		self.visited, self.islands, self.zeros = set(), [], set()
		for i in range(self.rows):
			for j in range(self.cols):
				if (i,j) in self.visited: continue
				cell = self.grid[i][j]
				if cell == 0:
					self.zeros.add((i,j))
					continue
				curr_island = self.map_island(i,j)
				self.islands.append(curr_island)
				self.visited.add((i,j))

		self.islands_hash = {}
		for i, island in enumerate(self.islands):
			island_size = len(island)
			for cell in island:
				self.islands_hash[cell] = [i,island_size]


		if len(self.zeros) <= 0:
			return self.rows*self.cols						
		
		max_joined_island = 0
		for i, j in self.zeros:
			joined_island_size = 0
			pot_islands = set()
			for dir in self.directions:
				new_i,new_j = i+dir[0], j+dir[1]
				if 0 <= new_i < self.rows and 0 <= new_j < self.cols:
					if (new_i,new_j) in self.islands_hash and self.islands_hash[new_i,new_j][0] not in pot_islands:
						pot_islands.add(self.islands_hash[new_i,new_j][0])
						joined_island_size += self.islands_hash[new_i,new_j][1]
			joined_island_size += 1
			max_joined_island = max(max_joined_island,joined_island_size)
		return max_joined_island								

	def map_island(self,i,j):
		stack = []
		stack.append((i,j))
		island = set()
		while stack:
			curr_i,curr_j = stack.pop()
			if (curr_i,curr_j) in self.visited:
				continue
			self.visited.add((curr_i,curr_j))
			island.add((curr_i,curr_j))
			for dir in self.directions:
				new_i,new_j = curr_i+dir[0], curr_j+dir[1]
				if 0 <= new_i < self.rows and 0 <= new_j < self.cols:
					curr_cell = self.grid[new_i][new_j]
					if curr_cell == 1: stack.append((new_i,new_j))
					if curr_cell == 0: self.zeros.add((new_i,new_j))
		return island
