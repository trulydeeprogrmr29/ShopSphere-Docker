from flask import Flask, jsonify

app = Flask(__name__)

products = {
    101: {"id": 101, "name": "Laptop", "price": 50000},
    102: {"id": 102, "name": "Mouse", "price": 500}
}

@app.get("/health")
def health():
    return jsonify({"status": "healthy", "service": "products"})

@app.get("/products/<int:product_id>")
def get_product(product_id):
    product = products.get(product_id)

    if product:
        return jsonify(product)

    return jsonify({"error": "Product not found"}), 404

@app.get("/")
def home():
    return jsonify({"service": "products", "message": "Products service running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
