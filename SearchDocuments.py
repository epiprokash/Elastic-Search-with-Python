from elasticsearch import Elasticsearch

es = Elasticsearch(
    ["https://localhost:9200"],
    basic_auth=("elastic", "6gzHNHuEBQj_x17n-yux"),
    verify_certs=False,
    ssl_show_warn=False
)

resp = es.search(index="new_index", query={"match_all": {}})
for hit in resp["hits"]["hits"]:
    print(hit["_source"])
