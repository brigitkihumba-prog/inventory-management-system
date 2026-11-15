import requests

def fetch_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v3/product/{barcode}"
    response = requests.get(url,
                            params={"fields": "product_name,brands,ingredients_text,"},
                            headers={"User-Agent": "InventoryApp/1.0"},
                            timeout=10
                            )
    response.raise_for_status()
    data = response.json()
    product = data.get("product")
    if not product:
        return None

    name = product.get("product_name") or product.get("product_name_en")

    if not name:
        return None
    return {
        "name": name,
        "brand": product.get("brands", ""),
        "barcode": barcode,
        "ingredients": product.get("ingredients_text", "")
    }