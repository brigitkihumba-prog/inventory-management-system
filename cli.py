import requests

URL = "http://127.0.0.1:5555"

def show_response(response):
    try:
        data = response.json()
    except ValueError:
        print(response.text)
        return
    if not response.ok:
        print("Request failed:", response.status_code)
        print(data)


def show_inventory():
    response = requests.get(f"{URL}/inventory")
    show_response(response)

def add_item():
    name = input("Product name: ")
    brand = input("Brand: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    data = {
        "name": name,
        "brand": brand,
        "price": price,
        "stock": stock
    }
    response = requests.post(f"{URL}/inventory", json=data)
    show_response(response)

def update_item():
    item_id = input("Product ID: ")
    price = float(input("New Price: "))
    stock = int(input("New Stock: "))
    data = {
        "price": price,
        "stock": stock
    }
    response = requests.patch(f"{URL}/inventory/{item_id}", json=data)
    show_response(response)

def delete_item():
    item_id = input("Product ID: ")
    response = requests.delete(f"{URL}/inventory/{item_id}")
    show_response(response)

def find_product():
    barcode = input("Enter product barcode: ")
    response = requests.get(f"{URL}/inventory")
    show_response(response)

def import_product():
    barcode = input("Enter product barcode: ")
    response = requests.get(f"{URL}/inventory/from-api/{barcode}")        
    show_response(response)

def main():
    while True:
        print("\nINVENTORY MANAGEMENT SYSTEM")
        print("1. View Inventory")
        print("2. Add product")
        print("3. Update product")
        print("4. Delete product")
        print("5. Find Product on OpenFoodFacts")
        print("6. Add product from OpenFoodFacts")
        print("7. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == '1':
                show_inventory()
            elif choice == '2':
                add_item()
            elif choice == '3':
                update_item()
            elif choice == '4':
                delete_item()
            elif choice == '5':
                find_product()
            elif choice == '6':
                import_product()
            elif choice == '7':
                print("Goodbye!")
                break
            else:
                print("Invalid Choice")
        except requests.RequestException:
            print("Could not connect to the server")
        except ValueError:
            print("Please enter valid numbers")

            if choice != "7":
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()    
      