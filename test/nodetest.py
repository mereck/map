import networkx as nx
import sys
def main():
    g = nx.MultiDiGraph()
    no2 = 'los angeles', {'temp':90.0,'weather':'cloudy with a chance'}
    g.add_node(no2[0], no2[1])
    g.remove_node(no2[0])
if __name__ == '__main__': 
	main()