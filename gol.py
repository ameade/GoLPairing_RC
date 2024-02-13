import copy



def dead_or_alive(world, row, col):
    row_coord = row
    col_coord = col
    if row >= len(world):
        row_coord = row % len(world)
    if col >= len(world[row_coord]):
        col_coord = col % len(world[row_coord])
    return world[row_coord][col_coord]

def count_neighbors(world, row, col):
    count = 0
    for row_mod in (-1, 0, 1):
        for col_mod in (-1, 0, 1):
            if not row_mod == col_mod == 0:
                count += dead_or_alive(world, row + row_mod, col + col_mod)

    return count

def progress_world(old_world):
    """ Return the next state of the game world.

    :param old_world: A 2d array with 0's representing dead cells and 1's representing live cells
    :return: Next state of the world with game of life rules applied
    """
    return copy.deepcopy(old_world)

def print_world(world):
    for row in world:
        row_string = "".join([str(cell) for cell in row])
        print(row_string)


if __name__ == "__main__":
    print_world([[0, 0], [0, 0]])