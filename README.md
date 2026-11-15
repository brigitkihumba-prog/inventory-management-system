# Inventory Management System

# Description

This is a Python Inventory Management System built with Flask.
It allows users to manage products, perform CRUD operations,
and search for product information using the OpenFoodFacts API.

# Features

- View all products
- View a single product
- Add new products
- Update product details
- Delete products
- Search for products 
- Import products from OpenFoodFacts
- Command-line interface

# Technologies Used

- Python
- Flask
- Requests
- Pytest
- OpenFoodFacts API

# Installation
Clone the repository:
```bash
git clone https://github.com/brigitkihumba-prog/inventory-management-system.git
```
Move into the project folder:
```bash
cd inventory-management-system
```
Install dependencies:
```bash
pipenv install
pipenv install --dev pytest
```
# Running the Application

Start the Flask server:
```bash
pipenv run python -m server.app
```
The server runs at:
http://127.0.0.1:5555

# Command Line Interface
Run the CLI in a second terminal:
```bash
pipenv run python cli.py
```
Available options:

1. View inventory
2. Add product
3. Update product
4. Delete product
5. Find product on OpenFoodFacts
6. Add product from OpenFoodFacts
7. Exit

# Running Tests
Run all tests using:
```bash
pipenv run pytest -v
```
# External API
This project uses the OpenFoodFacts API to retrieve product information using barcodes.
API: https://world.openfoodfacts.org/

## Author
BRIGIT KIHUMBA
2026