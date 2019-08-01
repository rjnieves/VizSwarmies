import pygame

class ScoreBoard(pygame.sprite.Sprite):
  def __init__(self, cube_state, time_keep, board_pix_size, board_font, font_color=(255,255,255)):
    super(ScoreBoard, self).__init__()
    self.cube_state = cube_state    # must be a reference to a mutating object!
    self.time_keep = time_keep      # must be a reference to a mutating object!
    self.board_font = board_font
    self.font_color = font_color
    self.image = pygame.Surface(board_pix_size)
    self.rect = self.image.get_rect()
    self.layer = 1

  def update(self):
    sb_string = 'Episode: {:d}, Step: {:d} of 900, At-Large: {:d}, Located: {:d}, In-Transit: {:d}, Collected: {:d}'.format(
      self.time_keep['episode'],
      self.time_keep['step'],
      self.cube_state['at-large'],
      self.cube_state['located'],
      self.cube_state['in-transit'],
      self.cube_state['collected']
    )
    text_surface = self.board_font.render(sb_string, True, self.font_color)
    text_dest = self.image.get_rect().move(
      (self.image.get_rect().width - text_surface.get_rect().width) / 2,
      (self.image.get_rect().height - text_surface.get_rect().height) / 2
    )
    self.image.fill((0, 0, 0))
    self.image.blit(text_surface, text_dest)

# vim: set ts=2 sw=2 expandtab:
