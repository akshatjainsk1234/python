class calculator:
  def __init__(self,n):
    self.n=n
  def square(self):
    print(f"the square is : {self.n * self.n}")
  def cubic(self):
    print(f"The cubic is : {self.n * self.n *self.n}" )
  def squareroot(self):
    print(f"The squareroot is : {self.n**1/2}")
    
  
    
a=calculator(4)
a.square()
a.cubic()
a.squareroot()