from util import neighbors4, neighbors8, tokenedlines, getlines

day = "12"
# day = "ex"

def get_region_and_score(start, grid):
    todo = [start]
    region = set(todo)
    my_color = grid[start[0]][start[1]]
    correct_neighbors = 0
    while todo:
        r, c = todo.pop()
        for newr, newc in neighbors4(r, c, grid):
            if grid[newr][newc] == my_color:
                correct_neighbors += 1
                if (newr, newc) not in region:
                    region.add((newr, newc))
                    todo.append((newr, newc))

    incorrect_neighbors = 4 * len(region) - correct_neighbors
    return region, (len(region) * incorrect_neighbors), 

def part1(grid):
    all_visited = set([])
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in all_visited:
                continue
            new_nodes, new_score = get_region_and_score((i, j), grid)

            all_visited.update(new_nodes)
            score += new_score
    return score

def part2(grid):
    all_visited = set([])
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in all_visited:
                continue
            new_nodes, _ = get_region_and_score((i, j), grid)
            all_visited.update(new_nodes)
            # print(f"Region starting at {i},{j} has p2 score {p2score(new_nodes)}")
            score += len(new_nodes) * p2score(new_nodes)
    return score

def p2score(nodes):
    # Build a graph with "holes" between the nodes
    new_grid = [(2 * i + 2, 2 * j + 2) for i, j in nodes]
    maxi = max(node[0] for node in new_grid) + 3
    maxj = max(node[1] for node in new_grid) + 3
    considered_nodes = set()
    p2score = 0
    for node in new_grid:
        for neighbor in neighbors8(*node, maxi, maxj)[4:]:
            # these are the 4 "diagonals" from this node
            if neighbor in considered_nodes:
                continue
            considered_nodes.add(neighbor)
            # Figure out what the four corners look like from here
            adjacent_node_signature = []
            for i, adj in enumerate(neighbors8(*neighbor, maxi, maxj)[4:]):
                if adj in new_grid:
                    adjacent_node_signature.append(i)
            if len(adjacent_node_signature) in [1, 3]:
                # This is either an inside or outside corner
                p2score += 1
            elif adjacent_node_signature in [[0, 3], [1, 2]]:
                # This is has two outside corners of the same region next to it
                p2score += 2
    return p2score
print(part1(getlines(day)))
print(part2(getlines(day)))