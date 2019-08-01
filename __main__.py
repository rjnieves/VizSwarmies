import sys
import csv
import pygame
from board import GameBoard, ScoreBoard

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Usage: python . <activity log CSV>')
    sys.exit(1)
  activity_log_path = sys.argv[1]
  time_keep = {
    'episode': 0,
    'step': 0
  }
  cube_state = {
    'at-large': 0,
    'located': 0,
    'in-transit': 0,
    'collected': 0
  }
  pygame.init()
  game_board = GameBoard((30, 30), (2, 2), (14, 14), (30, 30))
  sb_font = pygame.font.Font(pygame.font.get_default_font(), 20)
  score_board = ScoreBoard(cube_state, time_keep, (game_board.board_pix_size[0], 100), sb_font)
  score_board_rect = score_board.image.get_rect()
  screen = pygame.display.set_mode((game_board.board_pix_size[0], game_board.board_pix_size[1] + 100))
  game_board_surface = pygame.Surface(game_board.board_pix_size)
  score_board_surface = pygame.Surface((score_board_rect.width, score_board_rect.height))
  score_board_group = pygame.sprite.GroupSingle(score_board)
  with open(activity_log_path, 'r') as csvfile:
    activity_reader = csv.reader(csvfile, delimiter=',')
    for event in activity_reader:
      if int(event[0]) != time_keep['episode']:
        pygame.time.wait(100)
        time_keep['episode'] = int(event[0])
        game_board.reset_all()
        time_keep['step'] = 0
        for a_key in cube_state.keys():
          cube_state[a_key] = 0
      if int(event[1]) != time_keep['step']:
        pygame.time.wait(100)
        time_keep['step'] = int(event[1])
      if event[2] == 'CUBE':
        cube_loc = (
          int(event[4]),
          int(event[5])
        )
        game_board.get_cube_count_sprite(cube_loc).count_value += 1
        cube_state['at-large'] += 1
      elif event[2] == 'PICKUP':
        swarmie_id = int(event[3])
        cube_loc = (
          int(event[4]),
          int(event[5])
        )
        cube_count_sprite = game_board.get_cube_count_sprite(cube_loc)
        cube_count_sprite.count_value -= min(cube_count_sprite.count_value, 1)
        game_board.swarmie_sprites[swarmie_id].carrying = True
        game_board.get_grid_cell_sprite(cube_loc).occupied = False
        cube_state['located'] -= min(cube_state['located'], 1)
        cube_state['in-transit'] += 1
      elif event[2] == 'COLLECT':
        swarmie_id = int(event[3])
        game_board.swarmie_sprites[swarmie_id].carrying = False
        game_board.nest_count_sprite.count_value += 1
        cube_state['in-transit'] -= min(cube_state['in-transit'], 1)
        cube_state['collected'] += 1
      elif event[2] == 'POS':
        swarmie_id = int(event[3])
        swarmie_pos = (
          int(event[4]),
          int(event[5])
        )
        game_board.swarmie_sprites[swarmie_id].grid_coord = swarmie_pos
      elif event[2] == 'CUBESPOT':
        cell_pos = (
          int(event[4]),
          int(event[5])
        )
        grid_cell_sprite = game_board.get_grid_cell_sprite(cell_pos)
        if not grid_cell_sprite.occupied:
          cube_state['located'] += 1
          cube_state['at-large'] -= min(cube_state['at-large'], 1)
        grid_cell_sprite.occupied = True
        
      elif event[2] == 'DROP':
        swarmie_id = int(event[3])
        cell_pos = game_board.swarmie_sprites[swarmie_id].grid_coord
        game_board.get_cube_count_sprite(cell_pos).count_value += 1
        cube_state['at-large'] += 1
        cube_state['in-transit'] -= min(cube_state['located'], 1)
      screen.fill((0, 0, 0))
      game_board.update()
      game_board_surface.fill((0, 0, 0))
      game_board.draw(game_board_surface)
      score_board.update()
      score_board_surface.fill((0, 0, 0))
      score_board_group.draw(score_board_surface)
      screen.blit(score_board_surface, (0, 0))
      screen.blit(game_board_surface, (0, 100))
      pygame.display.flip()
      pygame.event.pump()

# vim: set ts=2 sw=2 expandtab:
