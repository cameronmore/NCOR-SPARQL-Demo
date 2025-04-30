import rdflib
from rdflib import Graph

g = Graph()

g.parse("Graphs/1/Foaf-Graph.ttl")



q = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
CONSTRUCT {
    ?p2 foaf:knows ?p1
}
WHERE {
    ?p1 foaf:knows ?p2 .
}
"""

results = g.query(q)
print("\n",'\n','\n',"\n",'\n','\n',"RESULTS:")
# g2 = Graph()
for row in results:
    g.add((row))
print(g.serialize(format="ttl"))


