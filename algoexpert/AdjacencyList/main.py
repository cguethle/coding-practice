# V = 5
# graph = Graph(V)
# graph.add_edge(0, 1)
# graph.add_edge(0, 4)
# graph.add_edge(1, 2)
# graph.add_edge(1, 3)
# graph.add_edge(1, 4)
# graph.add_edge(2, 3)
# graph.add_edge(3, 4)
#
# graph.print_graph()


# Adjacency list of vertex 0
# head -> 1-> 4
#
# Adjacency list of vertex 1
# head -> 0-> 2-> 3-> 4
#
# Adjacency list of vertex 2
# head -> 1-> 3
#
# Adjacency list of vertex 3
# head -> 1-> 2-> 4
#
# Adjacency list of vertex 4
# head -> 0-> 1-> 3

class ConnectedNode:

	def __init__(self, vertex, next_vertex=None):
		self.vertex = vertex
		self.next = next_vertex


class Graph:

	def __init__(self, size):
		"""
		start a graph
		:param size: number of vertices
		"""
		self._graph = [None]*size

	@staticmethod
	def _adjacent_nodes(starting_node: ConnectedNode):
		while starting_node:
			yield starting_node
			starting_node = starting_node.next

	def show_graph(self):
		for vertex in self._graph:
			if vertex:
				for adjacent_node in self._adjacent_nodes(vertex):
					print(f" -> {adjacent_node.vertex}", end="")
				print("\n")

	def add_edge(self, src: int, dst: int):
		"""
		add an edge from one vertex to another.

		adding an edge results in
		:param src:
		:param dst:
		:return:
		"""
		# undirected.
		for a, b in [(src, dst), (dst, src)]:
			self._graph[b] = ConnectedNode(a, self._graph[b])


class Graph2:
	def __init__(self, size):
		"""
		start a graph
		:param size: number of vertices
		"""
		self._graph = [None]*size

	def show_graph(self):
		for idx, v in enumerate(self._graph):
			print(idx, v)
			print(f"Edges from {idx}:", end="")
			if v:
				for dst in v:
					print(f" {dst}", end="")
				print("\n", end="")
			else:
				print(" None")

	def add_edge(self, src, dst):
		if self._graph[src] is None:
			self._graph[src] = set([dst])
		else:
			self._graph[src].add(dst)

		if self._graph[dst] is None:
			self._graph[dst] = set([src])
		else:
			self._graph[dst].add(src)

		print(f"add_edge: {self._graph}")


if __name__ == "__main__":
	graph = Graph2(5)
	# graph.show_graph()
	graph.add_edge(0, 1)
	graph.add_edge(0, 4)
	graph.add_edge(1, 2)
	graph.add_edge(1, 3)
	graph.add_edge(1, 4)
	graph.add_edge(2, 3)
	graph.add_edge(3, 4)
	graph.show_graph()
	print(graph._graph)
