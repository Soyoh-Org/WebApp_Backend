from . import Session
from bson import json_util
import json


def find(collection_name, query={}):
    collection = Session[collection_name]
    items = []
    for item in collection.find(query):
        items.append(json.loads(json.dumps(item, indent=4, default=json_util.default)))

    result = items if len(items) > 1 else items[0]
    return result


def insert(collection_name, item):
    collection = Session[collection_name]
    insert_result = collection.insert_one(item)
    result = {
        'inserted_id': str(insert_result.inserted_id),
        'generation_time': str(str(insert_result.inserted_id.generation_time))
    }
    return result


def delete(collection_name, item):
    collection = Session[collection_name]
    delete_result = collection.delete_one(item)
    result = {
        'deleted_items': delete_result.deleted_count
    }
    return result
