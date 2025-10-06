from elasticsearch import Elasticsearch, helpers

# Connect to Elasticsearch
es = Elasticsearch(
    ["https://localhost:9200"],
    basic_auth=("elastic", "your_password"), 
    verify_certs=False
)

# Sample documents
docs = [
    {"_index": "new_index", "_id": 1, "_source": {"name": "Alice", "age": 23, "city": "Dhaka"}},
    {"_index": "new_index", "_id": 2, "_source": {"name": "Bob", "age": 30, "city": "Chattogram"}},
    {"_index": "new_index", "_id": 3, "_source": {"name": "Charlie", "age": 28, "city": "Sylhet"}},
    {"_index": "new_index", "_id": 4, "_source": {"name": "Diana", "age": 35, "city": "Khulna"}},
]

# Bulk insert
helpers.bulk(es, docs)

print("✅ Documents inserted successfully!")
