import random

#persistant apple
#logic so snake isn't on top of apple
#add timer instead of waiting for input for game to run
  #way to call raw_input with blocking

snake = [(1,1), (1,2)]

def generate_apple(height, width):
  x = random.choice(range(width))
  y = random.choice(range(height))
  return (x,y)

def display(height, width, snake, apple):
  #create board
  rows = []
  for i in range(height):
    rows.append(["."] * width)
  for x, y in snake:
    rows[y][x] = "x"
  rows[apple[1]][apple[0]] = "a"

  #display board
  for row in rows:
    print "".join(row)

def make_move(user_input):
  moves = {"w": (0,-1),
          "a": (-1, 0),
          "s": (0,1),
          "d": (1, 0)}

  dx, dy = moves[user_input]

  new_snake_x = snake[0][0] + dx
  new_snake_y = snake[0][1] + dy

  if new_snake_y >= 0:
    snake.pop()
    snake.insert(0, (new_snake_x, new_snake_y))
    return True
  else:
    return False

def game_loop():
  display(10, 10, snake, generate_apple(5,5))
  user_input = raw_input("Choose a direction: ")

  while make_move(user_input):
    display(10, 10, snake, generate_apple(5,5))
    user_input = raw_input("Choose a direction: ")



game_loop()
