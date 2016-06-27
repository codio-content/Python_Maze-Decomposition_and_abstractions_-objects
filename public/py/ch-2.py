
def keyPressedEvent(keyCode):
	
  if not checkWall('U'):
    player.moveUp()
  if not checkWall('R'):
    player.moveRight()

