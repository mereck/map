import networkx as nx
import sys
def main():
    t = "Hello, World!"
    print(t)
if __name__ == '__main__': 
	try:
		main()
	except:
		print'Error:',sys.exc_info()[0]
		print'Resolve error before running again!'