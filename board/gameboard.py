import pygame
from sprites import GridCell, CubeCount, Swarmie

class GameBoard(pygame.sprite.LayeredUpdates):
  def __init__(self, cell_pix_size, nest_cell_size, nest_cell_loc, board_cell_size, font_name=None, font_size=16, board_font_color=(127, 127, 127), nest_font_color=(255, 255, 255)):
    super(GameBoard, self).__init__()
    font_name = font_name or pygame.font.get_default_font()
    self.cell_pix_size = cell_pix_size
    self.board_cell_size = board_cell_size
    self.font = pygame.font.Font(font_name, font_size)
    total_pix_size = (board_cell_size[0] * cell_pix_size[0], board_cell_size[1] * cell_pix_size[1])
    nest_cells = []
    for an_x_pos in range(nest_cell_loc[0], nest_cell_loc[0] + nest_cell_size[0]):
      for a_y_pos in range(nest_cell_loc[1], nest_cell_loc[1] + nest_cell_size[1]):
        nest_cells.append((an_x_pos, a_y_pos))
    board_cells = [(idx % board_cell_size[0], int(idx / board_cell_size[1])) for idx in range(board_cell_size[0] * board_cell_size[1])]
    self.grid_cell_sprites = [
      GridCell(self.cell_pix_size, cell_coord)
      for cell_coord in board_cells
    ]
    self.cube_count_sprites = [
      CubeCount(self.cell_pix_size, cell_coord, self.font, board_font_color)
      for cell_coord in board_cells
    ]
    nest_pix_size = (
      self.cell_pix_size[0] * nest_cell_size[0],
      self.cell_pix_size[1] * nest_cell_size[1]
    )
    nest_adj_loc = (
      nest_cell_loc[0] / nest_cell_size[0],
      nest_cell_loc[1] / nest_cell_size[1]
    )
    self.nest_cell_sprite = GridCell(nest_pix_size, nest_adj_loc, matte_color=(255, 0, 0), layer=2)
    self.nest_count_sprite = CubeCount(
      nest_pix_size,
      nest_adj_loc,
      self.font,
      nest_font_color,
      layer=2
    )
    self.swarmie_sprites = [
      Swarmie(self.cell_pix_size, (0, 0), (100, 100, 100)),
      Swarmie(self.cell_pix_size, (0, 0), (127, 0, 127)),
      Swarmie(self.cell_pix_size, (0, 0), (180, 180, 180))
    ]
    self.add(self.grid_cell_sprites, self.cube_count_sprites, self.nest_cell_sprite, self.nest_count_sprite, self.swarmie_sprites)

  @property
  def board_pix_size(self):
    return (self.board_cell_size[0] * self.cell_pix_size[0], self.board_cell_size[1] * self.cell_pix_size[1])

  def get_cube_count_sprite(self, cell_loc):
    sprite_idx = self.board_cell_size[1] * cell_loc[1] + cell_loc[0]
    return self.cube_count_sprites[sprite_idx]

  def get_grid_cell_sprite(self, cell_loc):
    cell_idx = self.board_cell_size[1] * cell_loc[1] + cell_loc[0]
    return self.grid_cell_sprites[cell_idx]

  def reset_all(self):
    for a_cube_count in self.cube_count_sprites:
      a_cube_count.count_value = 0
    self.nest_count_sprite.count_value = 0
    for a_swarmie in self.swarmie_sprites:
      a_swarmie.carrying = False
    for a_grid_cell in self.grid_cell_sprites:
      a_grid_cell.occupied = False

# vim: set ts=2 sw=2 expandtab:
