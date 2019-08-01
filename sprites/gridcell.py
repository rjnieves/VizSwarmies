import pygame

class GridCell(pygame.sprite.Sprite):
  def __init__(
    self,
    cell_size,
    grid_coord,
    border_size=1,
    matte_size=4,
    border_color=(255, 255, 255),
    matte_color=(0, 0, 255),
    bg_color=(0, 0, 0),
    occupied_bg_color=(100, 100, 0),
    layer=0
  ):
    super(GridCell, self).__init__()
    self.cell_size = cell_size
    self.grid_coord = grid_coord
    self.border_color = border_color
    self.matte_color = matte_color
    self.bg_color = bg_color
    self.occupied_bg_color = occupied_bg_color
    self.matte_size = matte_size
    self.image = pygame.Surface(cell_size)
    self.rect = self.image.get_rect()
    self.image.fill(border_color)
    self.image.fill(matte_color, self.rect.inflate(border_size * -2, border_size * -2))
    self.image.fill(bg_color, self.rect.inflate(matte_size * -2, matte_size * -2))
    self.occupied = False
    self.layer = layer
  
  def update(self):
    bg_rect = pygame.Rect((0, 0), self.cell_size).inflate(
      self.matte_size * -2,
      self.matte_size * -2
    )
    if self.occupied:
      self.image.fill(self.occupied_bg_color, bg_rect)
    else:
      self.image.fill(self.bg_color, bg_rect)
    self.rect = pygame.Rect(
      self.grid_coord[0] * self.cell_size[0],
      self.grid_coord[1] * self.cell_size[1],
      self.cell_size[0],
      self.cell_size[1]
    )

# vim: set ts=2 sw=2 expandtab
