import rdflib
from rdflib import Graph

g = Graph()

g.parse("Graphs/2/Foaf-Graph.ttl")


# We can also query on Literal values (strings, booleans, integers, decimals, and so on)
q = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
SELECT ?p
WHERE {
    ?p foaf:age 30 .
}
"""

results = g.query(q)
print("\n",'\n','\n',"\n",'\n','\n',"RESULTS:")
# g2 = Graph()
for row in results:
    print(str(row[0]),"\n","\n","\n")


