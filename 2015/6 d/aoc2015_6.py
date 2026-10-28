from pathlib import Path

import time

class Lightlayout:
  def __init__(self, part: int):
    self.part = part
    start = time.perf_counter()
    self.layout = [[0 for _ in range(1000)] for _ in range(1000)]
    end = time.perf_counter()
    print(f"Runtime: {end - start:.6f} seconds")  
    self.total = 0

  def coordinate(self, string):
    x, y = string.split(',')
    return int(x), int(y)
  def on(self, light):
    if self.part == 1:
      return 1
    return light + 1
  def off(self, light):
    if self.part == 1 or light == 0:
      return 0
    return light - 1
  def toggle(self, light):
    if self.part == 1:
      return 1 - light
    return light + 2

  def load_data(self, file_name):
    file_path = Path(__file__).parent / file_name
    with open(file_path) as f:
      for line in f:
        parts = line.strip().split()
        self.run_by_line(parts)

  def run_by_line(self, parts):
    if parts[0] == 'turn':
      self.switch(parts[1], self.coordinate(parts[2]), self.coordinate(parts[-1]), self.layout)
    else:
      self.switch(parts[0], self.coordinate(parts[1]), self.coordinate(parts[-1]), self.layout)

  def switch(self, keyword, start, end, grid):
    for i in range(start[0], end[0] + 1):
      for j in range(start[1], end[1] + 1):
        if keyword == 'on':
          grid[j][i] = self.on(grid[j][i])

        elif keyword == 'off':
          grid[j][i] = self.off(grid[j][i])

        elif keyword == 'toggle':
          grid[j][i] = self.toggle(grid[j][i])

    return grid

  def total_lights(self):
    return sum(sum(line) for line in self.layout)

  def calculate(number):
    diagram = [[number for _ in range(1000)] for _ in range(1000)]
    return sum(sum(line) for line in diagram)



# print(Lightlayout.calculate(2))
start = time.perf_counter()

diagram1 = Lightlayout(1)
diagram1.load_data('input_2015_6.txt')
end = time.perf_counter()
print(f"Load: {end - start:.6f} seconds")

print(diagram1.total_lights())

end = time.perf_counter()
print(f"Part 1: {end - start:.6f} seconds")

diagram2 = Lightlayout(2)
diagram2.load_data('input_2015_6.txt')
print(diagram2.total_lights())

end = time.perf_counter()
print(f"Total Runtime: {end - start:.6f} seconds")
