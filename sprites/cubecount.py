import pygame

class CubeCount(pygame.sprite.Sprite):
  def __init__(self, cell_size, grid_coord, text_font, text_color, layer=1):
    super(CubeCount, self).__init__()
    self.cell_size = cell_size
    self.grid_coord = grid_coord
    self.count_value = 0
    self.text_font = text_font
    self.text_color = text_color
    self.image = None
    self.rect = None
    self.layer = layer

  def update(self):
    self.rect = pygame.Rect(
      self.grid_coord[0] * self.cell_size[0],
      self.grid_coord[1] * self.cell_size[1],
      self.cell_size[0],
      self.cell_size[1]
    )
    self.image = self.text_font.render(
      '{}'.format(self.count_value),
      True,
      self.text_color
    )
    text_rect = self.image.get_rect()
    self.rect.move_ip(
      (self.rect.width - text_rect.width) / 2,
      (self.rect.height - text_rect.height) / 2
    )

# vim: set ts=2 sw=2 expandtab
