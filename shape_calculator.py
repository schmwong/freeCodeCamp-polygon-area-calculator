class Rectangle:
	
	def __init__(self, width, height):
		self.width = width
		self.height = height

	
	def set_width(self, width):
		self.width = width

	
	def set_height(self, height):
		self.height = height

	
	def get_area(self):
		return (self.width * self.height)

	
	def get_perimeter(self):
		return (2 * self.width + 2 * self.height)

	
	def get_diagonal(self):
		return((self.width ** 2 + self.height ** 2) ** .5)


	def get_picture(self):
		if self.width > 50 or self.height > 50:
			return "Too big for picture."
		else:
			line = "*" * self.width + "\n"
			picture = line * self.height
			return picture


	def get_amount_inside(self, shape):
		return (self.get_area() // shape.get_area())

	
	def __str__(self):
		return f"Rectangle(width={self.width}, height={self.height})"



class Square(Rectangle):
	
	def __init__(self, side):
		# Inheriting the __init__ method of the Rectangle class
		# Passing "length" attribute for both width and height
		super(Square, self).__init__(side, side)
		self.side = side
		self.height = side
		self.width = side


	def set_side(self, side):
		self.side = side
		self.height = side
		self.width = side

	
	def set_width(self, width):
		self.side = width
		self.height = width
		self.width = width


	def set_height(self, height):
		self.side = height
		self.height = height
		self.width = height


	def get_area(self):
		return super().get_area()


	def get_perimeter(self):
		return super().get_perimeter()


	def get_diagonal(self):
		return super().get_diagonal()
		
	
	def __str__(self):
		return f"Square(side={self.side})"