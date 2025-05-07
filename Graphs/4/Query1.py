import rdflib
from rdflib import Graph

g = Graph()

g.parse("Graphs/4/BFO-Graph.ttl")



q = """
PREFIX obo: <http://purl.obolibrary.org/obo/bfo#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX ex: <http://semanticweb.org/ontology/example/> 
SELECT *
WHERE {
    ?s obo:BFO_0000056 ?process .
    ?process obo:BFO_0000199 ?temporalRegion .
}
"""

results = g.query(query_object=q)
print("\n","RESULTS:")
for row in results:
    rr = []
    for item in row:
        rr.append(str(item))
    print(rr,'\n')
print('\n')



