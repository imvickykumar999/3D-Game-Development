
# python -m pip install anvil-parser

import anvil, math

def tower():
	from CallMe import MAZE3D_generator as mzg
	from CallMe import MAZE3D_solver as mzs

	region = anvil.EmptyRegion(0, 0)
	bottom = 0
	tall = 256

	chunk = 1
	side = 16*chunk -1

	gold_block = anvil.Block('minecraft', 'gold_block')
	glowstone = anvil.Block('minecraft', 'glowstone')

	diamond_block = anvil.Block('minecraft', 'diamond_block')
	blue_stained_glass = anvil.Block('minecraft', 'blue_stained_glass')

	for y in range(bottom, tall, 10): # floor
		us_maze = mzg.returnMaze(side,side)
		s_maze = mzs.solve_maze(us_maze)

		for x in range(side):
			for z in range(side):

				if s_maze[x][z] == 'w':
					region.set_block(diamond_block, x, y+1, z)
					region.set_block(diamond_block, x, y+2, z)

				if y == bottom or not (x == 1 and z == 1):
					region.set_block(gold_block, x, y, z)

				if s_maze[x][z] == 'p':
					region.set_block(glowstone, x, y, z)

	for x in range(side): # walls
		for y in range(bottom, tall-1):
			for z in range(side):
				if (x == 0 or x == side - 1 or z == 0 or z == side - 1):
					region.set_block(blue_stained_glass, x, y, z)

	region.save('region/r.0.0.mca')
	print('\nBuild Complete.')


def cylinder():
	region = anvil.EmptyRegion(0, 0)
	chunk = 1

	tall = 120
	radius = 16*chunk -1

	def printPattern(radius=4, y=0):
		xyz = []

		for x in range((2 * radius)+1):
			for z in range((2 * radius)+1):
				
				dist = math.sqrt((x - radius) * (x - radius) +
					(z - radius) * (z - radius))

				if (dist > radius - 0.5 and dist < radius + 0.5):
					# print("*",end=" ")
					xyz.append((x-radius, y ,z-radius))
				else:
					# print(" ",end=" ")	
					pass
		
			# print()
		return xyz

	# wall = anvil.Block('minecraft', 'gold_block')
	wall = anvil.Block('minecraft', 'glowstone')

	floor = anvil.Block('minecraft', 'diamond_block')
	# floor = anvil.Block('minecraft', 'blue_stained_glass')

	for x in range(2*radius): # floor
		for y in range(-63, tall, 5):
			for z in range(2*radius):
				if y == -63 or not (x == 1 and z == 1):
					region.set_block(floor, x, y, z)
					
	for i in range(-63, tall-1): # wall
		for x,y,z in printPattern(radius, i):
			region.set_block(wall, x+radius, y, z+radius)

	region.save('region/r.0.0.mca')
print('\nBuild Complete.')


# tower()
cylinder()
