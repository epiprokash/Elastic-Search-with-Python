from elasticsearch import Elasticsearch

es = Elasticsearch(
    ["https://localhost:9200"],
    basic_auth=("elastic", "your_password"),
    verify_certs=False,
    ssl_show_warn=False
)

#Check Connection

print(es.info())

es.index (index ="test_index", id =1, document = {"name":"Prokash Maitra", "age":24, "course":"MCA"})
es.index (index ="test_index", id =2, document = {"name":"Md Galib Ibn-Kibria", "age":46, "course":"CSE"})
es.index (index ="test_index", id =3, document = {"name":"Muhib", "age":28, "course":"EEE"})
es.index (index ="test_index", id =4, document = {"name":"Sabbir", "age":26, "course":"BBA"})

doc1 = es.get(index ="test_index", id =1)
doc2 = es.get(index ="test_index", id =2)
doc3 = es.get(index ="test_index", id =3)

print(doc1['_source'])
print(doc2['_source'])
print(doc3['_source'])

# Search documents

resp = es.search(
    index="test_index",
    query={"match": {"name": "Prokash"}}
)
print(resp["hits"]["hits"])


#Update document

# es.update(
#     index="test_index",
#     id=1,
#     doc={"age": 26}
# )

#Delete document

# es.delete(index="test_index", id=1)

