from flask import Flask, jsonify, request

app = Flask(__name__)

#Inventory
inventory = [
    {
        "id": 1,
        "name": "Coca-Cola 500ml",
        "brand": "Coca-Cola",
        "price": 100,
        "barcode": "123456789",
        "ingredients": "Carbonated water, sugar, flavouring"
    },
    {
        "id": 2,
        "name": "Pepsi 500ml",
        "brand": "Pepsi",
        "price": 90,
        "barcode": "987654321",
        "ingredients": "Carbonated water, sugar, flavouring"
    }
]

#GET all products
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory), 200

#GET one item
@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in inventory:
        if item['id'] == item_id:
            return jsonify(item), 200
        
    return jsonify({"error": "Item not found"}), 404

#POST new item
@app.route('/inventory', methods=['POST'])
def add_item():
    data = request.get_json()
    if not data or not data.get("name"):
        return jsonify({"error": "Product name is required"}), 400

    new_item = {
        "id": max([item['id'] for item in inventory], default=0) + 1,
        "name": data["name"],
        "brand": data.get("brand", ""),
        "price": data.get("price", 0),
        "stock": data.get("stock", 0),
        "barcode": data.get("barcode", ""),
        "ingredients": data.get("ingredients", "")
    }
    inventory.append(new_item)
    return jsonify(new_item), 201

#PUT update item
@app.route('/inventory/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    for item in inventory:
        if item['id'] == item_id:
            for key in ["name", "brand", "price", "stock", "barcode", "ingredients"]:
                if key in data:
                    item[key] = data[key]
            return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

#DELETE item
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in inventory:
        if item['id'] == item_id:
            inventory.remove(item)
            return jsonify({"message": "Item deleted successfully"}), 200
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5555)