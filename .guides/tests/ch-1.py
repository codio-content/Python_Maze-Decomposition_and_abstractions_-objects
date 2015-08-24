
x = 1
y = 4

class Player:
  
  def setX(self, val):
    global x 
    x = val

  def setY(self, val):
    global y 
    y = val
  
player = Player()


try:
  execfile('/home/codio/workspace/public/py/ch-1.py')
  
  keyPressedEvent('C')
    
  if x <= 3 and y >= 2:
    raise ValueError("error")
  
  print 'well done'
  exit(0)
  
except (IOError, SyntaxError, ValueError) as e:
  pass
  
print 'Not quite right, try again!'
exit(1)
