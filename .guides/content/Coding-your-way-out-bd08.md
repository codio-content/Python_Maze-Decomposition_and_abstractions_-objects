The next challenge will test your ability to solve a complex, but fun coding problem.

## Escape the maze
We have generated a simple maze and you have to get to the exit. However, we've disabled the arrow keys.


## Helper function
We have provided a helper function `checkWall()` that checks whether there is a wall up, down, left or right as you make a move. To check if there is a wall above, you would call `checkWall('U')`. You can also check 'L', 'R' and 'D'.

```python
if checkWall('U') == False:
  player.moveUp()
```

which you can also write in shorthand (the `!` character means 'not') as

```python
if not checkWall('A'):
  player.moveUp()
```

This is asking "if there is **not** a wall above the player, then move up.

{Check It!|assessment}(test-2365830075)


|||guidance
## One possible solution

```python
def keyPressedEvent(keyCode):

  if not checkWall('U'):
    player.moveUp()
  if not checkWall('R'):
    player.moveRight()

```
|||