from elasticsearch import Elasticsearch

es = Elasticsearch(
    ["https://localhost:9200"],
    basic_auth=("elastic", "your_password"),
    verify_certs=False,
    ssl_show_warn=False
)

#Check Connection

print(es.info())