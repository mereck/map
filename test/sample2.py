import networkx as nx
def main():
        g=nx.MultiDiGraph()
        nj = "nj"
        ny = "ny"
        pa = "pa"
        padict= {'temp':85,'humidity':'low'}
        va = "va"
        vadict= {'temp':87,'humidity':'high'}
	g.add_node(nj)
	g.add_node(ny)
	g.add_nodes_from([(pa,padict),(va,vadict)])
	print g.nodes(data=True)
	
if __name__== '__main__':
	main()









