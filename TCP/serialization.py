import pickle


def serialize(data):
    serialized = pickle.dumps(data)
    return serialized


def deserialization(data):
    deserialized = pickle.loads(data)
    return deserialized
