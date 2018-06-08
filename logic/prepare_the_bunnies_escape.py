from collections import deque


def get_siblings(maze, maze_width_minus_one, maze_length_minus_one, node):
    neighbors = deque()

    row, col, can_destroy = node[:3]

    # For x, we know that if the val is greater than 0, or less than maze length minus one, it is safe to access the
    # val from the map
    if row > 0:
        wall = maze[row - 1][col] == 1
        if wall:
            if can_destroy:
                neighbors.appendleft((row - 1, col, False))
        else:
            neighbors.appendleft((row - 1, col, can_destroy))

    if row < maze_length_minus_one:
        wall = maze[row + 1][col] == 1
        if wall:
            if can_destroy:
                neighbors.appendleft((row + 1, col, False))
        else:
            neighbors.appendleft((row + 1, col, can_destroy))

    # For y, we know that if the val is greater than 0, or less than maze width minus one, it is safe to access the
    # val from the map
    if col > 0:
        wall = maze[row][col - 1] == 1
        if wall:
            if can_destroy:
                neighbors.appendleft((row, col - 1, False))
        else:
            neighbors.appendleft((row, col - 1, can_destroy))

    if col < maze_width_minus_one:
        wall = maze[row][col + 1] == 1
        if wall:
            if can_destroy:
                neighbors.appendleft((row, col + 1, False))
        else:
            neighbors.appendleft((row, col + 1, can_destroy))

    return neighbors


def answer(maze):
    """Iterate through the maze created on init. For each node in the queue, check all it's siblings and traverse
            through the maze until you reach the end.

    :return: int() --> path length
    """
    maze_width_minus_one = len(maze[0]) - 1
    maze_length_minus_one = len(maze) - 1

    # Establish queue to keep track of node progress
    queue = deque()
    # __node = ['row', 'col', 'can_destroy']
    queue.appendleft((0, 0, True))

    log_distance = {(0, 0, True): 1}

    while True:
        # unpack the node
        current_node = queue.pop()

        # We reach the end of the map
        if current_node[0] == maze_length_minus_one and current_node[1] == maze_width_minus_one:
            return log_distance[current_node]

        for sibling_node in get_siblings(maze, maze_width_minus_one, maze_length_minus_one, current_node):
            # If we havent seen this node before..
            if sibling_node not in log_distance:
                # add the distance to the node
                log_distance[sibling_node] = log_distance[current_node] + 1

                # append new node to the queue
                queue.appendleft(sibling_node)
