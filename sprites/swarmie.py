import pygame

class Swarmie(pygame.sprite.Sprite):
  def __init__(self, cell_size, grid_coord, color, layer=3, cube_color=(255, 255, 0)):
    super(Swarmie, self).__init__()
    self.cell_size = cell_size
    self.grid_coord = grid_coord
    self.color = color
    self.image = pygame.Surface(cell_size)
    self.image.fill(color)
    self.rect = self.image.get_rect()
    self.layer = layer
    self.cube_color = cube_color
    self.carrying = False

  def update(self):
    self.image.fill(self.color)
    if self.carrying:
      cube_rect = pygame.Rect((0, 0), self.cell_size).inflate(-16, -16)
      self.image.fill(self.cube_color, cube_rect)
    self.rect = pygame.Rect(
      self.grid_coord[0] * self.cell_size[0],
      self.grid_coord[1] * self.cell_size[1],
      self.cell_size[0],
      self.cell_size[1]
    )

# vim: set ts=2 sw=2 expandtab:
