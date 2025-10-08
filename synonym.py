from elasticsearch import Elasticsearch, helpers

# Connect to Elasticsearch
es = Elasticsearch(
    ["https://localhost:9200"],
    basic_auth=("elastic", "your_password"), 
    verify_certs=False
)

# Sample documents
docs = [
{"_index": "products", "_id": 1, "_source": {"product_name": "car battery", "city": "Dhaka"}},
{"_index": "products", "_id": 2, "_source": {"product_name": "automobile tires", "city": "Chattogram"}},
{"_index": "products", "_id": 3, "_source": {"product_name": "mobile case", "city": "Sylhet"}},
{"_index": "products", "_id": 4, "_source": {"product_name": "notebook charger", "city": "Khulna"}}

]

# Bulk insert
helpers.bulk(es, docs)

print("✅ Documents inserted successfully!")