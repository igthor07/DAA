# Write a program to solve a  Travelling Salesman Problem using dynamic programming or branch and
# bound strategy. 
import itertools

def tsp_dynamic_programming(graph):
    n = len(graph)

    # Generate all possible subsets of cities
    all_sets = [frozenset(subset) for subset in itertools.combinations(range(n), n)]

    # Initialize the memoization table
    memo = {}

    # Initialize the start and end node
    start = 0

    # Initialize the memoization table with base case
    for end in range(1, n):
        memo[(frozenset({end}), end)] = (graph[start][end], start)

    # Iterate over subsets of cities
    for r in range(2, n):
        for subset in itertools.combinations(range(1, n), r):
            for end in subset:
                if end == start:
                    continue
                min_dist = float('inf')
                prev_city = None
                mask = frozenset(set(subset) - {end})
                for k in subset:
                    if k == end:
                        continue
                    new_dist = memo.get((mask, k), (float('inf'), None))[0] + graph[k][end]
                    if new_dist < min_dist:
                        min_dist = new_dist
                        prev_city = k
                memo[(subset, end)] = (min_dist, prev_city)

    # Find the shortest tour
    end_subset = frozenset(range(1, n))
    min_dist_to_end = [(memo.get((end_subset, end), (float('inf'), None))[0] + graph[end][start], end) for end in range(1, n)]
    tour_min = min(min_dist_to_end)

    # Reconstruct the tour
    tour = [start]
    cur_node = tour_min[1]
    end_subset -= {cur_node}

    for _ in range(n - 1):
        prev_node = memo.get((end_subset, cur_node), (float('inf'), None))[1]
        tour.append(prev_node)
        end_subset -= {prev_node}
        cur_node = prev_node

    tour.append(start)
    tour_length = tour_min[0]

    return tour, tour_length

# Example usage
graph = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]

]

tour, tour_length = tsp_dynamic_programming(graph)

print("Optimal Tour:", tour)
print("Tour Length:", tour_length)
