from pymilvus import connections, Collection

# Connect to Milvus
connections.connect("default", host="localhost", port="19530")

def search_milvus(vector, top_k=5):
    collection = Collection("asana_tasks")  # Replace with your collection name
    results = collection.search(
        data=[vector],
        anns_field="vector_field",  # Replace with your vector field
        param={"metric_type": "IP", "params": {"nprobe": 10}},
        limit=top_k,
    )
    return results
