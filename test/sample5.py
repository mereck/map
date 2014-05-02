#translating deletion of nodes and edges
#when deleting the edge, should check if the edge is directed or undirected
import networkx as nx
import matplotlib.pyplot as plt
def main():
        g=nx.MultiDiGraph()
        nj = ["nj"]
        ny = ["ny"]
        fl= ["fl"]
        pa = ["pa", {'temp':85,'humidity':'low'}]
        va = ["va", {'temp':87,'humidity':'high'}]
        #instantiating edges
        flight1= [nj[0],ny[0]]
        flight2 = [ny[0], pa[0]]
        flight3= [pa[0],va[0],{'cost':302, 'distance':4092}]
        flight4= [va[0],nj[0]]
        flight5 = [nj[0],fl[0], {'cost':50, 'distance':5000}]
        g.add_node(nj[0])
        g.add_node(ny[0])
        g.add_node(fl[0])
        g.add_nodes_from([(pa[0],pa[1]),(va[0],va[1])])
        #adding edges to the graph
        g.add_edge(flight1[0],flight1[1])
        g.add_edges_from([(flight2[0],flight2[1]),(flight3[0],flight3[1],flight3[2])])
        g.add_edges_from([(flight4[0],flight4[1]),(flight4[1],flight4[0])])
        g.add_edges_from([(flight5[0],flight5[1],flight5[2]),(flight5[1],flight5[0],flight5[2])])
        print g.nodes(data=True)
	print g.edges(data=True)
	g.remove_node(pa[0])
	g.remove_nodes_from([(va[0]), (ny[0])])
	print g.edges(data=True)
	g.remove_edges_from([(nj[0],fl[0]),(fl[0],nj[0])])
	print g.edges(data=True)
	nx.draw(g)
	plt.show()
	

if __name__== '__main__':
        main()