
def keyPressedEvent(keyCode):

  if keyCode == 'C':
    player.moveUp()
    player.moveRight()
    showMessage('X:' + str(player.getX()) + ' Y:' + str(player.getY()))
