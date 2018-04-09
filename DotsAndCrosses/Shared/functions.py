import pickle


def serialization(board):
    serialized = pickle.dumps(board)
    return serialized


def deserialization(board):
    deserialized = pickle.loads(board)
    return deserialized
