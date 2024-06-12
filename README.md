# Priority Inventory Store API

## General Information
This is Priority's official inventory store API repository.
This API provides endpoints for managing inventory items and suppliers, and it returns data in JSON format.
This API is designed to be used by various internal systems, including front-end interfaces (React for web applications and Flutter for mobile applications.) 
and inventory tracking systems. 
This documentation will guide developers on how to set up, use, and extend the API.

## Setup
Prerequisites
- Python 3.8+
- Django 4.0+
- Django REST Framework 3.1+


```bash
pip install -r requirements.txt
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




List all suppliers:






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

## Contributing
still to come



## Contributors
- Benjamin

## Contact Information
[Linkedin](https://linkedin.com/in/benjamin-ogbonna)


## License
still to come