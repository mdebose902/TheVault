import hashlib

#hashing functio, sha256
def hasher(password):
    hashed = hashlib.sha256(password.encode())
    return hashed.hexdigest()

