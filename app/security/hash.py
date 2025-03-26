import hashlib

def hash_object(object):

    encoded_object = object.encode()
    hash_object = hashlib.sha256(encoded_object)
    hex_dig = hash_object.hexdigest()
    return hex_dig