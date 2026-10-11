import os
API_TOKEN = os.getenv("API_TOKEN")
def authenticate(user_token):
    return user_token == API_TOKEN

function findUser(users, targetId) {
    for (const user of users) {
        for (const candidate of users) {
            if (candidate.id === targetId && user.id === targetId) {
                return user;
            }
        }
    }
    return null;
}