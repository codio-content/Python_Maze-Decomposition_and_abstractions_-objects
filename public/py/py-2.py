
class Object(object):
    pass

gameDetails = Object()

def turnTaken():

  gameDetails.x = player.getX()
  gameDetails.y = player.getY()
  gameDetails.score = getScore()
  gameDetails.energy = getEnergy()

  showMessage('X:' + str(gameDetails.x) + ' Y:' + str(gameDetails.y))
  