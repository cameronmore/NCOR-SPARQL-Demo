import rdflib
from rdflib import Graph

g = Graph()

g.parse("Graphs/3/Foaf-Graph.ttl")


# We can also query on Literal values (strings, booleans, integers, decimals, and so on)
q = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
SELECT ?p1 ?age
WHERE {
    ?p1 foaf:knows ?p2 .
    ?p1 foaf:age ?age .
    
    ?p2 foaf:knows ?p3 .
    ?p2 foaf:birthday ?bday1 .
    
    ?p3 foaf:knows ?p4 .
    ?p3 foaf:birthday ?bday2 .
    
    ?p4 foaf:lastName ?lastNameValue .
    FILTER regex (?lastNameValue, "McDonald") 
    FILTER ( ?bday1 = ?bday2 )
}
"""

results = g.query(q)
print("\n",'\n','\n',"\n",'\n','\n',"RESULTS:")
# g2 = Graph()
for row in results:
    print(str(row[0]),"   ",row[1],"\n","\n","\n")


