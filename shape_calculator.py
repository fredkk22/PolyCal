import math

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, setWidth):
    self.width = setWidth
    
  def set_height(self, setHeight):
    self.height = setHeight

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    picStr = ""
    
    for i in range(self.height):
      for j in range(self.width):
        picStr += "*"
      picStr += "\n"

    return picStr
  
  def get_amount_inside(self, shape):
    if shape.get_area() > self.get_area():
      return False

    return math.floor(self.get_area()/shape.get_area())
    

class Square(Rectangle):
  def __init__(self, side):
    self.width, self.height = side, side

  def __str__(self):
    return f"Square(side={self.width or self.height})"

  def set_side(self, side):
    self.width, self.height = side, side