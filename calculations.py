class MakeCalculation:
  def __init__(self,a,b):
    self.first=a
    self.second=b
    
  def ADD(self):
    return (self.first+self.second)
  
ob=MakeCalculation(12,21)
ob.ADD()
