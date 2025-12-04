import hashlib

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def verify_data(original, received):
    original_hash = generate_hash(original)
    received_hash = generate_hash(received)
    return original_hash == received_hash, original_hash, received_hash

original_data = "Hello World"
modified_data = "Hello Wor1d"

status, orig_hash, recv_hash = verify_data(original_data, modified_data)

print("Original Hash:", orig_hash)
print("Received Hash:", recv_hash)
print("Integrity Verified:", status)
