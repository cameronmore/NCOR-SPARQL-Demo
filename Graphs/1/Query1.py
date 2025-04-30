import rdflib
from rdflib import Graph

g = Graph()

g.parse("Graphs/1/Foaf-Graph.ttl")

q1 = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
SELECT ?person
WHERE {
    ?person foaf:knows foaf:Bill .
}
"""

results = g.query(q1)
print("\n","RESULTS:")
for row in results:
    print(str(row[0]))

