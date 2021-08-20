class MakeCalculation:
  def __init__(self,a,b):
    self.first=a
    self.second=b
    
  def ADD(self):
    return (self.first+self.second)
  
  def __del__(self):
    pass
  
ob=MakeCalculation(12,21)
ob.ADD()
