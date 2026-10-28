from pathlib import Path

import time

class LightLayout:
  def __init__(self):
    self.total = 0
    self.layout = {}


  def run(self, file_name):
    file_path = Path(__file__).parent / file_name

    with open(file_path) as f:
      for line in f:
        parts = line.strip().split()
        self.run_by_line(parts)


  def run_by_line(self, parts):
    keyword = parts[0]
    
    if keyword == 'turn':
      state = parts[1]
      start_position = self.parse_coordinate(parts[2])
      end_position = self.parse_coordinate(parts[4])
      
      if state == 'on':
        self.turn_on(start_position, end_position)
      else:
        self.turn_off(start_position, end_position)
    else:
      start_position = self.parse_coordinate(parts[1])
      end_position = self.parse_coordinate(parts[3])

      self.toggle(start_position, end_position)


  def parse_coordinate(self, string):
    x, y = string.split(',')
    return int(x), int(y)
  

  def is_on(self, location):
    return location in self.layout and self.layout[location] == 1
  

  def turn_on_position(self, location):
    if not self.is_on(location):
      self.layout[location] = 1
      self.total += 1
  

  def turn_off_position(self, location):
    if self.is_on(location):
      self.total -= 1
      self.layout[location] = 0


  def toggle_position(self, location):
    if self.is_on(location):
      self.turn_off_position(location)
    else:
      self.turn_on_position(location)


  def turn_on(self, start, end):
    for i in range(start[0], end[0] + 1):
      for j in range(start[1], end[1] + 1):
        location = j, i
        self.turn_on_position(location)
  
  
  def turn_off(self, start, end):
    for i in range(start[0], end[0] + 1):
      for j in range(start[1], end[1] + 1):
        location = j, i
        self.turn_off_position(location)


  def toggle(self, start, end):
    for i in range(start[0], end[0] + 1):
      for j in range(start[1], end[1] + 1):
        location = j, i
        self.toggle_position(location)


  def print(self):
    print(self.total)


class LightLayout2(LightLayout):
  def turn_on_position(self, location):
    pass
  def turn_off_position(self, location):
    pass





# --- Main ---
start = time.perf_counter()

mine = LightLayout()
mine.run('input_2015_6.txt')
mine.print()

end = time.perf_counter()
print(f"Part 1: {end - start:.6f} seconds")