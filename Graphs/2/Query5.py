import rdflib
from rdflib import Graph

g = Graph()

g.parse("Graphs/2/Foaf-Graph.ttl")


# This query shows us how to use the "FILTER" keyword
q = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
SELECT ?p
WHERE {
    ?p foaf:age ?value .
    FILTER NOT EXISTS { ?p foaf:knows foaf:Stewart }

}
"""

results = g.query(q)
print("\n",'\n','\n',"\n",'\n','\n',"RESULTS:")
# g2 = Graph()
for row in results:
    print(str(row[0]))
print("\n","\n","\n")


