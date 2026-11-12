from flask import Flask, request, jsonify
import requests
import socket
import os

app = Flask(__name__)

USERS_URL = os.environ.get("USERS_URL", "http://users:5001")
PRODUCTS_URL = os.environ.get("PRODUCTS_URL", "http://products:5002")

@app.get("/health")
def health():
    return jsonify({"status": "healthy", "service": "orders"})

@app.post("/orders")
def create_order():
    data = request.get_json()

    user_id = data.get("user_id")
    product_id = data.get("product_id")
    qty = data.get("qty", 1)

    user_response = requests.get(f"{USERS_URL}/users/{user_id}")
    product_response = requests.get(f"{PRODUCTS_URL}/products/{product_id}")

    if user_response.status_code != 200:
        return jsonify({"error": "User not found"}), 404

    if product_response.status_code != 200:
        return jsonify({"error": "Product not found"}), 404

    user = user_response.json()
    product = product_response.json()

    order = {
        "message": "Order created successfully",
        "user": user,
        "product": product,
        "qty": qty,
        "total": product["price"] * qty,
        "served_by": socket.gethostname()
    }

    return jsonify(order), 201

@app.get("/")
def home():
    return jsonify({"service": "orders", "message": "Orders service running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
