class favourites:

	def numberOfBlocksAbove(self,array, block):

		# checks how many blocks are in each of columns above the line
		
		elementsAbove = []
		# 1. remove all lines but those above 

		for element in array:
			if (element[1] > block[1]):
				elementsAbove.append(element)

		# 2. loop thrue remaining elements and count 
		LMR = [0, 0, 0]

		for element in elementsAbove:
			if(element[0] == 0):
				LMR[0] += 1

			if(element[0] == 1):
				LMR[1] += 1

			if(element[0] == 1):
				LMR[2] += 1
			
		# 3. return [L, M, R]
		print(' -------------------------- ')
		print('numberOfBlocksAbove: ' + str(LMR))

		return LMR

	def massPointDisplacementFromMid (self, array, block):

		# tells how is mass arranged from middle block or center of row

		LMR = self.numberOfBlocksAbove(self, array, block)

		# Get number of blocks left and right columns.
		# Get different number ob blocks in columns, divided by total number of blocks in side columns.

		displacement = (LMR[2]-LMR[0])/(LMR[0]+LMR[2])
		print(' -------------------------- ')
		print('massPointDisplacementFromMid: ' + str(displacement))
		
		return displacement


	def massPointDisplacementFromBlock (self, array, block):

		 # tells how is mass arranged from  block itself,
		#  !!! implementation is kind of lacking !!! 

		LMR = self.numberOfBlocksAbove(self, array, block)
		# factor is based on different effect of distance from column
		factor = 1

		if( block[0] == 0):
			displacement = (LMR[1]*factor + LMR[2]) / (LMR[0]+ LMR[1]*factor + LMR[2])         

		if( block[0] == 1):
			displacement = self.massPointDisplacementFromMid(self, array, block)
		
		if( block[0] == 2):
			 displacement = -(LMR[1]*factor + LMR[0]) / (LMR[0]+ LMR[1]*factor + LMR[2])

		print(' -------------------------- ')
		print('massPointDisplacementFromBlock: ' + str(displacement))
		

		return displacement

	def block_level (self, array, block):
		# Returns position of block in line and other two blocks in following format:
		# ['L', [1,0,1]]

		# check what is the first number of block
		LMR = '0'

		if block[0] == 0:
			LMR = 'L'
		
		if block[0] == 1:
			LMR = 'M'
		
		if block[0] == 2:
			LMR = 'R'

		line = []

		for x in array:
			if (x[1] == block[1]):
				line.append(x)

		# go one by one and create array

		arrayLine = [0,0,0]

		for x in line:
			if (x[0] == 0):
				arrayLine[0] = 1
			if (x[0] == 1):
				arrayLine[1] = 1
			if (x[0] == 2 ):
				arrayLine[2] = 1
		print(' -------------------------- ')
		print('block_level:  ' + str([LMR, arrayLine]))

		return [LMR, arrayLine]

	def level_bottom (self, block, array):
		return block[1]
	
	def level_top(self, array, block):
		# returns how many blocks from the top is current block

		max_level = 0

		for x in array:
			if(x[1] > max_level):
				max_level = x[1]
		
		print(' -------------------------- ')
		print('Max level:  ' + str(max_level-block[1]))
		
		return (max_level-block[1])
