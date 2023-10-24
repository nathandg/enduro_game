import math

class Street():
  def __init__(self):
    self.width = 200
    self.height = 200
    self.CX = self.width / 2
    self.L = 50
    
  def math(self, cx, y):
    print("Calculando com cx = {} e y = {}".format(cx, y))
    
    pre = cx + y
    print("pre = cx + y = ", pre)

    pre *= (self.height - y)
    print("pre *= (self.height - y) = ", pre)
        
    pre *= (cx - self.CX)
    print("pre *= (cx - self.CX) = ", pre)
    
    pre *= 0.001
    
    pre += ((self.width  / (2 * self.height)) * y )
    print("pre += ((self.width  / (2 * self.height)) * y) = ", pre)
    
    # pre = ((y * y) * (y - self.height) * (cx - self.CX) * 1 * (self.width / (2 * self.height)))
    # d = cx - pre
    # e = cx + pre
    # return d, e
    return pre


if __name__ == "__main__":
    street = Street()
    screen = []
    
    for i in range(street.height):
      print(street.math(150, i))    
      print("-----------\n")
    
    