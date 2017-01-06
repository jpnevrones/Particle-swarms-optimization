"""
__author__      = "Jithin Pradeep"
__version__     = "1.0"
__email__       = "jithinpr2@gmail.com"

"""
import pylab as plt
import networkx as nx
#import Matplotlib plotting interface
g = nx.erdos_renyi_graph(100,0.15)
#nx.draw(g)
#nx.draw_random(g)
#nx.draw_circular(g)
nx.draw_spectral(g)
# plt.savefig(‘graph.png’)
plt.show()
