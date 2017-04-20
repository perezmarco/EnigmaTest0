def make_bricks(small, big, goal):
    big_capacity = goal/5
    if big_capacity == 0 or big == 0:
      small_used = min(goal, small)
      if small_used == goal:
        return True
      else:
        return False
    else:
      big_used = min(big_capacity, big)
      return make_bricks(small, big - big_used, goal - 5*big_used)
