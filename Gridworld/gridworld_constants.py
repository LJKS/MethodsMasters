TILE_TYPE_END = 'E'
TILE_TYPE_FREE = 'F'
TILE_TYPE_PIT = 'P'
TILE_TYPE_OBSTACLE = 'O'

DIRECTION_NORTH = '^'
DIRECTION_EAST = '>'
DIRECTION_SOUTH = 'v'
DIRECTION_WEST = '<'

DIRECTIONS = {DIRECTION_NORTH: (-1, 0), DIRECTION_EAST: (0, 1), DIRECTION_SOUTH: (1, 0), DIRECTION_WEST: (0, -1)}
REWARDS = {TILE_TYPE_END: 1, TILE_TYPE_FREE: -0.4, TILE_TYPE_PIT: -1, TILE_TYPE_OBSTACLE: 'O'}
PROBABILITIES = (0.8, 0.1, 0.1)




