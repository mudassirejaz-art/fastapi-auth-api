import requests

BASE_URL = "http://127.0.0.1:8000"

# ---- Step 1: Login ----
def login(client_key, secret_key):
    url = f"{BASE_URL}/login"
    payload = {
        "client_key": client_key,
        "secret_key": secret_key
    }
    r = requests.post(url, json=payload)
    print("Login Response:", r.status_code, r.json())
    return r.json()

# ---- Step 2: /me endpoint ----
def get_me(token):
    url = f"{BASE_URL}/me"
    payload = {"token": token}
    r = requests.get(url, json=payload)
    print("Me Response:", r.status_code, r.json())
    return r.json()

# ---- Step 3: /secure-data endpoint ----
def get_secure_data(token):
    url = f"{BASE_URL}/secure-data"
    payload = {"token": token}
    r = requests.get(url, json=payload)
    print("Secure Data Response:", r.status_code, r.json())
    return r.json()


if __name__ == "__main__":
    # 👇 apna test user ka keys dal do
    client_key = "myclient123"
    secret_key = "mysecret456"

    login_data = login(client_key, secret_key)

    if "access_token" in login_data:
        token = login_data["access_token"]

        # Test /me
        get_me(token)

        # Test /secure-data
        get_secure_data(token)
    else:
        print("❌ Login failed, check your client_key / secret_key")
