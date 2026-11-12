from flask import Flask, jsonify

app = Flask(__name__)

users = {
    1: {"id": 1, "name": "Deepak"},
    2: {"id": 2, "name": "Rahul"}
}

@app.get("/health")
def health():
    return jsonify({"status": "healthy", "service": "users"})

@app.get("/users/<int:user_id>")
def get_user(user_id):
    user = users.get(user_id)

    if user:
        return jsonify(user)

    return jsonify({"error": "User not found"}), 404

@app.get("/")
def home():
    return jsonify({"service": "users", "message": "Users service running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
