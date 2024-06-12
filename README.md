# Priority Inventory Store API

## General Information
This is Priority's official inventory store API repository.
This API provides endpoints for managing inventory items and suppliers, and it returns data in JSON format.
This API is designed to be used by various internal systems, including front-end interfaces (React for web applications and Flutter for mobile applications.) 
and inventory tracking systems. 
This documentation will guide developers on how to set up, use, and extend the API.

This API (Application Programming Interface) is like a bridge that helps 
different parts of priority online store system talk to each other. 
It manages information about the products they sell and the suppliers who provide 
these products. Here’s how it works:

Managing Products:
The API keeps a detailed list of all the items in the store, including their names, 
descriptions, prices, and when they were added to the inventory.
Employees can use the API to add new items, update details about existing items, 
view the details of any item, or remove items that are no longer available.

Managing Suppliers:
The API also keeps track of suppliers, including their names and contact information.
Employees can add new suppliers, update supplier details, and view information 
about each supplier. Connecting Products and Suppliers:

Each product can be supplied by one or more suppliers, and each supplier can provide 
multiple products. The API allows employees to see which suppliers provide a specific 
product and also see all the products provided by a specific supplier.

How It Helps:
- Efficiency: By using this API, the store can quickly and accurately manage inventory and supplier information, 
saving time and reducing errors.
- Integration: The API ensures that all parts of the system (like the website and inventory 
tracking) can easily access and use the same up-to-date information.
- Flexibility: Employees have the tools to easily add, update, or remove products and 
suppliers, helping the business stay organized and responsive to changes.

  
### Setup
Prerequisites
- Python 3.8+
- Django 4.0+
- Django REST Framework 3.1+
- drf-spectacular 0.27+


### Installation
- Clone the repository:
```bazaar
git clone https://github.com/benjaminogbonna/Priority-Inventory-Store
cd Priority-Inventory-Store-master
```
- Create and activate a virtual environment if you haven't done so already:
```bazaar
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```
- Install Libraries/dependencies:
```bazaar
pip install -r requirements.txt
```
- Run database migrations
```bazaar
python manage.py migrate
```
- Create a superuser for employees (optional, for accessing the Django admin):
```bazaar
python manage.py createsuperuser
```
- Start the development server:
```bazaar
python manage.py runserver
```


## API Endpoints and Example Requests & Responses
The base URL for the API is ```http://127.0.0.1:8000/priority-api/```

### Inventory
- List all items: ```GET /priority-api/items/```
```json
[
  {
    "id": 1,
    "name": "laptop",
    "description": "dell laptop",
    "price": "30000.00",
    "date_added": "2024-06-11T11:27:53.034364Z",
    "suppliers": [
      1
    ]
  },
  {
    "id": 2,
    "name": "phone",
    "description": "samsung phone",
    "price": "20000.00",
    "date_added": "2024-06-11T11:34:00.147984Z",
    "suppliers": [
      2
    ]
  },  
  {
    "id": 3,
    "name": "test item",
    "description": "bla bla",
    "price": "22222.00",
    "date_added": "2024-06-11T11:51:25.185021Z",
    "suppliers": [
      1,
      2
    ]
  }
]
```
- Retrieve a single item: ```GET /priority-api/items/{id}/```

Response:
```json
{
  "id": 1,
  "name": "laptop",
  "description": "dell laptop",
  "price": "30000.00",
  "date_added": "2024-06-11T11:27:53.034364Z",
  "suppliers": [
    1
  ]
}
```

- Create a new item: ```POST /priority-api/items/```

Request:
```json
 {
    "name": "laptop",
    "description": "dell laptop",
    "price": "30000.00",
    "suppliers": [
      1
    ]
  }
```
Response:
```json
{
  "id": 1,
  "name": "laptop",
  "description": "dell laptop",
  "price": "30000.00",
  "date_added": "2024-06-11T11:27:53.034364Z",
  "suppliers": [
    1
  ]
}
```

- Update an existing item: ```PUT /priority-api/items/{id}/```

Request:
```json
 {
    "name": "laptop",
    "description": "dell laptop",
    "price": "30500.00",
    "suppliers": [
      1
    ]
  }
```
Response:
```json
{
  "id": 1,
  "name": "laptop",
  "description": "dell laptop",
  "price": "30500.00",
  "date_added": "2024-06-11T11:27:53.034364Z",
  "suppliers": [
    1
  ]
}
```
- Delete an item: ```DELETE /priority-api/items/{id}/```


### Suppliers

- List all suppliers: ```GET /priority-api/suppliers/```
```json
[
  {
    "id": 1,
    "name": "Benjamin",
    "contact_info": "Nigeria,\r\nbenjaim@example.com,\r\n0123456789"
  },
  {
    "id": 2,
    "name": "daniel",
    "contact_info": "nigeria"
  }
]
```

- Retrieve a single supplier: ```GET /priority-api/suppliers/{id}/```
```json
{
  "id": 1,
  "name": "Benjamin",
  "contact_info": "Nigeria,\r\nbenjaim@example.com,\r\n0123456789"
}
```

- Create a new supplier: ```POST /priority-api/suppliers/```

Request
```json
{
  "name": "Benjamin",
  "contact_info": "Nigeria,\r\nbenjaim@example.com,\r\n0123456789"
}
```
Response
```json
{
  "id": 1,
  "name": "Benjamin",
  "contact_info": "Nigeria,\r\nbenjaim@example.com,\r\n0123456789"
}
```

- Update an existing supplier: ```PUT /priority-api/suppliers/{id}/```

Request
```json
{
  "name": "daniel",
  "contact_info": "Abuja, Nigeria"
}
```
Response
```json
{
  "id": 2,
  "name": "daniel",
  "contact_info": "Abuja, Nigeria"
}
```

- Delete a supplier: ```DELETE /priority-api/suppliers/{id}/```


### Inventory-Supplier Relationship
- List suppliers for an item: ```GET /priority-api/items/{id}/suppliers/```

Response
```json
[
  {
    "id": 1,
    "name": "Benjamin",
    "contact_info": "Nigeria,\r\nbenjaim@example.com,\r\n0123456789"
  },
  {
    "id": 2,
    "name": "daniel",
    "contact_info": "nigeria"
  }
]
```
- List items for a supplier: ```GET /priority-api/suppliers/{id}/items/```

Response
```json
[
  {
    "id": 2,
    "name": "phone",
    "description": "samsung phone",
    "price": "20000.00",
    "date_added": "2024-06-11T11:34:00.147984Z",
    "suppliers": [
      2
    ]
  },
  {
    "id": 4,
    "name": "test item",
    "description": "bla bla",
    "price": "22222.00",
    "date_added": "2024-06-11T11:51:25.185021Z",
    "suppliers": [
      1,
      2
    ]
  }
]
```




### Testing
To ensure correct functioning of the API, run the tests included in the inventory/tests.py file
```bazaar
python manage.py test inventory
```

## Contributors
- Benjamin

## Contact Information
[Linkedin](https://linkedin.com/in/benjamin-ogbonna)


## License
still to come