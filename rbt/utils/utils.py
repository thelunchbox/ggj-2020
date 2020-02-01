import json

# takes in json object, returns bytes
def serialize(data):
    return json.dumps(data).encode('utf-8')

# takes in bytes, returns json object
def deserialize(bytes):
    return json.loads(bytes.decode('utf-8'))