#!/bin/python3
import sys
print(sys.getrecursionlimit())
import math
import os
import random
import re
import sys
from queue import Queue

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
LEFT_LEAF = 0
RIGHT_LEAF = 1


def swapNodes(indexes, queries):
    indexes.insert(0, [None, None])     # prepend [None,None] to simplify node lookup
    results = []
    max_depth = get_max_depth(indexes, 1)
    for k in queries:
        depths_to_swap = [depth for depth in range(1, max_depth + 1) if depth % k == 0]
        if depths_to_swap:
            nodes = get_nodes_at_kth_depths(indexes, depths_to_swap)
            for node in nodes:
                indexes[node][LEFT_LEAF], indexes[node][RIGHT_LEAF] = \
                    indexes[node][RIGHT_LEAF], indexes[node][LEFT_LEAF]
            traversal = in_order_traversal(indexes, 1)
            results.append(" ".join(map(str, traversal)).split())
    return results or \
           [" ".join(map(str, in_order_traversal(indexes, 1))).split()]


def get_nodes_at_kth_depths(data, depths):
    # depths is a list of depths to grab nodes from....
    nodes = []
    max_depth = depths[-1]
    children_to_search = Queue()
    children_to_search.put((1, 1))
    while not children_to_search.empty():
        curr_node, curr_node_depth = children_to_search.get()
        if curr_node_depth in depths:
            nodes.append(curr_node)
        if curr_node_depth < max_depth:
            if data[curr_node][LEFT_LEAF] > -1:
                children_to_search.put((data[curr_node][LEFT_LEAF], curr_node_depth + 1))
            if data[curr_node][RIGHT_LEAF] > -1:
                children_to_search.put((data[curr_node][RIGHT_LEAF], curr_node_depth + 1))

    return nodes


def in_order_traversal(data, node):
    output = []

    if node > -1:  # make sure we are dealing with a node and not a dead end.
        output.extend(in_order_traversal(data, data[node][LEFT_LEAF]))
        output.append(node)
        output.extend(in_order_traversal(data, data[node][RIGHT_LEAF]))

    return output


def get_max_depth(data, node):
    left, right = data[node][LEFT_LEAF], data[node][RIGHT_LEAF]

    return max(
        get_max_depth(data, left) if left > -1 and left < len(data) else 0,
        get_max_depth(data, right) if right > -1 and right < len(data) else 0
    ) + 1


if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    with open('input.txt', 'r') as input_file:

        n = int(input_file.readline().strip())

        indexes = []

        for _ in range(n):
            indexes.append(list(map(int, input_file.readline().rstrip().split())))

        queries_count = int(input_file.readline().strip())

        queries = []

        for _ in range(queries_count):
            queries_item = int(input_file.readline().strip())
            queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()


# def has_children(data, node=None):
#     node = 1 if node is None else node
#     try:
#         return data[node][LEFT_LEAF] > -1 or data[node][RIGHT_LEAF] > -1
#     except IndexError:
#         return False

# def get_child_node(data, side, node):
#     # print(f"get_child_node: {data}, {side}, {node}")
#     return data[node][side]