

class Graph:
    n_nodes = 0
    adj_matrix = [[]]
    neighbor = {}
    def __init__(self, n):
        self.n_nodes = n
        self.adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.neighbor   = {i:[] for i in range(n)}
        
    def add_edge(self, node_i, node_j):
        self.adj_matrix[node_i][node_j] = 1
        self.adj_matrix[node_j][node_i] = 1
        self.neighbor.get(node_i, []).append(node_j)
        self.neighbor.get(node_j, []).append(node_i)
        
    def set_adj_matrix(self, M):   
        self.adj_matrix = M
        self.n_nodes = len(M)
        for thisnode in range(self.n_nodes):
            self.neighbor.setdefault(thisnode,[])
            for othernode, is_connected in enumerate(self.adj_matrix[thisnode]):
                if is_connected == 1:
                    self.neighbor.get(thisnode, []).append(othernode)


    def get_neighbor(self, node):
        return self.neighbor.get(node, [])
    
    def get_shortest_path(self, start_node):
        visited = [False for _ in range(self.n_nodes) ]
        distance = [-1 for _ in range(self.n_nodes)]
        #visitfrom = [-1 for _ in range(self.n_nodes)]
        visited[start_node] = True
        distance[start_node] = 0
        to_visit_neighbors = [start_node]
        while not not to_visit_neighbors:
            thisnode = to_visit_neighbors.pop(0)
            node_neighbors = self.get_neighbor(thisnode)
            for othernode in node_neighbors:
                if not visited[othernode]:
                    visited[othernode] = True
                    distance[othernode] = distance[thisnode] + 1
                    to_visit_neighbors.append(othernode)
        return distance    
    def get_connected_components(self):
        visited = [False for _ in range(self.n_nodes) ]
        comp_all = dict()
        for n in range(self.n_nodes):
            if not visited[n]:
                visited[n] = True
                to_visit_neighbors = [n]
                comp_all.setdefault(n, set([n]))
                while not not to_visit_neighbors:
                    thisnode = to_visit_neighbors.pop(0)
                    node_neighbors = self.get_neighbor(thisnode)
                    comp_all.get(n, set([])).update(set(node_neighbors))
                    for othernode in node_neighbors:
                        if not visited[othernode]:
                            visited[othernode] =True
                            to_visit_neighbors.append(othernode)
        return comp_all
if __name__ == '__main__':
    adj_matrix = [[1,1,0,0,0,1],[1,1,0,0,0,0],[0,0,1,0,1,0], [0,0,0,1,0,0],[0,0,1,0,1,0],[1,0,0,0,0,1]]
    g = Graph(6)
    g.set_adj_matrix(adj_matrix)
    all_components = g.get_connected_components()
    for k in all_components:
        print(all_components[k])
#    fid = open('C:\\Users\\debs_\\Downloads\\input06_shortest_path.txt', 'r')
#    fout = open('C:\\Users\\debs_\\Downloads\\output06_shortest_path.txt', 'r')
#    t = int(fid.readline().strip())
#    for i in range(t):
#        n,m = [int(value) for value in fid.readline().strip().split()]
#        graph = Graph(n)
#        for i in range(m):
#            x,y = [int(x) for x in fid.readline().strip().split()]
#            graph.add_edge(x-1,y-1) 
#        s = int(fid.readline().strip())
#        all_dist = graph.get_shortest_path(s-1)
#        #print(all_dist)
#        new_dist = []
#        for i in range(n):
#            if s-1 != i:
#                new_dist.append(str(all_dist[i]))
#        c_dist = fout.readline().strip().split(' ')
#        print('len of my output =' + str(len(all_dist)))
#        print('len of output =' + str(len(c_dist)))
#        for i in range(len(c_dist)):
#            print(str(all_dist[i]) + ' ' +str(c_dist[i]) )
#        #print(' '.join(new_dist))
#    fid.close()
#    fout.close()