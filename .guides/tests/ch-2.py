
up = False
right = False

class Player:
  
  def moveUp(self):
    global up 
    up = True

  def moveDown(self):
    pass

  def moveLeft(self):
    pass
  
  def moveRight(self):
    global right 
    right = True
  
def checkWall(val):
  return False
    
player = Player()

try:
  execfile('/home/codio/workspace/public/py/ch-2.py')
  
  keyPressedEvent('C')
  keyPressedEvent('C')
  keyPressedEvent('C')
  keyPressedEvent('C')
    
  if not (up and right):
    raise ValueError("error")
  
  print 'well done'
  exit(0)
  
except (IOError, SyntaxError, ValueError) as e:
  pass
  
print 'Not quite right, try again!'
exit(1)
