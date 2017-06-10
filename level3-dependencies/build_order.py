def build_order(pkgs):
    # build the graph
    class graph(object):
        def __init__(self):
            self.nodes = set()
            self.adjacencyList = {}

        def add_node(self, node):
            self.nodes.add(node)

        def add_edge(self, node1, node2):
            if node1 in self.adjacencyList:
                self.adjacencyList[node1].append(node2)
            else:
                self.adjacencyList[node1] = [node2]

    g = graph()

    for pkg, deps in pkgs.items():
        g.add_node(pkg)
        for dep in deps:
            g.add_node(dep)
            g.add_edge(pkg, dep)

    # if each node is not in the adjacency list
    for node in g.nodes:
        if node not in pkgs:
            raise ValueError
    # so topolgical sort only works on acylcic graphs
    # so here I'm doing DFS so I have to detect cycles
    # so I'm marking nodes
    order = []
    visited = {}
    marked = set()

    def DFS(g, v):
        if visited.get(v, False):
            raise ValueError
        if v in marked:
            return
        visited[v] = True
        for neighbours in g.adjacencyList.get(v, []):
            DFS(g, neighbours)

        visited[v] = False
        marked.add(v)
        order.append(v)
    for node in g.nodes:
        # if node is unmarked
        if node in marked.symmetric_difference(g.nodes):
            DFS(g, node)

    return order
