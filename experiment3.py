import hashlib, uuid

SECRET = "my_secret_password"

def hash_value(challenge, secret=SECRET):
    return hashlib.sha256((challenge + secret).encode()).hexdigest()

def issue_challenge():
    return str(uuid.uuid4())

def authenticate():
    challenge = issue_challenge()
    print("Server Challenge:", challenge)

    client_resp = hash_value(challenge)
    server_resp = hash_value(challenge)

    if client_resp == server_resp:
        print("Authentication Successful")
        return challenge, client_resp
    else:
        print("Authentication Failed")
        return challenge, None

challenge, valid_resp = authenticate()

print("\n--- Replay Attack Simulation ---")
new_challenge = issue_challenge()
print("New Challenge (server):", new_challenge)

attacker_resp = valid_resp
print("Attacker Replay Response:", attacker_resp)

expected_resp = hash_value(new_challenge)

if attacker_resp == expected_resp:
    print("Replay Attack Successful (Should not happen!)")
else:
    print("Replay Attack Detected")
