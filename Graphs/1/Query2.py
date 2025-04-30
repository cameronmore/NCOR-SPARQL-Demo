import rdflib
from rdflib import Graph

g = Graph()

g.parse("Graphs/1/Foaf-Graph.ttl")



q = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
ASK
WHERE {
    ?person foaf:knows foaf:John .
}
"""

results = g.query(q)
print("\n",'\n','\n',"\n",'\n','\n',"RESULTS:")
for row in results:
    pass
    print(row,"\n","\n",'\n','\n')






