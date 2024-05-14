class Shape:
	width = 5
	height = 5
	printChar = '#'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	def print(self):
		for i in range(self.height):
			self.printRow(i)


class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)

class Triangle(Shape):
	height = 5
	width = 2 * height
	def printRow(self,i):
		triangleWidth = i * 2 + 1
		padding = (self.width - triangleWidth)/2
		# print(self.printChar*(i+1))
		print(''*padding +self.printChar -triangleWidth)

t = answer.Triangle()
print(t)