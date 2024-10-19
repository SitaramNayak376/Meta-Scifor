class Rectangle:
    def __init__(self,length,breadth):
      self.length = length
      self.breadth = breadth
    def setLength(self,length):
      self.length = length
    def setBreadth(self,breadth):
      self.breadth = breadth
    def getArea(self):
      return self.length * self.breadth

class Square(Rectangle):
  def __init__(self,side):
    super().__init__(side, side)
  def setLength(self,side):
    self.length = side
    self.breadth = side
  def setBreadth(self, side):
    self.length = side
    self.breadth = side

square = Square(4)
print("initial side", square.length)
print("initial area", square.getArea())

square.setLength(5)
print("new side", square.length)
print("new area", square.getArea())

square.setBreadth(6)
print("new side", square.length)
print("new area", square.getArea())