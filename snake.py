def display(height, width, snake):
  #create board
  rows = []
  for i in range(height):
    rows.append(["."] * width)
  for x, y in snake:
    rows[y][x] = "x"

  #display board
  for row in rows:
    print "".join(row)

display(5,5,[(1,1), (1,2)])
