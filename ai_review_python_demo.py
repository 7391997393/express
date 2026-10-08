import os
API_TOKEN = os.getenv("API_TOKEN")
def authenticate(user_token):
    return user_token == API_TOKEN
